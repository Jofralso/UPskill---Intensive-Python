import tkinter as tk

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Your Application Title")
        self.create_frames()


    def create_frames(self):
        self.frame1 = Frame1(self, bg="red")
        self.frame2 = Frame2(self, bg="blue")
        self.frame3 = Frame3(self, bg="green")

        self.frame1.grid(row=0, column=0, padx=10, pady=10)
        self.frame2.grid(row=0, column=1, padx=10, pady=10)
        self.frame3.grid(row=1, column=0, columnspan=2, padx=10, pady=10)


class Frame1(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.create_widgets()

    def create_widgets(self):
        label1 = tk.Label(self, text="Frame 1", fg="white", bg="red")
        label1.pack(padx=10, pady=10)

class Frame2(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.create_widgets()

    def create_widgets(self):
        button1 = tk.Button(self, text="Click Me!", command=self.some_function)
        button1.pack(padx=10, pady=10)

    def some_function(self):
        # Your code here
        pass

class Frame3(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.create_widgets()

    def create_widgets(self):
        entry1 = tk.Entry(self)
        entry1.pack(padx=10, pady=10)

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
