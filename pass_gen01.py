# Password Gen v 0.1
# First version of Password Gen.  Nicolás Táutiva ->   nicolastautiva at hotmail com

import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import scrolledtext
from tkinter import messagebox as msg 
import random


char = ('0123456789abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVXYZ-!#$%+*~&???/=')

def _quit():      # Function to close the program
	window.quit()
	window.destroy()
	exit()

def _msgBox1():
	msg.showwarning("Invalid number!", "Enter a valid number between 5 and 71")

def _msgBox2():
	msg.showwarning("Invalid number!", "Sorry, Can't generate a password this long!")
	
def _versionBox():
	msg.showinfo("Python message info Box", "Password Generator  Version 0.1 \n \n By Nicolás Táutiva")
	
def generate_password():

	password = ""
		
	try:
		if password_length.get() < 1:
			_msgBox1()
			
		elif password_length.get() > 71:
			_msgBox2()
			
		else:
			while len(password) < password_length.get():
				character = random.choice(char)
						
				# To avoid repeated characters in the final password
				if character in  password:
					continue
				else:
					password = password + character
			
		###### to be improved into a better look.  Maybe a new message box???  With this method is not possible for user to copy and paste.  
		###### Scrolltext is the solution??
		print(password)
		label_3 = ttk.Label(label_frame1, text = "your new password is:    " + password)
		label_3.grid(column = 0, row = 4, sticky = tk.W)
	
	except:
		_msgBox()
		
			
			
# Creating the GUI
window = tk.Tk()
window.title("PassGen 0.1")
window.geometry("380x300")
window.resizable(False, False)
window.wm_iconbitmap('passgen.ico')   # This icon sucks!!!  work on it!

label_frame1 = ttk.LabelFrame(window, text = "Welcome to Password Generator")
label_frame1.grid(column = 0, row = 1, padx = 20, pady = 20)


label_1 = ttk.Label(label_frame1, text = "How many characters would you like in your new password?")
label_1.grid(column = 0, row = 0, pady = 20)

label_2 = ttk.Label(label_frame1, text = "Minimum 5 and maximum 71 characters")
label_2.grid(column = 0, row = 1)


password_length = tk.IntVar()
password_length.set("9")   # I set an initial value!!
entry_1 = ttk.Entry(label_frame1, width = "5", textvariable = password_length)
entry_1.grid(column = 0, row = 2, pady = 20)
entry_1.focus()

button_1 = ttk.Button(label_frame1, text = "Generate Password!", command = generate_password)
button_1.grid(column = 0, row = 3, pady = 10)



# Creating the menu bar.  
menu_bar = Menu(window)
window.config(menu = menu_bar)

#creando el menu y agregando items
file_menu = Menu(menu_bar, tearoff = 0)  # tearoff para desaparecer un linea punteada sobre menu
menu_bar.add_cascade(label = "File", menu = file_menu)
file_menu.add_command(label = "Exit", command = _quit)

help_menu = Menu(menu_bar, tearoff = 0)
menu_bar.add_cascade(label = "Help", menu = help_menu)
help_menu.add_command(label = "About", command = _versionBox)



window.mainloop()