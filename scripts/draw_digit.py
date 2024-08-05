import tkinter as tk
from PIL import Image, ImageDraw
import numpy as np

class DrawDigitApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Draw a Digit")
        
        self.canvas = tk.Canvas(root, width=200, height=200, bg='white')
        self.canvas.pack()
        
        self.image = Image.new("L", (200, 200), 'white')
        self.draw = ImageDraw.Draw(self.image)
        
        self.canvas.bind("<B1-Motion>", self.paint)
        
        self.save_button = tk.Button(root, text="Save and Close", command=self.save_and_close)
        self.save_button.pack()

        self.clear_button = tk.Button(root, text="Clear", command=self.clear)
        self.clear_button.pack()

    def paint(self, event):
        x1, y1 = (event.x - 5), (event.y - 5)
        x2, y2 = (event.x + 5), (event.y + 5)
        self.canvas.create_oval(x1, y1, x2, y2, fill='black', width=5)
        self.draw.line([x1, y1, x2, y2], fill='black', width=5)

    def save_and_close(self):
        self.image.save("data/drawn_digit.png")
        print("Digit saved as data/drawn_digit.png")
        self.root.destroy()  # Close the window

    def clear(self):
        self.canvas.delete("all")
        self.image = Image.new("L", (200, 200), 'white')
        self.draw = ImageDraw.Draw(self.image)

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawDigitApp(root)
    root.mainloop()
