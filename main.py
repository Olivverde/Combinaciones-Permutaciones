
#---------------------------------------------------------------------
# UNIVERSIDAD DEL VALLE DE GUATEMALA
# MARTIN AMADO GIRON 19XXX
# OLIVER JOSUE DE LEON MILIAN 19270
#---------------------------------------------------------------------


# Imports
from itertools import permutations
from itertools import combinations
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from os import path
from PIL import Image, ImageTk
import os

# Stuff
n = []
e = ''
k = ''

# Interface
root = Tk()

# GUI design
canvas = Canvas(root, width = 1024, height = 576)
photo = ImageTk.PhotoImage(Image.open("kirby_bg.png"))
canvas.create_image(0,0,anchor = NW, image = photo)
canvas.pack()

# Title
root.title('Permutaciones y Combinaciones')

# Icon Photo
root.call('wm', 'iconphoto', root._w, PhotoImage(file='kirby.png'))
root.resizable(False,False)
frame = Frame()
frame.pack()

# GUI main label
label = Label(root, text = 'PERMUTACIONES\n&\nCOMBINACIONES', font = ('Bold','32'), fg='white', bg='turquoise4')
label.place(x = 50, y = 15)

# Functions ---------------------------------------------------------------------------------

# Asks the way out
def closing():
    if messagebox.askokcancel("Close program","¿Seguro que quiere salir del programa?"):
        root.destroy()
        
# Gets entries values      
def get_entry():
    global e
    global k
    
    flag = 0
    e = entry_1.get()
    k = entry_2.get()
    print(len(e))
    if ((len(e) > 0) | (k != '')):
        try:
            k = int(k) # ¿int?
            split_entry(e)
            print(n)
            if ((k > len(n)) & (k <= 0)):
                messagebox.showerror(title='Wrong Data',message='INGRESE UN DATO VALIDO')
                flag += 1
        except:
            messagebox.showerror(title='Wrong Data',message='INGRESE UN DATO VALIDO')
            flag += 1
    else:
        messagebox.showerror(title='Missing Data',message='INGRESE los datos REQUERIDOS')
        flag += 1
    return flag
        
# Split the entry
def split_entry(e):
    global n
    for i in e:
        n.append(i)

# Permutates using k entry 
def permutation():
    global e
    global k
    global n
    f = get_entry()
    if (f > 0):
        e = ''
        k = ''
    else:
        print(list(permutations(n,k)))
        n = []

def combination():
    global e
    global k
    global n
    f = get_entry()
    if (f > 0):
        e = ''
        k = ''
    else:
        print(list(combinations(n,k)))
        n = []

    
# Extra labels & buttons------------------------------------------------------------
# Labels
label_1 = Label(root, text = 'Conjunto N', font = ('Calibri Bold','12'), fg='white', bg='gray13')
label_1.place(x = 175, y = 200)
label_2 = Label(root, text = 'K a seleccionar', font = ('Calibri Bold','12'), fg='white', bg='gray13')
label_2.place(x = 175, y = 260)

# Entries
entry_1 = ttk.Entry()
entry_1.place(x=80, y=230, width=300)
entry_2 = ttk.Entry()
entry_2.place(x=80, y=290, width=300)

# Buttons
Button(text = 'PERMUTAR', bg='turquoise4', fg='gray97', font = ('Calibri Bold','10'),command = permutation).place(x = 175, y = 350)
Button(text = 'COMBINAR', bg='turquoise4', fg='gray97', font = ('Calibri Bold','10'),command = combination).place(x = 175, y = 390)


# Exit protocol
root.protocol("WM_DELETE_WINDOW", closing)


root.mainloop()