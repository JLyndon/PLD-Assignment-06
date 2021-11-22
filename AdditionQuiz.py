import random

# --------------- Context --------------------
# Program B: Addition Quiz
# Create a program that automatically generate two random numbers to add (0 to 99)
# Let the user answer and evaluate if the user has the correct answer
# The program will ask the user 10 addition operation
# Display the result summary of the 10 operations (ex 9/10)

def RandNumPickerBegin(Set_Item, Difficulty):
    if Set_Item == 0:
        randNum_01, randNum_02 = Randomize(Difficulty)
        print(f"\n\nWhat is {randNum_01} + {randNum_02} = ____ ?")
        Usr_Answer_0 = input("\nYour answer, here.\n\n> ")
        Item_Result_0 = CheckingAns(str(Usr_Answer_0), str(randNum_01), str(randNum_02))
        return Item_Result_0
    elif Set_Item == 1:
        QuestStatement = ["How about ", "Try ", "What? Try this instead  ", "Hmm. ", "This one: ", "Solve ", "Compute for "]
        randNum_11, randNum_22 = Randomize(Difficulty)
        print(f"\n\n{random.choice(QuestStatement)}{randNum_11} + {randNum_22} = ____ ?")
        Usr_Answer_1 = input("\nYour answer, here.\n\n> ")
        Item_Result_1 = CheckingAns(str(Usr_Answer_1), str(randNum_11), str(randNum_22))
        return Item_Result_1

def Randomize(Set_Difficulty):
    if Set_Difficulty == "normal":
        random_01 = random.randint(0,99)
        random_02 = random.randint(0,99)
        return random_01, random_02 
    elif Set_Difficulty == "veteran":
        random_11 = random.uniform(0,99)
        random_22 = random.uniform(0,99)
        rand_11 = round(random_11, 2)
        rand_22 = round(random_22, 2) 
        return rand_11, rand_22
    elif Set_Difficulty == "intermediate":
        random_11 = random.uniform(0,99)
        random_22 = random.uniform(0,99)
        rand_11 = round(random_11, 4)
        rand_22 = round(random_22, 4) 
        return rand_11, rand_22

def CheckingAns(Answer, FirstRandom, SecondRandom):
    if "." in FirstRandom and SecondRandom:
        if Answer.replace(".","", 1).isdecimal() == True:
            if float(Answer) == (float(FirstRandom) + float(SecondRandom)):
                return "correct"
            else:
                return "wrong"
        else:
            return "wrong"
    elif "." not in FirstRandom and SecondRandom:
        if Answer.isdecimal() == True:
            if int(Answer) == (int(FirstRandom) + int(SecondRandom)):
                return "correct"
            else:
                return "wrong"
        else:
            return "wrong"
    else:
        if (Answer == None) or (Answer == "") or (Answer.isspace() == True):
            return "wrong"
        else:
            return "wrong"

def QuizQuest(Chosen_Difficulty):
    Usr_Score = 0
    Item_Num = 0
    while Item_Num < 10:
        Item_Num += 1
        if Item_Num == 1:
            Question = RandNumPickerBegin(0, Chosen_Difficulty)
            if Question == "correct":
                Usr_Score += 1
            else:
                None
        elif Item_Num > 1:
            Question_ = RandNumPickerBegin(1, Chosen_Difficulty)
            if Question_ == "correct":
                Usr_Score += 1
            else:
                None
    print(f"\nYour score: {Usr_Score}/10")

def DifficultySelection(DifficOfChoice):
    if DifficOfChoice == "1" or "normal":
        print("\n\n                    \33[100m NORMAL DIFFICULTY \33[0m")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n".center(60, " "))
        return QuizQuest('normal')
    elif DifficOfChoice == "2" or "veteran":
        print("\n\n                  \33[44m VETERAN DIFFICULTY \33[0m")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n".center(60, " "))
        return QuizQuest('veteran')
    elif DifficOfChoice == "3" or "intermediate":
        print("\n\n               \33[41m INTERMEDIATE DIFFICULTY \33[0m")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n".center(60, " "))
        return QuizQuest('intermediate')
    else:
        return print("\33[91mUnknown Difficulty\33[0m")

def Decor_MonsterFace():
    output = ""
    for row in range(0, 11):
        for column in range(0, 36):
            if (column == 20 and (row == 0 or row == 1)) or (column == 21 and (row >= 2 and row <= 5 or row == 10)) or (column == 22 and (row >= 3 and row <= 5 or row == 9)) or (column == 23 and (row >= 3 and row <= 5 or row == 8)) or (column == 24 and (row >= 3 and row <= 5 or row == 9)) or (column == 25 and (row >= 4 and row <= 5 or row == 10)) or (column == 26 and row == 9) or (column == 27 and row == 8) or (column == 28 and row == 9) or (column == 29 and (row >= 4 and row <= 5  or row == 10)) or (column == 30 and (row >= 3 and row <= 5 or row == 9)) or (column == 31 and (row >= 3 and row <= 5 or row == 8)) or (column == 32 and (row >= 3 and row <= 5 or row == 9)) or (column == 33 and (row >= 2 and row <= 5 or row == 10)) or (column == 34 and (row == 0 or row == 1)):
                output = output+"\33[91m▉\33[0m"
            else:
                output = output+" "
        output = output + "\n"
    return print(output)

#Main Program
print("\n       Welcome to \33[41m\33[1m ADD-trocious Monster's \33[0m\33[100m\33[1m QUIZ \33[0m!")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n".center(60, " "))
Decor_MonsterFace()
print("Do you think you're brave enough to take the test?".center(60, " "))
while True:
    Usr_Decision = input("\n> ").lower()
    if Usr_Decision == "yes":
        print("\n\nVery well.. \n\nChoose your difficulty:\nType '1' or 'normal' for normal difficulty.\nType '2' or 'veteran' for veteran difficulty.\nType '3' or 'intermediate' for intermediate difficulty.")
        while True:
            ChoosingDiffi = input("\n\n> ").lower()
            DifficultySelection(ChoosingDiffi)
            break
        break
    elif Usr_Decision == "run":
        print("\n\nThere's no escape! You have to give me an answer!\n\n As punishment, I'll randomly choose the difficulty of your trial.")
        Difficulties = ["normal", "veteran", "intermediate"]
        RandDiff = random.choice(Difficulties)
        DifficultySelection(RandDiff)
        break
    elif Usr_Decision == "no":
        print("Come whenever you're ready!")
        break
    else:
        print("\33[91mUnknown command\33[0m")
        