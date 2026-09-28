"""
Filename: simple_calculator.py
Author: <Nunez, Bryan>
Created: <09/22/2026>
Instructor: Burgess
"""


print("Welcome to simple calculator.")
print("This calculator will ask the user to input two numbers,")
print("then the program will perform the four basic operations on the two numbers")
print(" (add, subtract, multiply, and divide).")


print("insert first number on the line below")
n1=int(input("number 1:"))
print('insert second number on the line below')
n2=int(input("number 2:"))

print(f"{n1} + {n2} = {n1+n2}")
print(f"{n1} - {n2} = {n1-n2}")
print(f"{n1} * {n2} = {n1*n2}")
print(f"{n1} / {n2} = {n1/n2}")

print("thank you for using this program")