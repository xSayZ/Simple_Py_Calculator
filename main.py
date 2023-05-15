import tkinter as tk

history = []  # List to store the history of calculations
current_index = -1  # Current index in the history list

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
        update_history(entry.get())  # Update the history with the calculation
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def update_history(calculation):
    global history, current_index
    history = history[:current_index + 1]  # Discard any redo history
    history.append(calculation)
    current_index += 1
    history_text.config(state=tk.NORMAL)  # Enable editing of the text widget
    history_text.insert(tk.END, calculation + "\n")
    history_text.see(tk.END)  # Scroll to the end of the text
    history_text.config(state=tk.DISABLED)  # Disable editing of the text widget

def history_click(event):
    widget = event.widget
    index = widget.index(f"@{event.x},{event.y}")
    line_number = int(widget.index(f"{index}.0 linestart").split('.')[0])
    selected_calculation = history[line_number - 1]
    entry.delete(0, tk.END)
    entry.insert(tk.END, selected_calculation.strip())

def undo():
    global current_index
    if current_index > 0:
        current_index -= 1
        entry.delete(0, tk.END)
        entry.insert(tk.END, history[current_index])

def redo():
    global current_index
    if current_index < len(history) - 1:
        current_index += 1
        entry.delete(0, tk.END)
        entry.insert(tk.END, history[current_index])

def on_keypress(event):
    if event.char.isdigit():
        button_click(event.char)
    elif event.char == "+":
        button_click("+")
    elif event.char == "-":
        button_click("-")

# Create the main window
window = tk.Tk()
window.title("Calculator")
window.configure(bg="#444444")  # Set background color to dark gray

# Create the entry widget
entry = tk.Entry(window, width=30, borderwidth=5, bg="#666666", fg="white", font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define button colors
button_bg = "#333333"
button_fg = "white"

# Create the number buttons in the desired order
for i in range(9):
    button = tk.Button(window, text=str(9 - i), padx=40, pady=20, command=lambda num=(9 - i): button_click(num),
                       bg=button_bg, fg=button_fg, font=("Arial", 12, "bold"))
    button.grid(row=(i // 3) + 3, column=i % 3)

# Create the other buttons
button_0 = tk.Button(window, text="0", padx=40, pady=20, command=lambda: button_click(0),
                     bg=button_bg, fg=button_fg, font=("Arial", 12, "bold"))
button_clear = tk.Button(window, text="C", padx=40, pady=20, command=button_clear,
                         bg=button_bg, fg=button_fg, font=("Arial", 12, "bold"))
button_equal = tk.Button(window, text="=", padx=40, pady=20, command=button_equal,
                         bg=button_bg, fg=button_fg, font=("Arial", 12, "bold"))
button_add = tk.Button(window, text="+", padx=40, pady=20, command=lambda: button_click("+"),
                       bg=button_bg, fg=button_fg, font=("Arial", 12, "bold"))
button_subtract = tk.Button(window, text="-", padx=40, pady=20, command=lambda: button_click("-"),
                            bg=button_bg, fg=button_fg, font=("Arial", 12, "bold"))
button_multiply = tk.Button(window, text="*", padx=40, pady=20, command=lambda: button_click("*"),
                            bg=button_bg, fg=button_fg, font=("Arial", 12, "bold"))
button_divide = tk.Button(window, text="/", padx=40, pady=20, command=lambda: button_click("/"),
                          bg=button_bg, fg=button_fg, font=("Arial", 12, "bold"))

button_0.grid(row=6, column=1)
button_clear.grid(row=6, column=0)
button_equal.grid(row=6, column=2)
button_add.grid(row=3, column=3)
button_subtract.grid(row=4, column=3)
button_multiply.grid(row=5, column=3)
button_divide.grid(row=6, column=3)

# Create the history log window
history_text = tk.Text(window, width=20, height=10, bg="#666666", fg="white", font=("Arial", 12, "bold"), state=tk.DISABLED)
history_text.grid(row=2, column=4, rowspan=4, padx=10, pady=10)

# Create the undo and redo buttons
button_undo = tk.Button(window, text="Undo", padx=20, pady=10, command=undo,
                        bg=button_bg, fg=button_fg, font=("Arial", 12, "bold"))
button_undo.grid(row=6, column=4, sticky="ew", padx=10, pady=5)

button_redo = tk.Button(window, text="Redo", padx=20, pady=10, command=redo,
                        bg=button_bg, fg=button_fg, font=("Arial", 12, "bold"))
button_redo.grid(row=7, column=4, sticky="ew", padx=10, pady=5)

# Start the main event loop
window.mainloop()
