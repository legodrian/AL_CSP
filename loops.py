#AL, Loops Notes 
import random

count = 1 

while count <= 10: 
    print(count)
    count += 1

ducks = 1 
goose = random.randint(1,11)
while True: 
    if ducks == goose : 
        break
    print("Duck. . . .")
    ducks += 1 #ducks = ducks + 1

print("GOOSE!!!!")

# Complex data type = holds other data types on it
siblings = ["Arianna","Aaron"] 
print(siblings[0])

#Adding to the list
siblings.append("Sebastian")
print(siblings)

siblings.insert(1, "Adrian")
print(siblings)

#Remove from the list
siblings.pop(3)
print(siblings)

#Print each item in a list
for sibling in siblings : 
    print(sibling)



#For Loops
for num in range(1,25):
    if num %15 == 0 :
        print("Fizzbuzz") 
    elif num %3 == 0: 
        print("Fizz")
    elif num %5 == 0: 
        print("Buzz")
    else :
        print(num)

