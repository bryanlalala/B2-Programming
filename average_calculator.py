"""
Filename: <Average_calculator.py>>
Author: <Nunez, Bryan>
Created: <10/29/2026>
Instructor: Burgess
"""

sum = 0
count = 0
keep_going = "yes"

while keep_going == "yes":
    number = int(input("Enter a number: "))
    sum += number
    count += 1
    average = sum / count

    print("Current sum:", sum)
    print("Numbers entered so far:", count)
    print("Current average:", average)

    keep_going = input("Would you like to input another number? (yes/no): ")