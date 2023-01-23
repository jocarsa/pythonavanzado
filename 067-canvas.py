from tkinter import *

marco = Frame(width=400,height=400)

lienzo = Canvas()
lienzo.create_oval(30,30,70,70,fill="red")
lienzo.create_oval(130,130,170,170,fill="blue")
lienzo.pack()
