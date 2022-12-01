import tkinter as tk
from random import randint

# Create the window 
window = tk.Tk(className="Paint | By ExclMark")

# Create the canvas
canvas = tk.Canvas(window, width=500, height=500)
canvas.pack()

# Draw a line from cursor to center when mouse is clicked
def draw_line(cursor):
    # Generate random color
    color = "#%06x" % randint(0, 0xFFFFFF)

    # Draw line
    canvas.create_line(cursor.x, cursor.y, 250, 250, fill=color)

# Bind the mouse click and hold to the draw_line function
canvas.bind("<B1-Motion>", draw_line)

# Start the window
window.mainloop()