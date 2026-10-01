# AL, Caesar Cipher

def stupid_proof_choice():
    while True: 
            choice = input("Would you like to (E)ncrypt or (D)ecrypt a message: ").upper()
            
            if choice == "E" or choice == "D" :
                return choice
            else:
                print("You think you are funny ? Try again >:/")

def stupid_proof_shift():
    while True: 
        try: 
            shift = int(input("Enter a shift amount: "))
            return shift
        except : 
            print("You think you are funny ? Try again >:/")

choice = stupid_proof_choice()
message = input("Enter your message: ")
shift = stupid_proof_shift()

def caesar_shift(message, shift):
    result = ""

    for char in message:
        if char.isalpha():
            if char.isupper():
                base = ord("A")  
             
            elif char.islower():
                base = ord("a")
            
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result += new_char
        else:
            result += char
    return result


if choice == "D":
    shift = -shift

result = caesar_shift(message, shift)

if choice == "E":
    print("Your encrypted message is:", result)
else:
    print("Your decrypted message is:", result)
