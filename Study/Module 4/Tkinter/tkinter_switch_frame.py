import tkinter as tk

def show_frame1():
    frame2.pack_forget()  # Hide Frame 2
    frame1.pack()         # Show Frame 1

def show_frame2():
    frame1.pack_forget()  # Hide Frame 1
    frame2.pack()         # Show Frame 2



def create_frame1():
    frame1 = tk.Frame(root, borderwidth=2, relief="groove")
    label1 = tk.Label(frame1, text="This is Frame 1")
    button1 = tk.Button(frame1, text="Switch to Frame 2", command=show_frame2)
    label1.pack()
    button1.pack()
    return frame1

def create_frame2():
    frame2 = tk.Frame(root, borderwidth=2, relief="ridge")
    label2 = tk.Label(frame2, text="This is Frame 2")
    button2 = tk.Button(frame2, text="Switch to Frame 1", command=show_frame1)
    label2.pack()
    button2.pack()
    return frame2

root = tk.Tk()
root.title("Switching Frames")

frame1 = create_frame1()
frame2 = create_frame2()

frame1.pack()  # Show Frame 1 initially
root.mainloop()