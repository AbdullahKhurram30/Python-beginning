import tkinter as tk
from tkinter import ttk

window = tk.Tk()

my_label = ttk.Label(window, text = "Hi, My name is Muhammad Abdullah! Nice to meet you")
my_label.grid(row = 1, column = 1)

quit_button = ttk.Button(window, text="Leave page")
quit_button.grid(row = 100, column = 100)
quit_button[ 'command' ] = window.destroy

window.mainloop()