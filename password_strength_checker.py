# Al, Password strength Checker

#conditional to password long enough 
#update length variable to "true"

#for letter in password: 

characters = False 
uppercase_letter = False
lowercase_letter = False
number = False
symbol = False

password = input("What is your password: ")

for letter in password :
    if len(password) < 8 : 
     characters = True 


for uppercarse_letter in password :
   if password.isupper() : 
    uppercase_letter = True 

for lower_case in password : 
   if password.islower() : 
    lowercase_letter = True 

for number in password : 
  if password.isnumeric() : 
    number = True 

for symbol in password : 
  if letter in "!@#$%?/" : 
    symbol = True 

