import tkinter


# Creation of the game Window
window = tkinter.Tk()
window.title("The Hangman")
window.geometry("300x500")
window.resizable()

# Image display
image = tkinter.PhotoImage(file="logo.png")
panel = tkinter.Label(window, image=image)
panel.pack()
window.mainloop()
