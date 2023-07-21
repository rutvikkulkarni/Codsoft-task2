import tkinter as tk


def on_click(event):
    current_text = entry.get()
    button_text = event.widget.cget("text")

    if button_text == "=":
        try:
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)


# Create the main application window
root = tk.Tk()
root.title("Calculator")

# Entry widget to display input and output
entry = tk.Entry(root, font=("Arial", 18), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button styles
button_style = {
    "font": ("Arial", 18),
    "padx": 20,
    "pady": 20,
    "width": 3,
    "height": 1,
    "borderwidth": 1,
    "relief": tk.RAISED,
    "bg": "grey",  # Background color
    "fg": "#000000"  # Foreground (text) color
}

# Buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0)
]

for (button_text, row, column) in buttons:
    btn = tk.Button(root, text=button_text, **button_style)
    btn.grid(row=row, column=column, padx=5, pady=5)
    btn.bind("<Button-1>", on_click)

# Start the main event loop
root.mainloop()
