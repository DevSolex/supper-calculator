# a simple calculator app, the program will only handle two numbers
print('''**********************
1. Addition
2. Subtraction
3. Multiplication
4. Division
********************************''')
print("Enter two numbers to add")
#prompt a user for a number and store it
first_number = input("first number:")
#prompt the user for nuber and store it
second_number = input("second number:")
sum = float(first_number) + float(second_number)
print(f"{first_number} + {second_number} = {sum}")

print('''***********************
subtraction
********************************
Enter two numbers to subtrac''')
#prompt a user for a number and store it
first_number = input("first number:")
#prompt the user for nuber and store it
second_number = input("second number:")
sub = float(first_number) - float(second_number)
print(f"{first_number} - {second_number} = {sub}")

print('''***********************
multiplication
********************************
Enter two numbers to multiply''')
#prompt a user for a number and store it
first_number = input("first number:")
#prompt the user for nuber and store it
second_number = input("second number:")
mul = float(first_number) * float(second_number)
print(f"{first_number} * {second_number} = {mul}")

