# AL, 7th, Silly Sentences

while True:
    name = input("Tell me a name: ").strip().capitalize()
    if name.isnumeric():
      print("That's a number not a name")
    elif " " in name: 
       print("Just one name.")
    else:
       break

while True:
    noun = input("Tell me a noun: ").strip().lower()
    if noun.isnumeric():
      print("That's a number not a noun")
    elif " " in noun: 
       print("Just one noun.")
    else:
       break


while True:
    noun_1 = input("Tell me another noun: ").strip().lower()
    if noun_1.isnumeric():
      print("Numbers are not noun")
    elif " " in noun_1: 
       print("One noun is okay.")
    else:
       break

while True:
    adjective = input("Tell me an adjective: ").strip().lower()
    if adjective.isnumeric():
      print("That's a number not an adjective")
    elif " " in adjective: 
       print("Just one adjective.")
    else:
       break

while True:
    verb = input("Tell me a verb that end in ing: ").strip().lower()
    if verb.isnumeric():
      print("That's a number not a verb")
    elif " " in verb: 
       print("Just one verb.")
    else:
       break

while True:
    food = input("Tell me a food: ").strip().lower()
    if food.isnumeric():
      print("That's a number not a food")
    elif " " in food: 
       print("Just one food.")
    else:
       break

print("My " + adjective + " " + noun +" was running late to the party at the house of " + name + ". At the party my " + noun + " was " + verb + " and stole a " + noun_1 + ". Going home he ate a " + food + ".")
