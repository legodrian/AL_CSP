# AL, Vibe code for a theater

def stupid_proof(age):
    if age.isnumeric():
        return age
    else:
        return "invalid"


age = input("Enter your age: ")

age = stupid_proof(age)

if age == "invalid":
    print("Invalid age")
else:
    age = int(age)

    matinee = input("Is this a matinee? (yes/no): ").lower()

    if matinee != "yes" and matinee != "no":
        print("Invalid matinee answer")
    else:
        if age <= 4:
            price = 0
        elif age <= 12:
            price = 8
        elif age <= 64:
            price = 12
        else:
            price = 9

        if matinee == "yes":
            price = price - 3

            if price < 0:
                price = 0

        print(f"Ticket price: ${price:.2f}")
