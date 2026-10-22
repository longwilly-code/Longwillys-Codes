import tkinter as tk
from tkinter import Canvas


#--GUI--
root = tk.Tk()
root.geometry('800x600')
root.title('Canvas Demo')


canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

canvas.create_text(175, 20, text = "circle", font = ("Arial", 30))
circle = canvas.create_oval(200, 100, 100, 200, width = 3) #size






root.mainloop()