import tkinter as tk 
from tkinter import ttk
from tkinter.messagebox import showerror

class TemperatureConverter:
    @staticmethod
    def fahrenheit_to_celsius(f):
        return (f - 32) * 5 / 9
    
class ConverterFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        
        #opções de campo
        options = {'padx': 5, 'pady' : 5}
        
        #etiqueta de temperatura (label)
        self.temperature_label = ttk.Label(self, text='Farenheit')
        self.temperature_label.grid(column=0, row=0, sticky=tk.W, **options)
        
        #Entry de temperatura
        self.temperature = tk.StringVar()
        self.temperature_entry = ttk.Entry(self, textvariable=self.temperature)
        self.temperature_entry.grid(column=1, row=0, **options)
        self.temperature_entry.focus()
        
        self.convert_button = ttk.Button(self)
        self.convert_button['text'] = 'Convert'
        self.convert_button['command'] = self.convert
        self.convert_button.grid(column=2, row=0, sticky=tk.W, **options)
        
        #Result label
        self.result_label = ttk.Label(self)
        self.result_label.grid(row=1, columnspan=3, **options)
        
        self.grid(padx=10, pady=10, sticky=tk.NSEW)
        
    def convert(self):
        '''Handle button click event'''
        
        try: 
            f = float(self.temperature.get())
            c = TemperatureConverter.fahrenheit_to_celsius(f)
            result =f'{f} Fahrenheit = {c:.2f} Celsius'
            self.result_label.config(text=result)
        except ValueError as error:
            showerror(title='Error', message=error)
            

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title('Conversor de Temperatura')
        self.geometry('300x70')
        self.resizable(False, False)
        
        
if __name__ =="__main__":
    app = App()
    ConverterFrame(app)
    app.mainloop()
