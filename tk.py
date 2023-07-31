
import datetime

import tkinter as tk


from tkinter import ttk

from tkinter.messagebox import showinfo




class App(tk.Tk):

    def __init__(self):

        super().__init__()




        self.title('Media Library')

        self.geometry('500x200')

        self.resizable(0, 0)




        self.configure(bg='DarkSeaGreen4')





class Mainframe(tk.Frame): #isto é uma frame dentro da janela

    def __init__(self, container):

        super().__init__(container)
        
    
        self.configure(bg='DarkSeaGreen4')


        self.label = tk.Label(self, text = 'Welcome to Your Media Library!', font = ('American Typewriter', 20, 'bold'), background = 'DarkSeaGreen4', foreground= 'papaya whip', height=2)

        self.label.pack(side='top', pady= 30) #recebe toda a info de options como parametro

        

        self.button = tk.Button(self, text = 'Start', bg = 'papaya whip', fg = 'DarkSeaGreen4')

        self.button['command'] = self.button_clicked

        self.button.pack(side='bottom', padx= 30)

    

    def button_clicked(self):

        # Clear the Mainframe by destroying all widgets inside it

        for widget in self.winfo_children():

            widget.destroy()




app = App()


frame = Mainframe(app) #esta frame esta dentro da nossa janela

frame.pack(padx= 5, pady= 5)

app.mainloop()