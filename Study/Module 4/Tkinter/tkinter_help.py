import tkinter as tk

# Function to be called on button click
def some_function():
    # Your code here
    pass

# Create the main window
root = tk.Tk()
root.title("Your Application Title")


# Create different frames
frame1 = tk.Frame(root, bg="red")
frame2 = tk.Frame(root, bg="blue")
frame3 = tk.Frame(root, bg="green")

# Organize frames with grid layout
frame1.grid(row=0, column=0, padx=10, pady=10)
frame2.grid(row=0, column=1, padx=10, pady=10)
frame3.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Add widgets to the frames
label1 = tk.Label(frame1, text="Frame 1", fg="white", bg="red")
label1.pack(padx=10, pady=10)

button1 = tk.Button(frame2, text="Click Me!", command=some_function,fg="white", bg="blue" )
button1.pack(padx=10, pady=10)

entry1 = tk.Entry(frame3)
entry1.pack(padx=10, pady=10)


# Run the main event loop
root.mainloop()