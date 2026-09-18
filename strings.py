#AL, Strings 
#Strings => any saved inside of quotation marks "" ''

name = input('Whats your name: ').strip().capitalize()

age = input('How old are you: ')
print(type(age))

#Concatenation = > puts a string directly next to each other
print(age + age) 

print(name + " " + "Leon") 

#Senctence
sentence = "The quick brown fox jumped over the lazy dog"

print(sentence)
print(sentence.replace("dog","monkey"))
print(len(name)) #<= gets the length of a string

print(f"Your name is {name} that is {len(name)} letters long. Your initial is {name[0]} I think i will call you {name[0:3]}")