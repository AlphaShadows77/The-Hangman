from tkinter import *
from PIL import ImageTk
from PIL import Image


# Creation of the game Window
wd = Tk()
wd.title("The Hangman")
height = 300
width = 200
wd.configure(height=height, width=width)
wd.resizable(0, 0)

# Title print
title = Label(wd, text="The Hangman", font=(None, -17, "bold"))
title.place(anchor=N, x=width/2, y=15)

# Image load and resize
img_raw = Image.open("logo.jpg")
img_height = 150
img_width = 150
img_raw = img_raw.resize((img_height, img_width))

# Image conversion
image = ImageTk.PhotoImage(img_raw)

# Image show
can = Canvas(wd, height=img_height, width=img_width)
can.create_image(0, 0, image=image, anchor=NW)
can.place(anchor=N, x=width/2, y=50)

# Play button
play = Button(wd, text="Play !")
play.place(anchor=S, x=width/2, y=height - 30)

wd.mainloop()
