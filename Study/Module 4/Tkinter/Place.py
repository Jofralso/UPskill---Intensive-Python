'''
# Importing tkinter module
from tkinter import * 
from tkinter.ttk import *

# creating Tk window
master = Tk()

# setting geometry of tk window
master.geometry("200x200")

# button widget
b1 = Button(master, text = "Click me !")
b1.place(relx = 1, x =-10, y = 10, anchor = NE)

# label widget
l = Label(master, text = "I'm a Label")
l.place(anchor = NW)

# button widget
b2 = Button(master, text = "GFG")
b2.place(relx = 0.5, rely = 0.5, anchor = CENTER)

# infinite loop which is required to
# run tkinter program infinitely
# until an interrupt occurs
mainloop()
''' 
# Importing tkinter module
from tkinter import * 
from tkinter.ttk import *

# creating Tk window
master = Tk()

# setting geometry of tk window
master.geometry("200x200")

# button widget
b2 = Button(master, text = "GFG")
b2.pack(fill = X, expand = True, ipady =10)

# button widget
b1 = Button(master, text = "Click me !")

# This is where b1 is placed inside b2 with in_ option
b1.place(in_= b2, relx = 0.5, rely = 0.5, anchor = CENTER)

# label widget
l = Label(master, text = "I'm a Label")
l.place(anchor = NW)

# infinite loop which is required to
# run tkinter program infinitely
# until an interrupt occurs
mainloop()