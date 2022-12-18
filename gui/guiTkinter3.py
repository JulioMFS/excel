import tkinter as tk

border_effects = {
    "flat1": tk.FLAT,
    "sunken2": tk.SUNKEN,
    "raised3": tk.RAISED,
    "groove4": tk.GROOVE,
    "ridge5": tk.RIDGE,
}

window = tk.Tk()

for relief_name, relief in border_effects.items():
    frame = tk.Frame(master=window, relief=relief, borderwidth=5)
    frame.pack(side=tk.LEFT)
    label = tk.Label(master=frame, text=relief_name)
    label.pack()

window.mainloop()