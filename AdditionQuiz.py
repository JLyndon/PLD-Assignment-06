import random

# --------------- Context --------------------
# Program B: Addition Quiz
# Create a program that automatically generate two random numbers to add (0 to 99)
# Let the user answer and evaluate if the user has the correct answer
# The program will ask the user 10 addition operation
# Display the result summary of the 10 operations (ex 9/10)

QuestStatement = ("How about ", "Try ", "Add ", "Hmm. ", "This one: ", "Solve ", "Compute for ")

def RandNumPickerStarter():
    randNum_01 = random.randint(0,99)
    randNum_02 = random.randint(0,99)
    print(f"\n\nWhat is {randNum_01} + {randNum_02} = ____ ?")
    Usr_Answer = input("\nYour answer, here.\n\n> ")
    if Usr_Answer.replace(".","").isdigit() == True:
        if int(Usr_Answer) == (randNum_01 + randNum_02):
            return "correct"
        else:
            return "wrong"
    else:
        return "wrong"

def RandNumPickerMid():
    randNum_01 = random.randint(0,99)
    randNum_02 = random.randint(0,99)
    print(f"\n\n{random.choice(QuestStatement)}{randNum_01} + {randNum_02} = ____ ?")
    Usr_Answer = input("\nYour answer, here.\n\n> ")
    if Usr_Answer.replace(".","").isdigit() == True:
        if int(Usr_Answer) == (randNum_01 + randNum_02):
            return "correct"
        else:
            return "wrong"
    else:
        return "wrong"

Usr_Score = 0
Item_Num = 0
while Item_Num < 10:
    Item_Num += 1
    if Item_Num == 1:
        Question = RandNumPickerStarter()
        if Question == "correct":
            Usr_Score += 1
        else:
            None
    elif Item_Num > 1:
        Question_ = RandNumPickerMid()
        if Question_ == "correct":
            Usr_Score += 1
        else:
            None

print(f"\nYour score: {Usr_Score}/10")
