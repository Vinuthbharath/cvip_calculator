import tkinter as tk
from tkinter import font


def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))


def clear():
    entry.delete(0, tk.END)


def calculate():
    current = entry.get()
    try:
        result = eval(current)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")



root = tk.Tk()
root.title("Calculator")


entry_font = font.Font(family="Arial", size=30)
entry = tk.Entry(root, font=entry_font, width=25, borderwidth=10)
entry.grid(row=0, column=0, columnspan=7, padx=20, pady=20)


button_font = font.Font(family="Arial", size=30)
buttons = [
    'C',
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',

]


row_num = 1
col_num = 0

for button in buttons:
    if button == '=':
        tk.Button(root, text=button, padx=20, pady=20, font=button_font, command=calculate).grid(row=row_num,
                                                                                                 column=col_num)
    elif button == 'C':
        tk.Button(root, text=button, padx=20, pady=20, font=button_font, command=clear).grid(row=row_num,
                                                                                             column=col_num)
    else:
        tk.Button(root, text=button, padx=20, pady=20, font=button_font, command=lambda b=button: button_click(b)).grid(
            row=row_num, column=col_num)

    col_num += 1
    if col_num > 3:
        col_num = 0
        row_num += 1


root.geometry("400x500")


root.mainloop()