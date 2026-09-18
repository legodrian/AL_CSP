# AL, try 

while True:
    number = input("Tell me your favorite number: ").strip()
    if number.isnumeric():

        print(f"{number} is a cool number!")

    elif " " in number: 
       print("I said number.")
    else:
       break
