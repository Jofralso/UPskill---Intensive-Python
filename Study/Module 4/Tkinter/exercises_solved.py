'''
Ex. 1

Criar uma janela pricipal com um campo de introdução de texto com um botão a dizer mostrar mensagem, 
quando clicado aparece uma messagebox com o título mensagem e conteúdo :Olá, _texto introduzido_

import tkinter as tk
from tkinter import messagebox

def show_message():
    user_input = entry.get()
    messagebox.showinfo("Mensagem", f"Olá, {user_input}")

def main():
    global entry  # Declare 'entry' as a global variable
    root = tk.Tk()
    root.title("Entry and Messagebox")
    root.geometry("300x200")

    label = tk.Label(root, text="Introduza mensagem:", font=("Helvetica", 14))
    label.pack(pady=10)

    entry = tk.Entry(root, font=("Helvetica", 12))
    entry.pack(pady=10)

    button = tk.Button(root, text="Mostrar mensagem", command=show_message)
    button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
'''
'''
Ex. 2

Write a program that asks the user to type  a word and return him its reverse without using any predefined function . 
Example if the user enters the word python, the program returns nohtyp to him as shown in the figure below:

from tkinter import *

root = Tk()
root.geometry('400x150')

def action():
    word = entryWord.get()
    # initialise the reversed word 
    reversed_word = ""
    for x in word:
        reversed_word = x + reversed_word
    lblResult['text'] = reversed_word
        

# Create label and entry word
lblWord = Label(root , text ='Enter a word : ')
lblWord.place( x = 20 , y = 20 )
entryWord = Entry(root )
entryWord.place( x = 150 , y = 20 , width = 225 , height = 25)

# create a label to display result
lblResult = Label(root , text = "result .......")
lblResult.place( x = 150 , y = 60)

# Create a button to perform action
btnAction = Button(root , text = "Validate" , command = action)
btnAction.place( x = 150 , y = 100 , width = 225 , height = 30 )

root.mainloop()
'''
'''
Ex 3

Write a Python GUI program to create a ScrolledText widgets using tkinter module.
'''
import tkinter as tk
import tkinter.scrolledtext as tkst
from tkinter import *

parent = tk.Tk()
parent.title("Scrolledtext")
parent.geometry('350x200')

txt = tkst.ScrolledText(parent)
txt.grid(column=0, row=0)
txt.pack(fill = BOTH, expand = True)
parent.mainloop()