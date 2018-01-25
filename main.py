# Password Gen v 0.2b
# Third version of Password Gen.  Nicolás Táutiva ->   nicolastautiva at hotmail com

###################
####  TO FIX: #####
# 1.  Check if entry is number or letter.  Manage error accordingly
# 3.  There are no instructions on how to use the Password Generator.  Create another button? Tooltips?
# 4.  Error when CREATE ANOTHER PASSWORD.  I have to delete Scrolledtext content, and the insert a new one
# 5.  Code is still very messy.  It works... but I have to work on this!!
##################
##################


import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import scrolledtext
from tkinter import messagebox as msg 
import random

version = "Version 0.2b"


#Chars, numbers & symbols to use
LETTERS = ('abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVXYZ')
NUMBERS = ('0123456789')
SYMBOLS = ('@-!#$%+*~&¿?;:/=')     #Are they all accepted?  


def show_tips():
	tips_window = tk.Tk()
	tips_window.title("Tips to select a new Password")
	tips_window.geometry("500x600")
	tips_window.resizable(False, False)
	tips_window.wm_iconbitmap("passgen.ico")
	
	scrol_w = 60
	scrol_h = 33
	scr_tip = scrolledtext.ScrolledText(tips_window, width = scrol_w, height = scrol_h, wrap = tk.WORD)
	scr_tip.grid(column = 1, columnspan = 3)
	
	with open("password_tips.txt") as file_object:
		contents = file_object.read()
			
	scr_tip.insert(tk.INSERT, contents)
	
	
	def _destroyWindow():
		tips_window.quit()
		tips_window.destroy()
		
	#Improve.  To center the CLOSE button!
	close_button = ttk.Button(tips_window, text = " Close ", command = _destroyWindow)
	close_button.grid(column = 1, row = 3, columnspan = 2, pady = 25)
	
	tips_window.mainloop()	
	
	
def _quit():      # Function to close the main.py program
	window.quit()
	window.destroy()
	exit()

def _msgBox(title = "Invalid number!", message = "Enter a valid number between 8 and 5000"):
	msg.showwarning(title, message)

def _versionBox():
	msg.showinfo("Python message info Box", "Password Generator  {} \n \n By Nicolás Táutiva".format(version))


def generate_password():
	print(type(password_length.get()))
	password = []
	values_for_password = []
	if type(password_length.get()) == int:

		if password_length.get() < 8:
			_msgBox()
			
		elif password_length.get() > 10000:
			_msgBox(message = "Sorry, Can't generate a password this long!")
			
		else:
			#Dictionary to check and store user values.   THIS IS WORKINIG!!!
			variable_values = {'chVarLetters' : chVarLetters.get(),
							'chVarNumbers' : chVarNumbers.get(),
							'chVarSymbols' : chVarSymbols.get()
							}
		
			#just to test the values-  TO BE DELETED!!!
			print(variable_values)
			
	
			#To check the user preferences.  If checked, it'll be added to list values_for_password.	
			for key, value in variable_values.items():
				if value == 1:
					values_for_password.append(key)
				else:
					continue
			
			#just to test the values-  TO BE DELETED!!!	
			print(values_for_password)
			print("list lenght = " + str(len(values_for_password)))
	
			if not values_for_password:
				_msgBox(title = "Error!", message = "At least one option must be checked!")

			else:
				#Dictionary to match the variable name from the buttons and the varibale value (LETTERS, NUMBERS or SYMBOLS)
				equivalent_values = { 'chVarLetters' : LETTERS,
										'chVarNumbers' : NUMBERS,
										'chVarSymbols' : SYMBOLS
									}
				
				if len(values_for_password) == 3:
					print("3 opciones")    # If three options... it's working like a charm!!! :)
					
					for i in range(round(password_length.get() / 3)):
						item = values_for_password[0]
						character = random.choice(equivalent_values[item])
						password.append(character)

					for i in range(round(password_length.get() / 3)):
						item = values_for_password[1]
						character = random.choice(equivalent_values[item])
						password.append(character)
								
					while len(password) < password_length.get():
						item = values_for_password[2]
						character = random.choice(equivalent_values[item])
						password.append(character)
					
				elif len(values_for_password) == 2:
					print("2 opciones")  # If two options... it's working like a charm!!! :)
									
					for i in range(round(password_length.get() / 2)):
						item = values_for_password[0]
						character = random.choice(equivalent_values[item])
						password.append(character)
					
					while len(password) < password_length.get():
						item = values_for_password[1]
						character = random.choice(equivalent_values[item])
						password.append(character)
				
				else:
					print("Una opcion") # If one option... it's working like a charm!!! :)
					
					for key, value in equivalent_values.items():
						if key in values_for_password:
							while len(password) < password_length.get():
								character = random.choice(value)
								password.append(character)
							print(password) #  A control print. TO BE DELETED!!
							print(len(password))
						else:
							continue
																	
	else:
		_msgBox(message = "Error mal manejado")
	
			
	print(password) 	#  print original password, then shuffle it, print lenght.  TO BE DELETED
	random.shuffle(password) # shuffle password.
	print(password)    	#  print original password, then shuffle it, print lenght.  TO BE DELETED
	password = "".join(password) # Turn password into a string
	print(password)    	#  print original password, then shuffle it, print lenght.  TO BE DELETED
	print(len(password))    	#  print original password, then shuffle it, print lenght.  TO BE DELETED
	# Insert the password into the scrolledtext.
	scr_pass.insert(tk.INSERT, password)


#############################################
####### Creating the GUI for the main program
#############################################			

window = tk.Tk()
window.title(version)
window.geometry("800x600")
window.resizable(False, False)
window.wm_iconbitmap("passgen.ico")

#############################################
####### Creating the Tabs
#############################################

#Tab1 for the password Generator.  
tab_control = ttk.Notebook(window) # create the tabcontrol
tab_1 = ttk.Frame(tab_control)     #create a tab
tab_control.add(tab_1, text = "Password Generator")     # add the tab
tab_control.pack(expand = 1, fill = "both")         # pack it to make it visible

#Tab2 for the Password Manager
tab_2 = ttk.Frame(tab_control)
tab_control.add(tab_2, text = "Password Manager")
tab_control.pack(expand = 1)


#############################################
####### Creating the Widgets for Tab 1
#############################################

advice_button = ttk.Button(tab_1, text = "Password Tips", command = show_tips)
advice_button.grid(column = 0, row = 0, pady = 20)

label_frame1 = ttk.LabelFrame(tab_1, text = "Your Password Generator Options:")
label_frame1.grid(column = 0, row = 1, padx = 20, pady = 5)

label_1 = ttk.Label(label_frame1, text = "Number of characters in new password? :")
label_1.grid(column = 0, row = 0, pady = 20)

password_length = tk.IntVar()
password_length.set("11")   # I set an initial value!!
entry_1 = ttk.Entry(label_frame1, width = "5", textvariable = password_length)
entry_1.grid(column = 1, row = 0, padx = 20, pady = 20)
entry_1.focus()

chVarLetters = tk.IntVar()
check_1 = tk.Checkbutton(label_frame1, text = "Password has letters?", variable = chVarLetters,
						state = 'active')
check_1.select()
check_1.grid(column = 0, row = 1, sticky = 'W')

chVarNumbers = tk.IntVar()
check_1 = tk.Checkbutton(label_frame1, text = "Password has numbers?", variable = chVarNumbers,
						state = 'active')
check_1.select()
check_1.grid(column = 0, row = 2, sticky = 'W')

chVarSymbols = tk.IntVar()
check_1 = tk.Checkbutton(label_frame1, text = "Password has symbols?", variable = chVarSymbols,
						state = 'active')
check_1.select()
check_1.grid(column = 0, row = 3, sticky = 'W')


button_1 = ttk.Button(label_frame1, text = "Generate Password!", command = generate_password)
button_1.grid(column = 0, row = 4, columnspan = 2, pady = 20)

##################
###### More Widgets for Tab1... but in Frame 2
##################
label_frame2 = ttk.LabelFrame(tab_1, text = "Your new password")
label_frame2.grid(column = 1, row = 1, padx = 20, pady = 5)

label_2 = ttk.Label(label_frame2, text = "Edit your new password if needed.  Try to keep as generated.")
label_2.grid(column = 0, row = 0, pady = 10)

scrol_w = 42
scrol_h = 5
scr_pass = scrolledtext.ScrolledText(label_frame2, width = scrol_w, height = scrol_h, wrap = tk.WORD)
scr_pass.grid(column = 0, row = 1, columnspan = 3, padx = 12, pady = 10)

# Falta que el generado de codigo lo envíe a este widget!		
#scr_pass.insert(tk.INSERT, password)

#Este boton genera el mismo còdig que el generate_password
button_2 = ttk.Button(label_frame2, text = "Generate Another Password!", command = generate_password)
button_2.grid(column = 0, row = 2, columnspan = 3, pady = 15)


#############################################
####### Creating the menu bar
#############################################
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