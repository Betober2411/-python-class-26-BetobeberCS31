# Starting file for LAB 1
# Include your course number, student first and last name, and date in the comment header
# CS 31 Lab Activity 1
# Sunday Octuber 4th 2026
# Carlos Farias

## 2. Display Hello, World!
print("Hi, World")


## 3. Add Two Numbers : Write code to add two numbers together. Print the complete equation and calculated total.
a = 10
b = 55
total3 = a + b
#print(a + b)
print(f"{a} + {b} = {total3}")


## 4. Multiply Three Numbers : Print out the complete equation and calculated answer.
a = 5
b = 10
c = 2
total4 = a*b*c
print(f"{a}*{b}*{c} = {total4}")

## 5. Create firstName: Create a variable named firstName
firstName = "Beto"

## 6. Create lastName: Create a variable named lastName
lastName = "Farias"

## 7. Create major: Create a variable named major
major = "Computer Science"

## 8. Display Your Name: Use your variables to display:
print(f"My name is {firstName} {lastName} ")

## 9. Display Your Major: 
print(f"My Major is {major}")

## 10. Ask for num1: Ask the user to Enter a number from 0 - 100: Store the user's answer in a variable named num1

num1 = int(input("Enter a number from 0 al 100: "))
while num1 < 0 or num1 > 100:
    print("Number out of range. Please try again..")
    num1 = int(input("Enter a number from 0 al 100: "))

## 11. Ask for num2: Ask the user to Enter a number from 10 - 10000: Store the user's answer in a variable named num2
num2 = int(input("Enter a number from 10 al 10000: "))
while num1 < 10 or num1 > 10000:
    print("Number out of range. Please try again..")
    num2 = int(input("Enter a number from 10 al 10000: "))

## 12. Multiply num1 and num2: Use Python to multiply the two values.
result = num1 * num2
print(f"{num1} * {num2} = {result}")

## 13. Experiment: Add at least **one or two additional lines of Python code of your own.

x = int(input("Enter an integer: "))
y = int(input("Enter an integer: "))
if (x >= y):
    print(x, "is greater.")
else:
    print(y, "is greater.")