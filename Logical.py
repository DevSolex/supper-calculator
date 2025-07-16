# a simple calculator app, the program will only handle two numbers
print('''welcome to our simple calculator
**********************
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exponential
6. Floor division
********************************''')
print("Enter two numbers to add")
#prompt a user for a number and store it
first_number = input("first number:")
#prompt the user for nuber and store it
second_number = input("second number:")
sum = float(first_number) + float(second_number)
print(f"{first_number} + {second_number} = {sum:.2f}")

print('''***********************
subtraction
********************************
Enter two numbers to subtrac''')
#prompt a user for a number and store it
first_number = input("first number:")
#prompt the user for nuber and store it
second_number = input("second number:")
sub = float(first_number) - float(second_number)
print(f"{first_number} - {second_number} = {sub:.2f}")

print('''***********************
multiplication
********************************
Enter two numbers to multiply''')
#prompt a user for a number and store it
first_number = input("first number:")
#prompt the user for nuber and store it
second_number = input("second number:")
mul = float(first_number) * float(second_number)
print(f"{first_number} * {second_number} = {mul:.2f}")

print('''***********************
division
********************************
Enter two numbers to divide''')
#prompt a user for a number and store it
first_number = input("first number:")
#prompt the user for nuber and store it
second_number = input("second number:")
div = float(first_number) / float(second_number)
print(f"{first_number} / {second_number} = {div:.2f}")

print('''***********************
exponential
********************************
Enter two numbers to get exponential''')
#prompt a user for a number and store it
first_number = input("first number:")
#prompt the user for nuber and store it
second_number = input("second number:")
expo = float(first_number) ** float(second_number)
print(f"{first_number} ** {second_number} = {expo:.2f}")

print('''***********************
floor division
********************************
Enter two numbers to get exponential''')
#prompt a user for a number and store it
first_number = input("first number:")
#prompt the user for nuber and store it
second_number = input("second number:")
floor = float(first_number) // float(second_number)
print(f"{first_number} // {second_number} = {floor:.2f}")

