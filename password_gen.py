# Password generator V 0.1

### Original code to work on CMD!  

# User is asked for num of characters.  This program checks that input 
# is valid (numbers > 0 and no letters) and generates a letter at a time.
# The same character won't be in the final password.
# 72 characters long is the top this generator can make with the above conditions.
# If password_gen is good enough (??) my plan is to save the password in a .txt
# or something (not sure the most secure method)


import random

char = ('0123456789abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVXYZ-!#$%+*~&???/=')

password = ""

while True:
	invalid_num = "***  Enter a valid number, please.  ***" 
	
	try:
		extension = int(input("How many characters would you like in your new password?: > "))
		if extension > 72:
			print("Sorry, can't generate a password this long.")
			print("Select a shorter number of characters.")
			continue
		if extension > 0:
			break
		else:
			print(invalid_num)
			print("")
			continue
	except ValueError:
		print(invalid_num)
		print("   **********************")

while len(password) < extension:
    character = random.choice(char)
	
    # To avoid repeated characters in the final password
    if character in  password:
	    continue
    else:
        password = password + character
        
		
print("This is your new password: ")
print("    " + password)
