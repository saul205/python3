import tkinter as tk
import random as r

turno = 2
players = 4
dado = 0
tam = 600
casilla = tam/10
casilla2 = (tam - 2*casilla) /9
casilla2int = int(casilla2)

piezas = []

cartas = [["Mansion de Ari", 0 , casilla , 120, False, "compra", "none", [10]],
          ["Carta trampa", 0 , casilla+casilla2*1, 110, False, "pagar", "none"],
          ["Piscina de Ari", 0 , casilla+casilla2*2, 0, False,  "compra", "none", [10]],
          ["Yugi oh", 0 , casilla+casilla2*3, 90, False, "carta", "none"],
          ["Overpass", 0 , casilla+casilla2*4, 80, False, "estacion", "none", [10]],
          ["Scarab", 0 , casilla+casilla2*5, 100, False, "compra", "none", [10]],
          ["Comunidad Gamer", 0 , casilla+casilla2*6, 60, False, "carta", "none"],
          ["Merc", 0 , casilla+casilla2*7, 0, False, "compra", "none", [10]],
          ["Octane",0 , casilla+casilla2*8, 50, False, "compra", "none", [10]],
          
          ["YOU DIED", 0 ,0, 0, False, "carcel", "none"],

          ["Centro pokemon", 0 , casilla , 120, False, "compra", "none", [10]],
          ["Bebida energetica", 0 , casilla+casilla2*1, 110, False, "recurso", "none", [10]],
          ["Gimnasio pokemon", 0 , casilla+casilla2*2, 0, False,  "compra", "none", [10]],
          ["Pueblo Paleta", 0 , casilla+casilla2*3, 90, False, "compra", "none", [10]],
          ["Inferno", 0 , casilla+casilla2*4, 80, False, "estacion", "none", [10]],
          ["Clannad", 0 , casilla+casilla2*5, 100, False, "compra", "none", [10]],
          ["Full Metal Alchemist", 0 , casilla+casilla2*6, 60, False, "compra", "none", [10]],
          ["Yugi oh", 0 , casilla+casilla2*7, 0, False, "carta", "none"],
          ["Attack on titan",0 , casilla+casilla2*8, 50, False, "compra", "none", [10]],

          ["Parking", 0 ,0, 0, False, "visitas", "none"],
          
          ["SMITE", 0 , casilla , 120, False, "compra", "none", [10]],
          ["LOL", 0 , casilla+casilla2*1, 110, False, "compra", "none", [10]],
          ["Comunidad Gamer", 0 , casilla+casilla2*2, 0, False, "carta", "none"],
          ["Dota", 0 , casilla+casilla2*3, 90, False, "compra", "none", [10]],
          ["Mirage", 0 , casilla+casilla2*4, 80, False, "estacion", "none", [10]],
          ["Sunakagure", 0 , casilla+casilla2*5, 100, False, "compra", "none", [10]],
          ["Kirikagure", 0 , casilla+casilla2*6, 60, False, "compra", "none", [10]],
          ["Luz", 0 , casilla+casilla2*7, 0, False, "recurso", "none", [10]],
          ["Konoha",0 , casilla+casilla2*8, 50, False, "compra", "none", [10]],

          ["Carcel", 0 , tam-casilla, 0, False, "visitas", "none"],
          
          ["Casa Simpson", casilla , tam-casilla, 120, False, "compra", "none", [10]],
          ["Bar de Moe", casilla+casilla2*1 , tam-casilla, 110, False, "compra", "none", [10]],
          ["Yugi oh", casilla+casilla2*2 , tam-casilla, 0, False, "carta", "none"],
          ["Badulaque", casilla+casilla2*3 , tam-casilla, 90, False, "compra", "none", [10]],
          ["Dust 2", casilla+casilla2*4 , tam-casilla, 80, False, "estacion", "none", [10]],
          ["Goblin ladron", casilla+casilla2*5 , tam-casilla, 100, False, "pagar", "none"],
          ["Castillo de peach", casilla+casilla2*6 , tam-casilla, 60, False, "compra", "none", [10]],
          ["Comunidad Gamer", casilla+casilla2*7 , tam-casilla, 0, False, "carta", "none"],
          ["Castillo de Bowser", casilla+casilla2*8 , tam-casilla, 50, False, "compra", "none", [10]],
          
          ["Salida", tam-casilla , tam-casilla, 0, False, "salida" , "none", [10]]]



indice_carta = 0

def crear_jugadores():
    global piezas
    for i in range(players):
        piezas.append([ i, "abajo", 500, [], cartas[len(cartas)-1], 0])

def ejecucion():
    global piezas
    global frame3
    global frame2
    global tablero
    if frame3[1]:
        destruir3()
    frame3[0] = tk.Frame(tablero, bg = 'white')
    frame3[0].place(x = casilla*2, y = casilla*2)
    frame3[1] = True
    dados()
    piezas = mover_piezas(tablero, piezas)
    
def actualizar():
    var3.set("Jugador: %d, saldo: %d"%(turno,piezas[turno-1][2]))
    txt_marcador.config(text=texto_mar())

def dados():
    global turno
    global dado
    turno = turno%players + 1
    var.set("Turno: "+ str(turno))
    dado = r.randint(1,6)
    var2.set("Dado: "+ str(dado))
    
def compra():
    global indice_carta
    global cartas
    global piezas
    global frame3
    piezas[turno-1][2] -= cartas[indice_carta][3]
    cartas[indice_carta][4] = True
    cartas[indice_carta][6] = turno
    piezas[turno-1][3].append(cartas[indice_carta])
    if cartas[indice_carta][5] == "estacion":
        piezas[turno-1][5] += 1
        print(piezas[turno-1])
    frame3[2].destroy()
    actualizar()

##def colorear(lienzo):
##    for i in cartas:
        
def crear_tablero(num_jugadores):
    root = tk.Tk()
    ventana = tk.Canvas(root, width = tam, height = tam, background = 'white')

##    colorear(ventana)

    for i in range(1, 9):
        ventana.create_line(0,casilla + casilla2*i, casilla,casilla + casilla2*i, fill = 'black', width = '3')
        ventana.create_line(tam - casilla,casilla + casilla2*i, tam,casilla + casilla2*i, fill = 'black', width = '3')

    for i in range(1,9):
        ventana.create_line(casilla + casilla2*i,0, casilla + casilla2*i,casilla, fill = 'black', width = '3')
        ventana.create_line(casilla + casilla2*i, tam - casilla, casilla + casilla2*i,tam, fill = 'black', width = '3')

        
    ventana.create_line(casilla,0, casilla,tam, fill = 'black', width = '3')
    ventana.create_line(tam - casilla,0, tam - casilla,tam, fill = 'black', width = '3')
    ventana.create_line(0,casilla, tam,casilla, fill = 'black', width = '3')
    ventana.create_line(0,tam - casilla, tam,tam - casilla, fill = 'black', width = '3')

    ventana.create_polygon(tam - casilla, tam-casilla,
                           tam - casilla, tam,
                           tam , tam- casilla,
                           tam, tam,
                           fill = 'purple')

    var = tk.StringVar()
    var2 = tk.StringVar()

    button = tk.Button(ventana, text = "Tirar Dado", command = ejecucion)    
    button.place(height = 40, width = 100, x = tam - (2*casilla + 50) , y = tam - (casilla + 82))

    button2 = tk.Button(ventana, text = "Acabar", command = root.quit)    
    button2.place(height = 40, width = 100, x = tam - (2*casilla + 200) , y = tam - (casilla + 82))

    label = tk.Label(ventana, font='Arial', bg='white', textvariable = var)
    label.place( height=20, width=100, x = tam - (2*casilla + 70) , y = tam - (casilla + 122))

    label = tk.Label(ventana, font='Arial', bg='white', textvariable = var2)
    label.place( height=20, width=100, x = tam - (2*casilla + 70) , y = tam - (casilla + 102))

    frame = tk.Frame(ventana)
    
    return ventana, var, var2, root, [frame, False, 0]

def construir_marcador():
    root = tk.Tk()

    label = tk.Label(root ,font='Arial', bg='white', text = texto_mar(), width = 75,anchor = 'nw', justify = 'left')
    label.pack()
    
    return root, label

def texto_mar():
    texto= ''
    for i in range(players):
        texto += 'Jugador'+str(i+1)+':\n\t-Casilla= '+piezas[i][4][0]+'\n\t-Saldo: '+str(piezas[i][2])+'\n\t-Cartas:\n'
        for j in piezas[i][3]:
            texto += '\t\t*'+j[0]+", pago al caer: "+ str(j[7][0])+'\n'

    return texto


def dibujar_piezas(tablero):
    global piezas
    
    p1 = []
    p1.append(tablero.create_oval(tam - casilla, tam - casilla,  tam - casilla+ casilla2/2, tam - casilla + casilla2/2, fill = 'red'))
    p1.append(tablero.create_oval(tam - casilla+casilla2/2, tam - casilla,  tam-casilla +casilla2, tam - casilla + casilla2/2, fill = 'blue'))
    p1.append(tablero.create_oval(tam - casilla, tam-casilla +casilla2/2,  tam-casilla +casilla2/2, tam - casilla + casilla2, fill = 'pink'))
    p1.append(tablero.create_oval(tam - casilla + casilla2/2, tam-casilla +casilla2/2,  tam - casilla + casilla2, tam - casilla + casilla2, fill = 'green'))

    for i in range(players):
        piezas[i][0] = p1[i]


def mover_piezas(tablero,p1):
    i = 0
    while i < dado:
        if p1[turno-1][1] == "abajo":
            if int(tablero.coords(p1[turno-1][0])[0]) < casilla2int:
                p1[turno-1][1] = "izq"
            else:
                tablero.move(p1[turno-1][0], -casilla2, 0)
                i += 1
                casillasal(tablero, p1[turno-1])
        elif p1[turno-1][1] == "izq":
            if int(tablero.coords(p1[turno-1][0])[1]) < casilla2int:
                p1[turno-1][1] = "arriba"
            else:
                tablero.move(p1[turno-1][0], 0,-casilla2)
                i += 1
                casillasal
        elif p1[turno-1][1] == "arriba":
            if int(tablero.coords(p1[turno-1][0])[0]) >= int(tam-casilla):
                p1[turno-1][1] = "dcha"
            else:
                tablero.move(p1[turno-1][0], casilla2, 0)
                i += 1
                casillasal(tablero, p1[turno-1])
        elif p1[turno-1][1] == "dcha":
            if int(tablero.coords(p1[turno-1][0])[1]) >= int(tam-casilla):
                p1[turno-1][1] = "abajo"
            else:
                tablero.move(p1[turno-1][0], 0, casilla2)
                i += 1
                casillasal(tablero, p1[turno-1])

    p1[turno-1] = casillas(tablero, p1[turno-1])
        
    return p1

def comparar_casilla(tablero, pieza, i):
        
                piezas[turno-1][4] = cartas[i]
                txt_marcador.config(text=texto_mar())
                
                if cartas[i][5] == "compra" or cartas[i][5] == "recurso" or cartas[i][5] == "estacion":
                    mensaje(tablero,i, pieza)
                    crear_compra(tablero,i, pieza)
                    
                elif cartas[i][5] == "visitas":
                    mensaje(tablero,i, pieza)

                return True

                    
def casillas(tablero, pieza):
    encontrado = False
    i = len(cartas)-2
    while i >= 0 and not encontrado:
        
        if pieza[1] == "abajo":
            if tablero.coords(pieza[0])[0] >= cartas[i][1]-1 and tablero.coords(pieza[0])[1] >= cartas[i][2]-1 and tablero.coords(pieza[0])[0] < cartas[i+1][1]-1:
                encontrado = comparar_casilla(tablero, pieza, i)

        elif pieza[1] == "izq":
            if tablero.coords(pieza[0])[0] >= cartas[i][1]-1 and tablero.coords(pieza[0])[1] >= cartas[i][2]-1 and tablero.coords(pieza[0])[1] < cartas[i+1][2]-1 and tablero.coords(pieza[0])[0] < casilla + 1:
                encontrado = comparar_casilla(tablero, pieza, i)

        elif pieza[1] == "arriba":
            if tablero.coords(pieza[0])[0] >= cartas[i][1]-1 and tablero.coords(pieza[0])[1] >= cartas[i][2]-1 and tablero.coords(pieza[0])[1] < cartas[i+1][2]-1 and tablero.coords(pieza[0])[1] < casilla + 1:
                encontrado = comparar_casilla(tablero, pieza, i)
                
        elif pieza[1] == "dcha":
            if tablero.coords(pieza[0])[0] >= cartas[i][1]-1 and tablero.coords(pieza[0])[1] >= cartas[i][2]-1 and tablero.coords(pieza[0])[1] < cartas[i+1][2]-1:
               encontrado = comparar_casilla(tablero, pieza, i)
               
        i -= 1

    return pieza

def crear_compra(tablero, i, pieza):
    global indice_carta
    global frame3
    global piezas

    if not cartas[i][4] and pieza[2] >= cartas[i][3]:

        indice_carta = i
        label = tk.Label(frame3[0] ,font='Arial', bg='white', text = "Precio: %d"%cartas[i][3])
        label.grid(row = 3, sticky = 'NW')
        frame3[2] = tk.Button(frame3[0], text = "Comprar", command = compra)
        frame3[2].grid(row = 3, sticky = 'NE')

    elif cartas[i][4] and cartas[i][6] != turno:
## si no puede pagar se elimina, no implementado, pensando como eliminar jugadores
        if cartas[i][5] == "recurso":
            pagar = cartas[i][7][0]*dado
        elif cartas[i][5] == "estacion":
            pagar = cartas[i][7][0]*pieza[5]
        else:
            pagar = cartas[i][7][0]
        print(pagar)
        pieza[2] -= pagar
        piezas[cartas[i][6]-1][2] += pagar
        label = tk.Label(frame3[0] ,font='Arial', bg='white', text = "Jugador%d paga a Jugador%d %d"%(turno, cartas[i][6], pagar))
        label.grid(sticky = 'NW')
        actualizar()

    return pieza

def mensaje(tablero, i, pieza):
    global frame3

    var3.set("Jugador: %d, saldo: %d"%(turno,piezas[turno-1][2]))
    label1 = tk.Label(frame3[0] ,font='Arial', bg='white', textvariable = var3)
    label1.grid(row = 1, sticky = 'NW')
    salida = "Casilla: "+cartas[i][0]
    label = tk.Label(frame3[0] ,font='Arial', bg='white', text = salida)
    label.grid(row = 2, sticky = 'NW')


def destruir3():
    global frame3

    frame3[0].destroy()
    frame3[1] = False


def casillasal(tablero, pieza):
    global frame2

    if tablero.coords(pieza[0])[0] >= tam-casilla and tablero.coords(pieza[0])[1] >= tam-casilla:

        salida = str(turno)+" ha pasado por la casilla de salida"
        label = tk.Label(frame3[0] ,font='Arial', bg='white', text = salida)
        label.grid(row = 0, sticky = 'NW')

        pieza[2] += 100
        
tablero, var, var2, root, frame3 = crear_tablero(4)
var3 = tk.StringVar()

crear_jugadores()
marcador, txt_marcador = construir_marcador()

dibujar_piezas(tablero)

tablero.pack()

tablero.mainloop()

root.destroy()
marcador.destroy()

