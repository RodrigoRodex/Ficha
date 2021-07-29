import tkinter as tk

root = tk.Tk()

margin = 0.23

entry = tk.Entry(root)

entry.pack()


def profit_calculator():
    profit = margin + int(entry.get())
    print(profit)


button_calc = tk.Button(root, text="Calculate", command=profit_calculator)
button_calc.pack()

root.mainloop()
"""
Label(window, text="Carisma:").grid(row=1, sticky=W)
Entry(window).grid(row=1, column=1)

Label(window, text="Constituição:").grid(row=2, sticky=W)
Entry(window).grid(row=2, column=1)

Label(window, text="Inteligência:").grid(row=3, sticky=W)
Entry(window).grid(row=3, column=1)

Label(window, text="Destreza:").grid(row=4, sticky=W)
Entry(window).grid(row=4, column=1)

Label(window, text="Sabedoria:").grid(row=5, sticky=W)
Entry(window).grid(row=5, column=1)

"""
