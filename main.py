from tkinter import *
from tkinter import ttk
from math import *
import webbrowser
import tkinter.font as font
from PIL import Image, ImageTk

calc = Tk()
calc.title('Калькулятор')
calc.resizable(False, False)
calc.iconbitmap('calc.ico')
rel = ""
r = 2
c = 0

button = [
    'Author', 'CE', 'C', '<',
    '1/x', 'xⁿ', '√', '/',
    '7', '8', '9', 'x',
    '4', '5', '6', '-',
    '1', '2', '3', '+',
    '±', '0', '.', '=',
]
s = ttk.Style()
s.configure('my.TButton', font=('Helvetica', 14, 'bold'))

for i in button:
    rel = ''
    cmd = lambda x=i: calc1(x)
    ttk.Button(calc, text=i, command=cmd, style='my.TButton').grid(row=r, column=c, ipady=5, ipadx=1)
    c += 1
    if c == 4:
        c = 0
        r += 1
calc_entry = Entry(calc, bd='0', font="Helvetica 25 bold", justify="right")
calc_entry.grid(row=1, column=0, columnspan=5, ipady=1, ipadx=90)
eniq = Entry(calc, bd='0', fg='#cccccc', font="Helvetica 25 bold", justify="right")
eniq.grid(row=0, column=0, columnspan=5, ipady=10, ipadx=90)


def calc1(num):
    if num == '0':
        calc_entry.insert(END, "0")
        eniq.insert(END, "0")
    if num == '1':
        calc_entry.insert(END, "1")
        eniq.insert(END, "1")
    if num == '2':
        calc_entry.insert(END, "2")
        eniq.insert(END, "2")
    if num == '3':
        calc_entry.insert(END, "3")
        eniq.insert(END, "3")
    if num == '4':
        calc_entry.insert(END, "4")
        eniq.insert(END, "4")
    if num == '5':
        calc_entry.insert(END, "5")
        eniq.insert(END, "5")
    if num == '6':
        calc_entry.insert(END, "6")
        eniq.insert(END, "6")
    if num == '7':
        calc_entry.insert(END, "7")
        eniq.insert(END, "7")
    if num == '8':
        calc_entry.insert(END, "8")
        eniq.insert(END, "8")
    if num == '9':
        calc_entry.insert(END, "9")
        eniq.insert(END, "9")
    if num == '=':
        result = eval(eniq.get())
        calc_entry.delete(0, END)
        eniq.insert(END, '=')
        calc_entry.insert(END, int(result))
    if num == '+':
        calc_entry.insert(END, "+")
        eniq.insert(END, "+")
        calc_entry.delete(0, END)
    if num == '-':
        calc_entry.insert(END, "-")
        eniq.insert(END, "-")
        calc_entry.delete(0, END)
    if num == '/':
        calc_entry.insert(END, "/")
        eniq.insert(END, "/")
        calc_entry.delete(0, END)
    if num == 'x':
        calc_entry.insert(END, '*')
        eniq.insert(END, "*")
        calc_entry.delete(0, END)
    if num == 'C':
        calc_entry.delete(0, END)
        eniq.delete(0, END)
    if num == 'xⁿ':
        calc_entry.insert(END, '**')
        eniq.insert(END, "**")
        calc_entry.delete(0, END)
    if num == '<':
        calc_entry.delete(len(calc_entry.get()) - 1)
        eniq.delete(len(eniq.get()) - 1)
    if num == '.':
        calc_entry.insert(END, '.')
        eniq.insert(END, ".")
    if num == '±':
        result = calc_entry.get()
        calc_entry.delete(0, END)
        calc_entry.insert(END, int(result) * -1)
        eniq.delete(0, END)
        eniq.insert(END, int(result) * -1)
    if num == '√':
        result = calc_entry.get()
        calc_entry.delete(0, END)
        calc_entry.insert(END, sqrt(int(result)))
        eniq.delete(0, END)
    if num == '1/x':
        result = calc_entry.get()
        calc_entry.delete(0, END)
        eniq.delete(0, END)
        calc_entry.insert(END, 1 / int(result))
    if num == 'CE':
        for i in range(len(calc_entry.get())):
            eniq.delete(len(eniq.get()) - 1)
        calc_entry.delete(0, END)
    if num == 'Author':
        webbrowser.open('https://vk.com/jenik_s', new=2)


calc.mainloop()
