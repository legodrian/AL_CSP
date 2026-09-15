#AL, Hello user 

while True: 
    name = input("Tell me only your first name ").strip().capitalize()
    if name.isnumeric():
        print("Numbers are not names >:/")
    elif " " in name: 
        print("I said only your first name >:/")
    else: 
        break

print(f"Hello {name} :)! Nice to meet you") 