# Program 1: Number Sorter
# Create a program that ask 4 numbers. 
# Print the 4 numbers from highest to lowest using only if-else statement.

firstNum = int(input("Enter first number: "))
secondNum = int(input("Enter second number: "))
thirdNum = int(input("Enter third number: "))
fourthNum = int(input("Enter fourth number: "))

if (firstNum > secondNum) and (firstNum > thirdNum) and (firstNum > fourthNum):
    print("First Number is the highest. Insert top of the list.")
elif (secondNum > firstNum) and (secondNum > thirdNum) and (secondNum > fourthNum):
    print("Second Number is the highest. Insert top of the list.")
elif (thirdNum > firstNum) and (thirdNum > secondNum) and (thirdNum > fourthNum):
    print("Third Number is the highest. Insert top of the list.")
elif (fourthNum > firstNum) and (fourthNum > secondNum) and (fourthNum > thirdNum):
    print("Fourth Number is the highest. Insert top of the list.")
else:
    print() #Insert conditions for secondary screening of inputs.
