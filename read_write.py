# AL, Reading and Writting to Files

with open("practice.txt", "r+") as file : 
    content = file.read()
    content = "Chapter 1:\n" + content + "\nAnd Christioher Robin was sitting on his doorstep putting on his big foots"
    file.write(content)

with open("practice.txt", "a") as file : 
    file.write("\nWinnie the Pooh and The Blustery Day") 
