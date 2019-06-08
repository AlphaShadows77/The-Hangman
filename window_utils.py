import tkinter as tk


def clear_window(wd):
	for widget in wd.winfo_children():
		widget.destroy()
