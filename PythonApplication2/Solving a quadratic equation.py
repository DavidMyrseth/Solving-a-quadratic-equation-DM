from tkinter import *
from tkinter import messagebox as mb
import math
import matplotlib.pyplot as plt
import numpy as np

D = 0
t = ""
graf = False

def choice():
    figure_selected = var.get()
    if figure_selected == 1:
        kala()
    elif figure_selected == 2:
        prillid()

def kala():
    x1=np.arange(0,9.5,0.5)
    y1=(2/27)*x1*x1-3
    x2=np.arange(-10,0.5,0.5)
    y2=0.04*x2*x2-3
    x3=np.arange(-9,-2.5,0.5)
    y3=(2/9)*(x3+6)**2+1
    x4=np.arange(-3,9.5,0.5)
    y4=(-1/12)*(x4-3)**2+6
    x5=np.arange(5,9,0.5)
    y5=(1/9)*(x5-5)**2+2
    x6=np.arange(5,8.5,0.5)
    y6=(1/8)*(x6-7)**2+1.5
    x7=np.arange(-13,-8.5,0.5)
    y7=(-0.75)*(x7+11)**2+6
    x8=np.arange(-15,-12.5,0.5)
    y8=(-0.5)*(x8+13)**2+3
    x9=np.arange(-15,-10,0.5)
    y9=[1]*len(x9)
    x10=np.arange(3,4,0.5)
    y10=[3]*len(x10)
    plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10)
    plt.title('Kit')
    plt.xlabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()

def prillid():
    x1 = np.arange(-9, -0.5, 0.5)
    y1 = -(1/16) * (x1 + 5)**2 + 2
    x2 = np.arange(1, 9.5, 0.5)
    y2 = -(1/16) * (x2 - 5)**2 + 2
    x3 = np.arange(-9, -0.5, 0.5)
    y3 = (1/4) * (x3 + 5)**2 - 3
    x4 = np.arange(1, 9.5, 0.5)
    y4 = (1/4) * (x4 - 5)**2 - 3
    x5 = np.arange(-9, -6, 0.5)
    y5 = -(x5 + 7)**2 + 5
    x6 = np.arange(6, 9.5, 0.5)
    y6 = -(x6 - 7)**2 + 5
    x7 = np.arange(-1, 1, 0.01)
    y7 = -0.5 * (x7**2) + 1.5
    plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7)
    plt.title('Prillid')
    plt.xlabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()

def solve():
    global D, t, graf

    ent1_val = ent1.get()
    ent2_val = ent2.get()
    ent3_val = ent3.get()

    if not (ent1_val == "" or ent2_val == "" or ent3_val == ""):
        a = float(ent1_val)
        b = float(ent2_val)
        c = float(ent3_val)

        D=round ((b**2)-(4*a*c))

        if D > 0:
            x1 = round((abs(b) + math.sqrt(D)) / (2 * a), 2)
            x2 = round((abs(b) - math.sqrt(D)) / (2 * a), 2)
            lbl5.configure(text=f"D={D}\nX₁={x1}\nX₂={x2}")
            graf = True
        elif D == 0:
            x = round(abs(b) / (2 * a), 2)
            lbl5.configure(text=f"D={D}\nX={x}")
            graf = True
        else:
            lbl5.configure(text=f"D={D}\nLahendusi pole")
    else:
        mb.showwarning("Tähelepanu!", "On vaja sisestada numbreid!")

def graafik(graf, D):
    global t
    if graf:
        a = float(ent1.get())
        b = float(ent2.get())
        c = float(ent3.get())

        x0 = (-b) / (2 * a)
        y0 = a * x0 * x0 + b * x0 + c
        x1 = np.arange(x0 - 10, x0 + 10, 0.5)
        y1 = a * x1 * x1 + b * x1 + c

        fig = plt.figure()
        plt.plot(x1, y1, 'r-d')
        plt.ylabel('y')
        plt.xlabel('x')
        plt.grid(True)
        plt.show()
        text = f"Porabula tipp ({x0}, {y0})"
    else:
        text = f"Graafikut ei saa kuidagi luua"
    lbl5.configure(text=f"D = {D}\n{t}\n{text}")

aken = Tk()
aken.title("Решение квадратного уравнения") 
aken.geometry("600x300")
aken.title("Tkinteri kasutamine")
tekst = "Pealkiri\n"
lbl=Label(aken, text = "Решение квадратного уравнения",font = "Arial 16",bg = "#bd56e7")
ent1=Entry(aken, font = "Arial 20",fg = "#1c4226",bg = "#bd56e7",width = 4) 
lbl2=Label(aken, text = "x**2+",font = "Arial 16")
ent2=Entry(aken, font = "Arial 20",fg = "#1c4226",bg = "#bd56e7",width = 4) 
lbl3=Label(aken, text = "x+",font = "Arial 16")
ent3=Entry(aken, font = "Arial 20",fg = "#1c4226",bg = "#bd56e7",width = 4) 
lbl4=Label(aken, text = "=0",font = "Arial 16")
lbl5=Label(aken, text = "Решение",font = "Arial 16",bg = "#bd56e7")
btn1=Button(aken, text = "Решать",font = "Arial 12",fg = "#000000",bg = "#bd56e7",width = 14, height = 3,relief = RAISED, command=solve)
btn2=Button(aken, text = "graafik", font = "Arial 12", bg ="#bd56e7", width = 14, height = 3,relief = RAISED, command=lambda: graafik(graf, D))

var=IntVar()
kala_ = Radiobutton(aken, text="Kala", variable=var, value=1, font = "Arial 12", command=choice)
kala_.pack(side = BOTTOM)
prillid_ = Radiobutton(aken, text="Prillid", variable=var, value=2, font = "Arial 12", command=choice)
prillid_.pack(side = BOTTOM)

lbl5.pack(side = BOTTOM)
lbl.pack()
ent1.pack(side = LEFT)
lbl2.pack(side = LEFT)
ent2.pack(side = LEFT)
lbl3.pack(side = LEFT)
ent3.pack(side = LEFT)
lbl4.pack(side = LEFT)
btn1.pack(side = LEFT)
btn2.pack(side = LEFT)

aken.mainloop()