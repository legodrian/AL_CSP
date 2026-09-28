# AL, Nesting Notes

for number in range(1,21):
    if number %15 == 0 :
        print("Fizzbuzz") 
    elif number %3 == 0: 
        print("Fizz")
    elif number %5 == 0: 
        print("Buzz")
    else :
        print(number)


siblings = ["Arianna","Aaron","Adrian"]
count = 1 
if len(siblings) > 0 : 
    while count < len(siblings):
        print(f"{count}. {siblings[count -1]}")
        count += 1
else : 
    print("There is no siblings")


count = 2 
while count <= 20: 
    print(count)
    count += 2

for num in range(2,21, 2):
    print(num)

