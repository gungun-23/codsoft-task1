import math

# Advanced Calculator Program

# Taking inputs from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nChoose operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Modulus (%)")
print("6. Power (num1 ** num2)")
print("7. Floor Division (//)")
print("8. Square Root of numbers\n")

choice = input("Enter your choice (1/2/3/4/5/6/7/8): ")

# Performing calculation
if choice == '1':
    print(f"Result: {num1} + {num2} = {num1 + num2}")

elif choice == '2':
    print(f"Result: {num1} - {num2} = {num1 - num2}")

elif choice == '3':
    print(f"Result: {num1} * {num2} = {num1 * num2}")

elif choice == '4':
    if num2 != 0:
        print(f"Result: {num1} / {num2} = {num1 / num2}")
    else:
        print("Error! Division by zero.")

elif choice == '5':
    print(f"Result: {num1} % {num2} = {num1 % num2}")

elif choice == '6':
    print(f"Result: {num1} ** {num2} = {num1 ** num2}")

elif choice == '7':
    if num2 != 0:
        print(f"Result: {num1} // {num2} = {num1 // num2}")
    else:
        print("Error! Division by zero.")

elif choice == '8':
    print(f"Square root of {num1} = {math.sqrt(num1)}")
    print(f"Square root of {num2} = {math.sqrt(num2)}")

else:
    print("Invalid choice! Please select a valid option.")
