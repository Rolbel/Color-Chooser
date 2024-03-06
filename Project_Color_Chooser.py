import tkinter as tk
from tkinter import colorchooser

root = tk.Tk()
root.title("Color Chooser")
root.geometry("450x350")

n = 10  # The number of buttons
i = 4  # row
j = 0  # column
buttons = []
color_history = []

def update_color_history(color):
    if color not in color_history:
        color_history.append(color)
        if len(color_history) > 10:
            color_history.pop(0)
        update_buttons_color_history()

def update_buttons_color_history():
    for idx, color in enumerate(color_history):
        buttons[idx].config(bg=color, state=tk.NORMAL)

def copy_color():
    color_entry_text = color_entry.get()
    if color_entry_text:
        root.clipboard_clear()
        root.clipboard_append(color_entry_text)
        root.update()

def collect_color(k):
    color_code = color_history[k]
    color_entry.delete(0, tk.END)
    color_entry.insert(0, color_code)

def open_color_chooser():
    color_code = colorchooser.askcolor()
    if color_code and color_code[1]:
        update_color_history(color_code[1])
        color_entry.delete(0, tk.END)
        color_entry.insert(0, color_code[1])

color_entry = tk.Entry(root, width=30)
color_entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

copy_button = tk.Button(root, text="Copy", font=("Helvetica", 16),
                        command=copy_color, width=10)
copy_button.grid(row=1, column=0, columnspan=5, pady=5)

color_selector_button = tk.Button(root, text="Select a color", font=("Helvetica", 16),
                                   command=open_color_chooser, width=10)
color_selector_button.grid(row=2, column=0, columnspan=5, pady=5)

history_label = tk.Label(root, text="Color History:")
history_label.grid(row=3, column=0, columnspan=5, pady=5)

for k in range(n):
    e = tk.Button(root, text=k, height=2, width=10,
                  command=lambda a=k: collect_color(a), state=tk.DISABLED)
    e.grid(row=i, column=j, padx=1, pady=1)
    buttons.append(e)
    j = j + 1
    if (j % 5 == 0):
        i = i + 1
        j = 0

root.mainloop()
