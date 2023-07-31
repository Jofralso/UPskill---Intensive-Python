import tkinter as tk
from tkinter import messagebox

def show_selected_language():
    language = selected_language.get()
    messagebox.showinfo("Favorite Language", f"Your favorite programming language is: {language}")

def show_hobbies():
    hobbies = hobbies_listbox.get(0, tk.END)
    messagebox.showinfo("Hobbies", f"Your hobbies are:\n{', '.join(hobbies)}")

root = tk.Tk()
root.title("Tkinter Widget Examples")

# Labels
label_name = tk.Label(root, text="Enter your name:")
label_gender = tk.Label(root, text="Select your gender:")
label_language = tk.Label(root, text="Select your favorite programming language:")
label_hobbies = tk.Label(root, text="Select your hobbies:")

# Entry Fields
entry_name = tk.Entry(root)

# Radio Buttons
gender_var = tk.StringVar()
gender_var.set("male")
radio_male = tk.Radiobutton(root, text="Male", variable=gender_var, value="male")
radio_female = tk.Radiobutton(root, text="Female", variable=gender_var, value="female")

# Check Buttons
hobby_var1 = tk.IntVar()
hobby_var2 = tk.IntVar()
hobby_var3 = tk.IntVar()
check_reading = tk.Checkbutton(root, text="Reading", variable=hobby_var1)
check_coding = tk.Checkbutton(root, text="Coding", variable=hobby_var2)
check_gaming = tk.Checkbutton(root, text="Gaming", variable=hobby_var3)

# Combo Box
languages = ["Python", "Java", "JavaScript", "C++", "C#"]
selected_language = tk.StringVar()
combo_languages = tk.OptionMenu(root, selected_language, *languages)

# List Box
hobbies_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
hobbies = ["Painting", "Cooking", "Traveling", "Hiking", "Photography"]
for hobby in hobbies:
    hobbies_listbox.insert(tk.END, hobby)

# Buttons
language_button = tk.Button(root, text="Show Favorite Language", command=show_selected_language)
hobbies_button = tk.Button(root, text="Show Hobbies", command=show_hobbies)

# Grid layout
label_name.grid(row=0, column=0, padx=10, pady=5)
entry_name.grid(row=0, column=1, padx=10, pady=5)

label_gender.grid(row=1, column=0, padx=10, pady=5)
radio_male.grid(row=1, column=1, padx=10, pady=5)
radio_female.grid(row=1, column=2, padx=10, pady=5)

label_language.grid(row=2, column=0, padx=10, pady=5)
combo_languages.grid(row=2, column=1, padx=10, pady=5)
language_button.grid(row=2, column=2, padx=10, pady=5)

label_hobbies.grid(row=3, column=0, padx=10, pady=5)
check_reading.grid(row=3, column=1, padx=10, pady=5)
check_coding.grid(row=3, column=2, padx=10, pady=5)
check_gaming.grid(row=3, column=3, padx=10, pady=5)
hobbies_listbox.grid(row=4, column=1, columnspan=3, padx=10, pady=5)
hobbies_button.grid(row=4, column=0, padx=10, pady=5)

root.mainloop()
