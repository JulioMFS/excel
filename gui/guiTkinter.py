import tkinter as tk
window = tk.Tk()
greeting = tk.Label(text="Hello, Tkinter")
greeting.pack()

label = tk.Label(
    text = "Hello, Tkinter",
    foreground="white",
    background="black"
)
label.pack()
label1 = tk.Label(text="Hello, ..Tkinter", background="#34A2FE")
label1.pack()

button=tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)
button.pack()
entry=tk.Entry(fg="blue", bg="yellow", width=50)
entry.pack()
window.mainloop()