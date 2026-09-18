#outschool work

while True:
    number = input("Tell me your favorite number: ").strip()
    
    if " " in number: 
       print("I said number.")
    
    elif number.isnumeric():

        print(f"{number} is a cool number!")
    else:
       break
