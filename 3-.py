import tkinter as tk

def lienzo():
    root = tk.Tk()
    ventana = tk.Canvas(root,
                        width = 600,
                        height = 600,
                        background = 'blue')

    
    for i in range(0,4):
        ventana.create_line(75,75+150*i, 525,75+150*i , fill = 'red', width = '4')

    for i in range(0,4):
        ventana.create_line(75+150*i,75, 75+150*i,525 , fill = 'red', width = '4')

    return ventana

def control(event):
    global ventana_G
    global tablero
    global contador
    global jugador
    global win
    
    x = (event.x+75)//150
    y = (event.y+75)//150

    if tablero[x-1][y-1] == -1:
        if jugador == 1:
            ventana_G.create_oval(75+150*(x-1),75+150*(y-1),75+150*(x),75+150*(y), fill = 'yellow')
        else:
            ventana_G.create_oval(75+150*(x-1),75+150*(y-1),75+150*(x),75+150*(y), fill = 'green')
        
        contador += 1
        tablero[x-1][y-1] = jugador

    for i in range(0,3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] == jugador:
            print("1")
            win = True
    for i in range(0,3):
        if tablero[0][i] == tablero[1][i] == tablero[2][i] == jugador:
            print("2")
            win = True
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador:
        print("3")
        win = True
    if tablero[2][0] == tablero[1][1] == tablero[0][2] == jugador:
        print("4")
        win = True
    
    if contador > 8 or win:
        if win:
               print("Ha ganado el jugador", jugador+1)
        else:
            print("Game over")  
        ventana_G.unbind('<ButtonRelease-1>')
    else:
       jugador = ((jugador+1)%2)
       
    return

win = False
tablero = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
ventana_G = lienzo()
print("hola")
jugador = 0
contador = 0
ventana_G.pack()

ventana_G.bind('<ButtonRelease-1>',control)

ventana_G.mainloop()
