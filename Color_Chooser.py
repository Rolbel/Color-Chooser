"""This is an color chooser application using Tkinter"""
from tkinter import *
from tkinter import colorchooser

root = Tk()
root.title ("Color Chooser")
root.geometry("300x300")

""" Open the color chooser dialog and pass the hex data to the entry box"""
def choose_color():
    # Opens the color chooser dialog
    color_code = colorchooser.askcolor(title = "Choose color")

    if color_code[1]:
        # Clear any existing text
        color_entry.delete(0, END)
        # Insert the selected color code
        color_entry.insert(0, color_code[1])

"""Handles the logic for the copy button"""
def copy_color():
    # Clears the last copy data
    root.clipboard_clear()
    # Copies the data on the entry box
    root.clipboard_append(color_entry.get())
    # Required for clipboard changes to take effect
    root.update()

select_color_button = Button(root, text = "Select Color", command = choose_color)
select_color_button.pack(pady=70)

color_entry = Entry(root, font = 16, width = 28)
color_entry.pack(pady=20)

copy_button = Button(root, text = "Copy", command = copy_color)
copy_button.pack(pady=10)

root.mainloop()
