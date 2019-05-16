from tkinter import *
from PIL import ImageTk
from PIL import Image


# Creation of the game Window
wd = Tk()
wd.title("The Hangman")
height = 300
width = 200
wd.configure(height=height, width=width)
wd.resizable()

# Image load and resize
img_raw = Image.open("logo.jpg")
img_raw = img_raw.resize((150, 150))

# Image conversion
image = ImageTk.PhotoImage(img_raw)

# Image show
can = Canvas(wd, height=height, width=width)
can.create_image(width / 2, 50, image=image, anchor=N)
can.pack()

# Play button
play = Button(wd, text="Play !")
play.pack()
play.place(x=width/2, y=height-30, anchor=S)

wd.mainloop()
