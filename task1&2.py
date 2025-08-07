# task1.py
# Take input from the user

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform basic mathematical operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (division by zero)"

# Display the results
print("\n--- ANSWERS ---")
print(f"Addition:   {addition}")
print(f"Subtraction:   {subtraction}")
print(f"Multiplication:  {multiplication}")
print(f"Division:  {division}")

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")


full_name = (first_name+last_name)

print(f"welcome to python world,{full_name}")