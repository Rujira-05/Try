
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import random

class Heart:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.text = canvas.create_text(x, y, text="❤️", font=("Arial", 20))
        self.speed = random.randint(1, 3)

    def move(self):
        self.canvas.move(self.text, 0, -self.speed)
        pos = self.canvas.coords(self.text)
        if pos[1] < -20:
            self.canvas.coords(self.text, random.randint(0, self.canvas.winfo_width()), self.canvas.winfo_height())

def choose_image():
    filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
    if filepath:
        img = Image.open(filepath)
        img = img.resize((400, 400))
        img = ImageTk.PhotoImage(img)
        panel.config(image=img)
        panel.image = img

def create_hearts():
    for _ in range(30):
        x = random.randint(0, canvas.winfo_width())
        y = random.randint(canvas.winfo_height()//2, canvas.winfo_height())
        hearts.append(Heart(canvas, x, y))

def animate():
    for heart in hearts:
        heart.move()
    root.after(50, animate)

root = tk.Tk()
root.title("โชว์รูปพร้อมหัวใจลอย ❤️")

canvas = tk.Canvas(root, width=500, height=600, bg="white")
canvas.pack()

btn = tk.Button(root, text="เลือกรูปภาพ", command=choose_image)
btn.pack(pady=10)

panel = tk.Label(canvas)
panel.place(relx=0.5, rely=0.5, anchor="center")

hearts = []
root.after(1000, create_hearts)
root.after(1000, animate)

root.mainloop()
