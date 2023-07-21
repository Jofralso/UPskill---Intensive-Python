import tkinter as tk 
from tkinter import ttk
from tkinter.messagebox import showinfo

class MainFrame(ttk.Frame): 
    def __init__(self, container):
        super().__init__(container)
        
        options = {'padx' : 5, 'pady': 5}
        
        #Label
        self.label = ttk.Label(self, text='Olá!')
        self.label.pack(**options)

        #BUTTON
        self.button = ttk.Button(self, text='Clica-me!')
        self.button['command'] = self.button_clicked
        self.button.pack(**options)
        
        # mostrar frame no container
        self.pack(**options)
        
    def button_clicked(self):
        showinfo(title='INFO', message='Adeus!')
        
class App(tk.Tk):
    def __init__(self,):
        super().__init__()
        
        self.title ('Janelinha')
        self.geometry('300x100')
        
        
if __name__ == '__main__':
    app = App()
    frame = MainFrame(app)
    app.mainloop()