print("Enter the first number: ")   
num1_str = input()
num1 = float(num1_str)              #Converts the input of num1 into a decimal number
print("Enter the second number: ")
num2_str = input()
num2 = float(num2_str)              #Converts the input of num2 into a decimal number
sum_addition = float(num1 + num2)
sum_subtraction = float(num1 - num2)
sum_multiplication = float(num1 * num2)
sum_division = float(num1 / num2)
print("The sum of", num1, "and", num2, "is", sum_addition)
print("The difference of", num1, "and", num2, "is", sum_subtraction)
print("The product of", num1, "and", num2, "is", sum_multiplication)
print("The division of", num1, "and", num2, "is", sum_division)