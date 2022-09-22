#!/usr/bin/python3

# Just setting up a variable
count = 0

#Open the txt file and read it
with open("dracula.txt","r") as vampire:
    with open("vamps.txt", "w") as fang: #Create a file to write to
        for line in vampire:
            if "vampire" in line.lower(): #Anytime the word vampire appears write it into the text file
                print(line) #Prints all the lines with the word vampire
                count +=1
                fang.write(line) 
print(count)

