# Password Gen v 1.0
# First operational version of Password Generator.
# Nicolás Táutiva ->   nicolastautiva {at} hotmail com

###################
####  TO FIX: #####
# 13. tell user that there is something copied on the clipboard...
#     How??  change button color?  pop up?
##################
##################


import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import scrolledtext
from tkinter import messagebox as msg
import random

version = "Version 1.0"


#Chars, numbers & symbols to use
LETTERS = ('abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVXYZ')
NUMBERS = ('0123456789')
SYMBOLS = ('@-!#$%+*~&¿?;:/=')     #Are they all accepted?  


def show_tips():
	"""Function to show the tips on a PDF file"""
	import os
	os.startfile('tips.pdf')

def _openGuide():
	"""Function to show the user guide on a PDF file"""
	import os
	os.startfile('guide.pdf')
	
def _msgBox(title = "Invalid entry!", message = "Enter a valid number  \
												between 8 and 500"):
	"""Function to show different errors and messageBox"""
	msg.showwarning(title, message)

def _versionBox():
	"""Function to show the 'about' pop up"""
	msg.showinfo("Python message info Box", "Password Generator {} \n \
				\nBy Nicolás Táutiva ".format(version)) 

def _quit(): 
	"""Function to close the main program cleanly"""
	gen_window.quit()
	gen_window.destroy()
	exit()

def _openGit():
	"""Small function to open my git web site"""
	import webbrowser
	url = 'www.github.com/NickATC'
	webbrowser.open(url, new=0, autoraise=True)

def _copyClipboard():
	"""Function to copy the password to the clipboard"""
	import pyperclip
	pyperclip.copy(scr_pass.get(1.0,"end"))

def generate_password():
	"""Function to analize user entries and generate the password"""
	scr_pass.delete(1.0,"end")
	password = []
	values_for_password = []
	
	try:
		if int(password_length.get()) < 8:
			_msgBox()
			
		elif int(password_length.get()) > 500:
			_msgBox(message = "Sorry, Can't generate a password this long!")
			
		else:
			#Dictionary to check and store user values.
			variable_values = {'chVarLetters' : chVarLetters.get(),
							'chVarNumbers' : chVarNumbers.get(),
							'chVarSymbols' : chVarSymbols.get()
							}
		
			#To check the user preferences.  
			#If checked, it'll be added to list values_for_password.	
			for key, value in variable_values.items():
				if value == 1:
					values_for_password.append(key)
				else:
					continue
	
			if not values_for_password:
				_msgBox(title = "Error!", message = "At least one option must \
													be checked!")

			else:
				#Dictionary to match the variable name from the buttons and 
				#the varibale value (LETTERS, NUMBERS or SYMBOLS)
				equivalent_values = { 'chVarLetters' : LETTERS,
										'chVarNumbers' : NUMBERS,
										'chVarSymbols' : SYMBOLS
									}
				
				if len(values_for_password) == 3:
					for i in range(round(int(password_length.get()) / 3)):
						item = values_for_password[0]
						character = random.choice(equivalent_values[item])
						password.append(character)

					for i in range(round(int(password_length.get()) / 3)):
						item = values_for_password[1]
						character = random.choice(equivalent_values[item])
						password.append(character)
								
					while len(password) < int(password_length.get()):
						item = values_for_password[2]
						character = random.choice(equivalent_values[item])
						password.append(character)
					
				elif len(values_for_password) == 2:
					for i in range(round(int(password_length.get()) / 2)):
						item = values_for_password[0]
						character = random.choice(equivalent_values[item])
						password.append(character)
					
					while len(password) < int(password_length.get()):
						item = values_for_password[1]
						character = random.choice(equivalent_values[item])
						password.append(character)
				
				else:
					for key, value in equivalent_values.items():
						if key in values_for_password:
							while len(password) < int(password_length.get()):
								character = random.choice(value)
								password.append(character)
						else:
							continue
																	
	except ValueError:
		_msgBox()
	
	random.shuffle(password) 			  # shuffle password.
	password = "".join(password) 		  # Turn password into a string
	scr_pass.insert(tk.INSERT, password)  # Insert password into scrolledtext
	

####################################################
####### Creating the GUI for the password_generator
####################################################			

gen_window = tk.Tk()
gen_window.title("Password Generator")
gen_window.geometry("450x630")
gen_window.resizable(False, False)
gen_window.wm_iconbitmap("lock.ico")


pass_gen_header = tk.PhotoImage(file = 'pass_gen_header.gif')
pass_gen_header_gif = tk.Label(gen_window, image = pass_gen_header)
pass_gen_header_gif.grid(column = 0, row = 0)


#############################################
####### Creating the Widgets
#############################################

advice_button = ttk.Button(gen_window, text = "Password Tips", command = show_tips)
advice_button.grid(column = 0, row = 1, pady = 20)

label_frame1 = ttk.LabelFrame(gen_window, text = "Your Password Generator Options:")
label_frame1.grid(column = 0, row = 2, padx = 15, pady = 5)

label_1 = ttk.Label(label_frame1, 
text = "Enter the number of characters (between 8 and 500) for your new password :")
label_1.grid(column = 0, row = 0, pady = 20, padx = 5)

password_length = tk.StringVar()
password_length.set("20")   # I set an initial value!!
entry_1 = ttk.Entry(label_frame1, width = "10", textvariable = password_length)
entry_1.grid(column = 0, row = 1, padx = 20, pady = 5)
entry_1.focus()

chVarLetters = tk.IntVar()
check_1 = tk.Checkbutton(label_frame1, text = "Password has letters?", 
variable = chVarLetters, state = 'active')
check_1.select()
check_1.grid(column = 0, row = 2, sticky = 'W')

chVarNumbers = tk.IntVar()
check_1 = tk.Checkbutton(label_frame1, text = "Password has numbers?", 
variable = chVarNumbers, state = 'active')
check_1.select()
check_1.grid(column = 0, row = 3, sticky = 'W')

chVarSymbols = tk.IntVar()
check_1 = tk.Checkbutton(label_frame1, text = "Password has symbols?", 
variable = chVarSymbols, state = 'active')
check_1.select()
check_1.grid(column = 0, row = 4, sticky = 'W')


button_1 = ttk.Button(label_frame1, text = "Generate Password!", 
command = generate_password)
button_1.grid(column = 0, row = 5, columnspan = 2, pady = 20)

label_frame2 = ttk.LabelFrame(gen_window, text = "Your new password")
label_frame2.grid(column = 0, row = 3, padx = 20, pady = 5)

label_2 = ttk.Label(label_frame2, 
text = "Edit your new password if needed. Try to keep as generated.")
label_2.grid(column = 0, row = 0, pady = 10)

scr_pass = scrolledtext.ScrolledText(label_frame2, width = 42, height = 5, 
										wrap = tk.WORD)
scr_pass.grid(column = 0, row = 1, columnspan = 3, padx = 12, pady = 10)

button_2 = ttk.Button(label_frame2, text = "Generate Another Password!", 
						command = generate_password)
button_2.grid(column = 0, row = 2, pady = 15, sticky = "W")

button_3 = ttk.Button(label_frame2, text = "Copy to Clipboard", 
						command = _copyClipboard)
button_3.grid(column = 0, row = 2, sticky = "E")

#############################################
####### Creating the menu bar
#############################################
menu_bar = Menu(gen_window)
gen_window.config(menu = menu_bar)

#Creating the menu and adding items
file_menu = Menu(menu_bar, tearoff = 0)  
menu_bar.add_cascade(label = "File", menu = file_menu)
file_menu.add_command(label = "Exit", command = _quit)

help_menu = Menu(menu_bar, tearoff = 0)
menu_bar.add_cascade(label = "Help", menu = help_menu)
help_menu.add_command(label = "User guide", command = _openGuide)
help_menu.add_command(label = "Follow me on Git", command = _openGit)
help_menu.add_command(label = "About", command = _versionBox)

gen_window.mainloop()
