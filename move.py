import tkinter as tk
import random as r

sets_control = [['w','s','a','d'],['i', 'k', 'j', 'l']]
num_piezas = 0
class lienzo(tk.Canvas):
    x = 1000
    y = 1000
    piezas = []
    num_obstaculos = 5
    dist = 100
    tam_obs = 5
    coor = []
    obstaculos = []
    
    def __init__(self, parent):
        self.parent = parent
        tk.Canvas.__init__(self, parent, width = self.x, height = self.y,bg = 'white')


        for i in range(self.num_obstaculos):
            x, y = self.coords()
            self.coor.append([x,y])
            self.obstaculos.append(self.create_oval(x-self.tam_obs,y-self.tam_obs, x+self.tam_obs,y+self.tam_obs, fill = 'yellow', width = '1'))
            
        self.pack()

    def quit(self):
        self.destroy()

    def añadir(self,piezaa):
        if len(self.piezas)+1 < 3:
            piezaa.bind(sets_control[len(self.piezas)])
            for i in sets_control[len(self.piezas)]:
                root.bind(i, piezaa.move)
            self.piezas.append(piezaa)

    def update(self):
        for i in self.piezas:
            i.dibujar()
            self.pack()

        if self.num_obstaculos == 0:
            label = tk.Button(self, text = "You Win", command = quit2)
            label.place(x = self.x/2, y = self.y/2)

    def coords(self):
        valid = False

        while not valid:
            x = r.randint(0,self.x- self.tam_obs)
            y = r.randint(0,self.y- self.tam_obs)

            if len(self.coor) == 0:
                valid = True
            else:
                for i in self.coor:
                    if abs(x-i[0])+ abs(y-i[1]) > self.dist:
                        valid = True

        return x, y

class pieza:
    movex = 0
    movey= 0
    def __init__(self, canvas, diam, color):
        self.diam = diam
        self.canvas = canvas
        canvas = canvas.config()
        self.x = int(canvas['width'][len(canvas['width'])-1])/2
        self.y = int(canvas['height'][len(canvas['height'])-1])/2
        self.id = self.canvas.create_oval(self.x-self.diam,self.y-self.diam, self.x+self.diam,self.y+self.diam, fill = color, width = '0')

    def dibujar(self):
        
        self.canvas.move(self.id, self.movex*self.diam*2, self.movey*self.diam*2)
        self.movex = 0
        self.movey = 0
        colision(self.canvas, self.id)

    def bind(self, binds):
        self.binds = binds

    def move(self, event):
        if event.char == self.binds[0]:
            self.movey = -1
        elif event.char == self.binds[1]:
            self.movey = +1
        elif event.char == self.binds[2]:
            self.movex = -1
        elif event.char == self.binds[3]:
            self.movex = +1

        self.canvas.update()
        
def quit(event):
    root.destroy()

def quit2():
    root.destroy()

def add(event):
    global num_piezas
    if num_piezas < 2:
        ficha = pieza(mapa, 10, input("Elige color ficha: "))
        mapa.añadir(ficha)
        num_piezas += 1

def colision(canvas, pieza):
    caja = canvas.bbox(pieza)
    encontrado = False
    j = 0
    while j < len(canvas.coor) and not encontrado:
        if canvas.coor[j][0] >= caja[0] and canvas.coor[j][1] >= caja[1] and canvas.coor[j][0] <= caja[2] and canvas.coor[j][1] <= caja[3]:
            encontrado = True
            del canvas.coor[j]
            canvas.delete(canvas.obstaculos[j])
            del canvas.obstaculos[j]
            canvas.num_obstaculos -= 1
        j += 1
    
root = tk.Tk()
root.bind("q", quit)
mapa = lienzo(root)
root.bind("+", add)

mapa.update()
root.mainloop()
