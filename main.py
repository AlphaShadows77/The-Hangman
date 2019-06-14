import tkinter as tk
from PIL import ImageTk
from PIL import Image

import game


# Creation of the game Window
wd = tk.Tk()
wd.title("The Hangman")
wd.configure(bg="white")
height = 300
width = 200
wd.configure(height=height, width=width)
wd.resizable(0, 0)

# Title print
title = tk.Label(wd, bg="white", font=(None, -17, "bold"), text="The Hangman")
title.place(anchor='n', x=width/2, y=15)

# Image load and resize
img_raw = Image.open("logo.jpg")
img_height = 150
img_width = 150
img_raw = img_raw.resize((img_height, img_width))

# Image conversion
image = ImageTk.PhotoImage(img_raw)

# Image show
can = tk.Canvas(wd, bg="white", height=img_height, highlightthickness=0, width=img_width)
can.create_image(0, 0, image=image, anchor='nw')
can.place(anchor='n', x=width/2, y=50)

# Play button
play = tk.Button(wd, text="Play !", command=lambda : game.init_game(wd))
play.place(anchor='s', x=width/2, y=height - 30)

wd.mainloop()
