import random

# Program 2: Addition Quiz
# Create a program that automatically generate two random numbers to add (0 to 99)
# Let the user answer and evaluate if the user has the correct answer
# The program will ask the user 10 addition operation
# Display the result summary of the 10 operations (ex 9/10)

def RandNumPicker():
    randNum_01 = random.randint(0,99)
    randNum_02 = random.randint(0,99)
    return randNum_01, randNum_02

FNum, SNum = RandNumPicker()
print(f"What is {FNum} + {SNum} = ?")
Usr_Answer = int(input("\nPlace your answer here.\n> "))
if Usr_Answer == (FNum + SNum):
    print("Correct!")
else:
    None