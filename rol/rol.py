import random
import os

armas = ["Espada","Katana","Gran Espada"]

class mage:
    name = "mage"
    maxlife = 100
    maxmana = 150
    damage = 20
    skills_datos = [[1,0],[2,25],[3.5,75]]
    skills_nombre = ["Auto", "Fireball", "Spark"]

class warrior:
    name = "warrior"
    maxlife = 200
    maxmana = 50
    damage = 30
    skills_datos = [[1,0],[1.25,10],[1.75,30]]
    skills_nombre = ["Auto", "Shield Bash", "Stab"]

class archer:
    name = "archer"
    maxlife = 100
    maxmana = 100
    damage = 35
    skills_datos = [[1,0],[1.8,45],[1.45,25]]
    skills_nombre = ["Auto", "Charged Shot", "Rapid Fire"]

class objeto:
    def __init__(self, nombre):
        self.name = nombre

    def cons(self):
        self.usos = 1
        self.type = "consumible"

    def wep(self, numMon):
        self.daño = (numMon+1) *5
        self.equip = False
        self.type = "weapon"

    def addUso(self):
        self.usos += 1

def equipar(heroe, nombre):
    encontrado = False
    i = 0
    while i < heroe.numInv and not encontrado:
        if heroe.inv[i].name == nombre:
            heroe.inv[i].equip = True
            heroe.wepdam += heroe.inv[i].daño
            heroe.arma = True
            encontrado = True
        else:
            i += 1
    if not encontrado:
        print("No existe ese objeto")
    
class hero:

    def __init__(self, clase, nombre):
        self.name = nombre
        if clase == "mage":
            self.clas = mage
        elif clase == "warrior":
            self.clas = warrior
        elif clase == "archer":
            self.clas = archer
        self.clas.life = self.clas.maxlife
        self.clas.mana = self.clas.maxmana
        self.level = 0
        self.exp = 0
        self.siglvl = 1000
        self.basexp = 1000
        self.inv = []
        self.numInv = 0
        self.maxInv = 5
        self.arma = False
        self.wepdam = 0

    def dibujarvm(self):
        vida = int(self.clas.life)
        manaa = int(self.clas.mana)
        print("VIDA: ", end = '')
        for i in range((vida//10)*2):
            print("|", end = '')
        print("   MANA: ", end = '')
        for j in range((manaa//10)*2):
            print("|", end = '')

    def print_clase(self):
        print(self.name, "\n" + self.clas.name, " NIVEL:", self.level)
        print("Experiencia : ", int(self.exp), "/", int(self.siglvl))
        self.dibujarvm()
        print("  DAÑO:", int(self.clas.damage),"\nHabilidades:")
        for i in range(len(self.clas.skills_nombre)):
            print(i,") ",self.clas.skills_nombre[i], "- Multiplicador:", self.clas.skills_datos[i][0],"- Coste:",self.clas.skills_datos[i][1])
    
    def level_up(self):
        self.level += 1
        self.clas.maxlife = self.clas.maxlife * 1.1
        self.clas.maxmana = self.clas.maxmana * 1.1
        self.clas.life = self.clas.maxlife
        self.clas.mana = self.clas.maxmana
        self.clas.damage = self.clas.damage*1.1

    def mostrarInv(self):
        print("Objetos:")
        if self.numInv == 0:
            print("- None")
        else:
            for i in range(self.numInv):
                if self.inv[i].type == "consumible":
                    print("-", self.inv[i].name, ":", self.inv[i].usos)
                if self.inv[i].type == "weapon":
                    print("-", self.inv[i].name, ", Dano:", self.inv[i].daño, "Equipado:", self.inv[i].equip)

    def addObj(self, nombre, objeto):
        if len(self.inv) == self.maxInv:
            print("Inventario lleno")
        else:
            encontrado = False
            i = 0
            while i < len(self.inv) and not encontrado:
                if self.inv[i].name == nombre:
                    encontrado = True
                    if self.inv[i].type == "consumble":
                        self.inv[i].addUso()
                else:
                    i += 1
            if not encontrado:
                self.inv.append(objeto)
                self.numInv += 1

class monster:
    def __init__(self, numero):
        self.life = random.randint(50,100)*(1.25**(int(numero/10)))
        self.damage = random.randint(5, 15)*(1.25**(int(numero/10)))
        self.skills = [round(random.uniform(1.25, 1.75), 2),round(random.uniform(1, 1.5), 2),
                       round(random.uniform(1.25, 1.75), 2),round(random.uniform(1, 1.5), 2)]
        self.level = int(numero/10)

    def print_datos(self):
        print("MONSTRUO- Nivel: ", self.level, " Vida:", round(self.life, 2), "Daño:", round(self.damage, 1))

def attack_monster(heroe, enemigo):
    multiplicador = enemigo.skills[random.randint(0,3)]
    heroe.clas.life -= enemigo.damage*multiplicador
    if heroe.clas.life < 0:
        heroe.clas.life = 0
    return enemigo.damage*multiplicador

def attack_hero(heroe, ataque, enemigo):
    encontrado = False
    i = 0
    while i < len(heroe.clas.skills_nombre) and not encontrado:
        if ataque == heroe.clas.skills_nombre[i]:
            encontrado = True
            coste = heroe.clas.skills_datos[i][1]
            if heroe.clas.mana > coste:
                multiplicador = heroe.clas.skills_datos[i][0]
                
                enemigo.life = enemigo.life - (heroe.clas.damage + heroe.wepdam)*multiplicador
                if enemigo.life < 0:
                    enemigo.life = 0
                heroe.clas.mana = heroe.clas.mana - coste
                return (heroe.clas.damage + heroe.wepdam)*multiplicador
            else: 
                print("No Mana, elige otro")
                return attack_hero(heroe,  input("Elige ataque: "), enemigo)
        else:
            i += 1
    if not encontrado:
        print("Ese ataque no existe, selecciona otro: ")
        return attack_hero(heroe,  input("Elige ataque: "), enemigo)

def listarMenu():
    print("\nMENU\n========\n-Atacar\n-Inventario\n-Guardar\n-Guardar y salir\n")

def mostrarInfo(heroe1, monster1, danoH, danoM, derrotados, drop, arma):
    os.system("cls")
    heroe1.print_clase()
    print()
    monster1.print_datos()

    print("Daño provocado :", danoH, "  Daño recibido: ", round(danoM, 2) )
    
    print("Monstruos derrotados =", derrotados)

    if arma:
        item = objeto(armas[derrotados//10])
        item.wep(derrotados//10)
        heroe1.addObj(item.name, item)
        print("\nAñadida", item.name)
    elif drop:
        item = objeto("Pocion")
        item.cons()
        heroe1.addObj("Pocion", item)
        print("\nPOCION AÑADIDA")

def validClas(clase):
    if clase == "archer" or clase == "mage" or clase == "warrior":
        return True
    else:
        return False

def checkfile(archivo):
    try:
        fichero = open(archivo)
        fichero.close()
        return True
    except:
        return False

def guardar(heroe, derrotados, final):
    fichero = heroe.name + "_savefile.txt"
    f = open(fichero, 'w')
    if final:
        f.write(heroe.name + '\n' + heroe.clas.name + '\n' + str(heroe.clas.maxlife) + '\n' + str(heroe.clas.maxmana) + '\n' 
                + str(heroe.clas.damage) + '\n' + str(heroe.clas.maxlife) + '\n' + str(heroe.clas.maxmana) + '\n' 
                + str(heroe.level) + '\n' + str(heroe.exp) + '\n' + str(heroe.siglvl) + '\n' + str(heroe.basexp) + '\n' + str(derrotados))
    else:
        f.write(heroe.name + '\n' + heroe.clas.name + '\n' + str(heroe.clas.maxlife) + '\n' + str(heroe.clas.maxmana) + '\n' 
                + str(heroe.clas.damage) + '\n' + str(heroe.clas.life) + '\n' + str(heroe.clas.mana) + '\n' 
                + str(heroe.level) + '\n' + str(heroe.exp) + '\n' + str(heroe.siglvl) + '\n' + str(heroe.basexp) + '\n' + str(derrotados))
    f.close

def cargar(heroe, f):
    heroe.clas.maxlife = float(f.readline().rstrip('\n'))
    heroe.clas.maxmana = float(f.readline().rstrip('\n'))
    heroe.clas.damage = float(f.readline().rstrip('\n'))
    heroe.clas.life = float(f.readline().rstrip('\n'))
    heroe.clas.mana = float(f.readline().rstrip('\n'))
    heroe.level = int(f.readline().rstrip('\n'))
    heroe.exp = int(f.readline().rstrip('\n'))
    heroe.siglvl = float(f.readline().rstrip('\n'))
    heroe.basexp = int(f.readline().rstrip('\n'))
    derrotados =  int(f.readline().rstrip('\n'))
    return derrotados

def inicio():
    modo = input("Elige(1,2):\n-Crear personaje\n-Cargar personaje\n")
    if modo == "1" or modo == "2":
        if modo == "1":
            personaje = input("Elige un nombre: ")
            clase = input("Elige una clase(mage, warrior, archer): ")
            os.system("cls")
            while not validClas(clase):
                clase = input("Clase no válida.\nElige una clase(mage, warrior, archer): ")
            os.system("cls")
            return clase, personaje
        elif modo == "2":
            nombre = input("Nombre del personaje: ")
            print()
            fichero = nombre+"_savefile.txt"
            if checkfile(fichero):
                return fichero, nombre
            else:
                print("No hay guardado")
                return inicio()
    else:
        return inicio()

def main():
    entrada,personaje = inicio()
    if validClas(entrada):
        heroe1 = hero(entrada, personaje)
        heroe1.print_clase()
        derrotados = 0
        print()
    else:
        f = open(entrada)
        nombre = f.readline().rstrip('\n')
        clase = f.readline().rstrip('\n') 
        heroe1 = hero(clase, nombre)
        derrotados = cargar(heroe1, f)
        heroe1.print_clase()
        f.close()

    numMon = 0
    muerto = False
    exit = False
    while heroe1.clas.life != 0 and not exit: 
        drop = False
        arma = False
        if muerto:
            print("Monstruo muerto\n")
            muerto = False
        if numMon == 0:
            monster1 = monster(derrotados)
            print("Nuevo  ", end = '')
            monster1.print_datos()
            print("Monstruos derrotados:", derrotados)
            numMon += 1
        else:
            listarMenu()
            opcion = input("Elige una opcion(1,2,3, 0 para salir): ")
            if opcion == "1":
                danoH = attack_hero(heroe1, input("\nElige ataque: "), monster1)
                if monster1.life <= 0:
                    numMon -= 1
                    derrotados += 1
                    muerto = True
                    danoM = 0
                    heroe1.exp += monster1.level*50 + 250
                    if random.randint(0,10) == 0:
                        drop = True
                    if random.randint(0, 1) == 0:
                        arma = True
                else:
                    danoM = attack_monster(heroe1, monster1)
                heroe1.clas.mana += random.randint(2,10)
                if heroe1.clas.mana > heroe1.clas.maxmana:
                    heroe1.clas.mana = heroe1.clas.maxmana * 1.1**heroe1.level
                if heroe1.exp >= heroe1.siglvl:
                    heroe1.level_up() 
                    heroe1.siglvl += 500**(1.05**heroe1.level) + heroe1.basexp
                mostrarInfo(heroe1, monster1, danoH, danoM, derrotados, drop, arma)       
            elif opcion == "2":
                heroe1.mostrarInv()
                if heroe1.numInv != 0:
                    if input("Usar Objeto? ") == "si":
                        obj = input("Que quieres hacer: ")
                        if obj == "equipar":
                            que = input("Que quieres equipar")
                            equipar(heroe1, que)
                        elif obj == "pocion": 
                            heroe1.clas.life += 25
                            heroe1.inv[0].usos -= 1
                            if heroe1.inv[0].usos <= 0:
                                heroe1.numInv -= 1
                            if heroe1.clas.life > heroe1.clas.maxlife:
                              heroe1.clas.life = heroe1.clas.maxlife
                            danoH = 0
                            danoM = attack_monster(heroe1, monster1)
                            mostrarInfo(heroe1, monster1, danoH, danoM, derrotados, drop, arma)
                            print("Pocion usada")
            elif opcion == "3":
                guardar(heroe1, derrotados, False)
            elif opcion == "0":
                exit = True

    print("\nGame Over")
    if exit:
        guardar(heroe1, derrotados, False)
    else:
        guardar(heroe1, 0, True)
os.system("cls")
main()
