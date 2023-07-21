'''
# Importing tkinter module
from tkinter import * 


# creating Tk window
master = Tk()

# creating a Frame which can expand according
# to the size of the window
pane = Frame(master)
pane.pack(fill = BOTH, expand = True)

# button widgets which can also expand and fill
# in the parent widget entirely
# Button 1
b1 = Button(pane, text = "Click me !")
b1.pack(fill = BOTH, expand = True)

# Button 2
b2 = Button(pane, text = "Click me too")
b2.pack(fill = BOTH, expand = True)

# Execute Tkinter
master.mainloop()



# Importing tkinter module
from tkinter import *
# from tkinter.ttk import *

# creating Tk window
master = Tk()

# creating a Fra, e which can expand according
# to the size of the window
pane = Frame(master)
pane.pack(fill = BOTH, expand = True)

# button widgets which can also expand and fill
# in the parent widget entirely
# Button 1
b1 = Button(pane, text = "Click me !",
			background = "red", fg = "white")
b1.pack(side = TOP, expand = True, fill = BOTH)

# Button 2
b2 = Button(pane, text = "Click me too",
			background = "blue", fg = "white")
b2.pack(side = TOP, expand = True, fill = BOTH)

# Button 3
b3 = Button(pane, text = "I'm also button",
			background = "green", fg = "white")
b3.pack(side = TOP, expand = True, fill = BOTH)

# Execute Tkinter
master.mainloop()
'''


# Importing tkinter module
from tkinter import *
# from tkinter.ttk import *

# creating Tk window
master = Tk()

# creating a Fra, e which can expand according
# to the size of the window
pane = Frame(master)
pane.pack(fill = BOTH, expand = True)

# button widgets which can also expand and fill
# in the parent widget entirely
# Button 1
b1 = Button(pane, text = "Click me !",
			background = '#0bbbbb', fg = "white")
b1.pack(side = RIGHT, expand = True, fill = BOTH)

# Button 2
b2 = Button(pane, text = "Click me too",
			background = "blue", fg = "white")
b2.pack(side = RIGHT, expand = True, fill = BOTH)

# Button 3
b3 = Button(pane, text = "I'm also button",
			background = "green", fg = "white")
b3.pack(side = RIGHT, expand = True, fill = BOTH)

# Execute Tkinter
master.mainloop()

