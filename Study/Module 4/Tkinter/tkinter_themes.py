'''
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

def create_widgets():
    label = ttk.Label(root, text="Hello, Tkinter!", font=("Helvetica", 20))
    label.pack(pady=20)

root = ThemedTk(theme="equilux")  # Choose a theme from "breeze", "adapta", "equilux", "arc", etc.
root.title("Themed Tkinter Example")

create_widgets()

root.mainloop()


import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle

def create_widgets():
    style = ThemedStyle(root)
    style.configure("Custom.TButton", font=("Roboto", 14), foreground="red")
    
    button = ttk.Button(root, text="Click Me!", style="Custom.TButton")
    button.pack(pady=20)

root = tk.Tk()
root.title("Custom Themed Tkinter Example")

create_widgets()

root.mainloop()
'''
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

def change_theme(theme_name):
    root.set_theme(theme_name)

root = ThemedTk(theme="breeze")
root.title("Dynamic Theme Change")

theme_list = ["breeze", "equilux", "arc", "clearlooks"]
for theme in theme_list:
    ttk.Button(root, text=theme.capitalize(), command=lambda t=theme: change_theme(t)).pack()

root.mainloop()


