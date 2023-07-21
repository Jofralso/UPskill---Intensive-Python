'''
# Import all files from
# tkinter and overwrite
# all the tkinter files
# by tkinter.ttk
from tkinter import *
from tkinter.ttk import *

# creates tkinter window or root window
root = Tk()
root.geometry('200x100')

# function to be called when mouse enters in a frame
def enter(event):
	print('Mouse enters at = % d, y = % d'%(event.x, event.y))

# function to be called when mouse exits the frame
def exit_(event):
	print('mouse exits at x = % d, y = % d'%(event.x, event.y))

# frame with fixed geometry
frame1 = Frame(root, height = 100, width = 200)

# these lines are showing the
# working of bind function
# it is universal widget method
frame1.bind('<Enter>', enter)
frame1.bind('<Leave>', exit_)

frame1.pack()

mainloop()




# Import all files from
# tkinter and overwrite
# all the tkinter files
# by tkinter.ttk
from tkinter import *
from tkinter.ttk import *

# creates tkinter window or root window
root = Tk()
root.geometry('200x100')

# function to be called when button-2 of mouse is pressed
def pressed2(event):
	print('Button-2 pressed at x = % d, y = % d'%(event.x, event.y))

# function to be called when button-3 of mouse is pressed
def pressed3(event):
	print('Button-3 pressed at x = % d, y = % d'%(event.x, event.y))

## function to be called when button-1 is double clicked
def double_click(event):
	print('Double clicked at x = % d, y = % d'%(event.x, event.y))

frame1 = Frame(root, height = 100, width = 200)

# these lines are binding mouse
# buttons with the Frame widget
frame1.bind('<Button-2>', pressed2)
frame1.bind('<Button-3>', pressed3)
frame1.bind('<Double 1>', double_click)

frame1.pack()

mainloop()'''


# Import all files from
# tkinter and overwrite
# all the tkinter files
# by tkinter.ttk
from tkinter import *
from tkinter.ttk import *

# function to be called when
# keyboard buttons are pressed
def key_press(event):
	key = event.char
	print(key, 'is pressed')

# creates tkinter window or root window
root = Tk()
root.geometry('200x100')

# here we are binding keyboard
# with the main window
root.bind('<Key>', key_press)

mainloop()
