import tkinter as tk
r = tk.Tk()
r.title('Transfer E-Wallet')
r.mainloop()

from tkinter import*
master = Tk()
w = Canvas (master, width=50 , height=70)
w.pack()
canvas_height=200
canvas_width=200
y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y)
mainloop()