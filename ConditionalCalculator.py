print("Welcome to Conditional calculator.")
print("the calculator will ask the user to input their first number, then input the operation \n(add +, subtract -, multiply *, or divide /) they desire to perform, and then their second number. \nThe calculator will then perform only the operation that the user requested ")


print("insert first number on the line below")
n1=int(input("number 1:"))

op=input("On the line below: type + for addition, type - for subtraction, type * for multiplication, type / for division: ")


print("insert second number on the line below ")
n2=int(input("number 2:"))

# Notice the indents below and the colon added to the division line
if op=="+":
    print(f"{n1} + {n2} = {n1+n2}")
elif op=="-":
    print(f"{n1} - {n2} = {n1-n2}")
elif op=="*":
    print(f"{n1} * {n2} = {n1*n2}")
elif op=="/":
    print(f"{n1} / {n2} = {n1/n2}")


print("thank you for using this program")
