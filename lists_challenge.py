#!/usr/bin/env python3

def main():

    #Creates a list called wordbank
    wordbank = ["indentation", "spaces"] 

    #Creates a list called tlgstudents
    tlgstudents = ["Aaron", "Andy", "Asif", "Brent", "Cedric", "Chris", "Cory", "Ebrima", "Franco", "Greg", "Hoon", "Joey", "Jordan", "JC", "LB", "Mabel", "Shon", "Pat", "Zach"]

    #adds 4 into wordbank at the end
    wordbank.append(4)

    #ask user for a number and converts it to int
    num = int(input("add an underaged  number -inclusive"))

    print(f'You chose {num}')

    student_name = tlgstudents[num]
    print(f'{student_name} always uses {wordbank[2]} {wordbank[1]} to indent.')

main()

