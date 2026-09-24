# Al, Password strength Checker

characters = False 
uppercase_letter = False
lowercase_letter = False
number = False
symbol = False


password = input("What is your password: ")


if len(password) >= 8: 
    characters = True 


for letter in password:
    if letter.isupper(): 
        uppercase_letter = True  
    elif letter.islower(): 
        lowercase_letter = True  
    elif letter.isdigit(): 
        number = True  
    else: 
        symbol = True


strength = 0

if characters == True:
    strength += 1

if uppercase_letter == True:
    strength += 1

if lowercase_letter == True:
    strength += 1

if number == True:
    strength += 1

if symbol == True:
    strength += 1

password_type = 0

if strength == 5:
    password_type = "Strong"
elif strength == 3 or strength == 4:
    password_type = "Medium"
else:
    password_type = "Weak"


print(f"At least 8 characters: {characters}")
print(f"Has an uppercase letter: {uppercase_letter}")
print(f"Has a lowercase letter: {lowercase_letter}")
print(f"Has a number: {number}")
print(f"Has a symbol: {symbol}")
print(f"Your password strength is: {password_type}")


if password_type != "Strong":
    missing = ""
    
    if characters == False:
        missing += "at least 8 characters, "
    if uppercase_letter == False:
        missing += "an uppercase letter, "
    if lowercase_letter == False:
        missing += "a lowercase letter, "
    if number == False:
        missing += "a number, "
    if symbol == False:
        missing += "a symbol, "
        
    print(f"To make it Strong, add: {missing}")
