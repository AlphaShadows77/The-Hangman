import tkinter as tk

import window_utils as w_utils


# Properties
wd = None
wd_size = (wd.winfo_reqwidth(), wd.winfo_reqheight())
hangman_size = (wd_size[0] * 2/5,
				wd_size[1] * 2/5)
word_size = (wd_size[0] * 1/14,
			 wd_size[1] * 2/5)
word_field_size = (wd_size[0] * 1/14,
				   wd_size[1] * 2/5)

_player_guess = StringVar()

def get_player_guess():
	return str(_player_guess.get())


def init_game(wd):
	wd = wd
	w_utils.clear_window(wd)
	create_elements()

def _create_elements():
	hangman = Canvas(wd, bg='white', highlightthickness=0,
					 height=hangman_size[0], width=hangman_size[1])

	word = Label(wd, bg='white', height=word_size[0], width=word_size[1])

	word_field = Entry(wd, bg='white', exportselection=0, highlightthickness=0,
					   justify=center, textvariable=_player_guess,
					   validate='key', validatecommand='on_key_press')
