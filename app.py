import tkinter as tk
import csv

expenses = []

# expense add
def add():
    name = name_entry.get()
    amount = amount_entry.get()

    if name == "" or amount == "":
        total_label.config(text="enter item name and amount")
        return

    amount = float(amount)
    expenses.append((name, amount))

    listbox.insert(tk.END, name + " - $" + str(amount))

    name_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)

# calculate expense total
def total():
    t = 0
    for e in expenses:
        t += e[1]

    total_label.config(text="Total: $" + str(t))

# file save to computer
def save():
    file = open("expenses.csv", "w", newline="")
    writer = csv.writer(file)

    for e in expenses:
        writer.writerow(e)

    file.close()
    total_label.config(text="Saved to file")

# window
root = tk.Tk()
root.title("Expense Tracker App")

# user inputs
tk.Label(root, text="Item Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Amount").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

# buttons
tk.Button(root, text="Add Item", command=add).pack()
tk.Button(root, text="Calculate Total", command=total).pack()
tk.Button(root, text="Save File", command=save).pack()

# list
listbox = tk.Listbox(root)
listbox.pack()

# total label
total_label = tk.Label(root, text="Total: $0")
total_label.pack()

root.mainloop()