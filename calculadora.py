from tkinter import *
import tkinter as tk
root = tk.Tk()

root.sum = 0

def combo_simples():
    root.sum += 350
    L['text'] = 'soma ' + str(root.sum)


def combo_super():
    root.sum += 475
    L['text'] = 'soma: ' + str(root.sum)


def combo_ultra():
    root.sum += 575
    L['text'] = 'soma: ' + str(root.sum)


def burg():
    root.sum += 150
    L['text'] = 'soma: ' + str(root.sum)


def aneis():
    root.sum += 100
    L['text'] = 'soma: ' + str(root.sum)


def refri():
    root.sum += 100
    L['text'] = 'soma: ' + str(root.sum)


def suco():
    root.sum += 125
    L['text'] = 'soma: ' + str(root.sum)


def cafe():
    root.sum += 100
    L['text'] = 'soma: ' + str(root.sum)


def reset():
    root.sum -= root.sum
    L['text'] = 'soma: ' + str(root.sum)


b1 = Button(root, text="Combo Simples", command=combo_simples)
b1.pack()
b2 = Button(root, text="Combo Super",  command=combo_super)
b2.pack()
b3 = Button(root, text="Combo Ultra", command=combo_ultra)
b3.pack(),
b4 = Button(root, text="Hamburgue", command=burg)
b4.pack()
b5 = Button(root, text="aneis de cebola", command=aneis)
b5.pack()
b6 = Button(root, text="refrigerante", command=refri)
b6.pack()
b7 = Button(root, text="suco", command=suco)
b7.pack()
b8 = Button(root, text="café", command=cafe)
b8.pack()
b9 = Button(root, text="Limpar", command=reset)
b9.pack()


L = Label(root, text="soma: " + str(root.sum))
L.pack()

root.mainloop()
