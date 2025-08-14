#impor
from logging import exception
from tkinter import *
#gui
window = Tk()
window.geometry("500x500")

#entry box
e=Entry(window,width=54,borderwidth=5,bg="lightblue")
e.place(x=0,y=0)

#buttons
def click(num):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(num))
def clear():
    e.delete(0,END)
def backspace():
    current=e.get()
    e.delete(0,END)
    e.insert(0,current[:-1])
def addition():
    global math
    math ='add'
    n1=e.get()
    global i
    i=int(n1)
    e.delete(0,END)

def sub():
    global math
    math = 'subtraction'
    n1=e.get()
    global i
    i=int(n1)
    e.delete(0,END)
def mul():
    global math
    math= 'multiplication'
    n1=e.get()
    global i
    i=int(n1)
    e.delete(0,END)
def div():
    global math
    math = 'division'
    n1=e.get()
    global i
    i=int(n1)
    e.delete(0,END)
def equal():
    n2 = e.get()
    e.delete(0, END)
    try:
        if math == "add":
            e.insert(0, i + int(n2))
        elif math == "subtraction":
            e.insert(0, i - int(n2))
        elif math == "multiplication":
            e.insert(0, i * int(n2))
        elif math == "division":
            if int(n2) == 0:
                e.insert(0, "Error")
            else:
                e.insert(0, i / int(n2))
    except Exception as ex:
        e.insert(0, "Error")
b=Button(window,text= '1' ,width=12,command=lambda :click(1))
b.place(x=10,y=60)
b=Button(window,text= '2' ,width=12,command=lambda :click(2))
b.place(x=80,y=60)
b=Button(window,text= '3' ,width=12,command=lambda :click(3))
b.place(x=170,y=60)
b=Button(window,text= '4' ,width=12,command=lambda :click(4))
b.place(x=10,y=120)
b=Button(window,text= '5' ,width=12,command=lambda :click(5))
b.place(x=80,y=120)
b=Button(window,text= '6',width=12,command=lambda :click(6))
b.place(x=170,y=120)
b=Button(window,text= '7' ,width=12,command=lambda :click(7))
b.place(x=10,y=180)
b=Button(window,text= '8' ,width=12,command=lambda :click(8))
b.place(x=80,y=180)
b=Button(window,text= '9' ,width=12,command=lambda :click(9))
b.place(x=170,y=180)
b=Button(window,text= '0' ,width=12,command=lambda :click(0))
b.place(x=80,y=240)
Button(window, text='+', width=5,command=addition).place(x=280, y=60)
Button(window, text='-', width=5,command=sub).place(x=280, y=110)
Button(window, text='*', width=5,command=mul).place(x=280, y=160)
Button(window, text='/', width=5,command=div).place(x=280, y=210)
Button(window, text='Clear', width=5,command=lambda:clear()).place(x=280, y=260)   # Clear
Button(window, text='=', width=5,command=equal).place(x=170, y=240)
Button(window, text='⌫', width=12,command=lambda:backspace()).place(x=200, y=290)   ## Equals



#ending
window.mainloop()


