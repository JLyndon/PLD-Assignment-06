import random

# Program 2: Addition Quiz
# Create a program that automatically generate two random numbers to add (0 to 99)
# Let the user answer and evaluate if the user has the correct answer
# The program will ask the user 10 addition operation
# Display the result summary of the 10 operations (ex 9/10)

def RandNumPicker():
    randNum_01 = random.randint(0,99)
    randNum_02 = random.randint(0,99)
    print(f"\n\nWhat is {randNum_01} + {randNum_02} = ?")
    Usr_Answer = input("\nPlace your answer here.\n> ")
    if Usr_Answer.isdigit() == True:
        if int(Usr_Answer) == (randNum_01 + randNum_02):
            return "correct"
        else:
            return "wrong"
    else:
        return "wrong"

Usr_Score = 0
Item_01 = RandNumPicker()
if Item_01 == "correct":
    Usr_Score += 1
else:
    None

print(f"\nYour score: {Usr_Score}/10")