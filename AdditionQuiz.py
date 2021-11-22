import random
import time

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
                print("Incorrect!")
                None
        elif Item_Num > 1:
            Question_ = RandNumPickerBegin(1, Chosen_Difficulty)
            if Question_ == "correct":
                Usr_Score += 1
            else:
                print("Incorrect!")
                None
    print(f"\nYou got {Usr_Score} out of 10 equations right.")

def DifficultySelection(DifficOfChoice):
    if (DifficOfChoice == "normal") or (DifficOfChoice == "1"):
        print("\n\n                    \33[100m NORMAL DIFFICULTY \33[0m")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n".center(60, " "))
        return QuizQuest('normal')
    elif (DifficOfChoice == "veteran") or (DifficOfChoice == "2"):
        print("\n\n                  \33[44m VETERAN DIFFICULTY \33[0m")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n".center(60, " "))
        return QuizQuest('veteran')
    elif (DifficOfChoice == "intermediate") or (DifficOfChoice == "3"):
        print("\n\n               \33[41m INTERMEDIATE DIFFICULTY \33[0m")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n".center(60, " "))
        return QuizQuest('intermediate')
    else:
        return print("\33[91mUnknown Difficulty\33[0m")

def DifficultyComment(RandomDiffic):
    if RandomDiffic == "normal":
        return print("\n\n\33[92mLucky you!\33[0m Answer in:")
    elif RandomDiffic == "veteran":
        return print("\n\n\33[94mGood luck!\33[0m Answer in:")
    elif RandomDiffic == "intermediate":
        return print("\n\n\33[91mOho. \33[0mBrace yourself as you will answer in:")

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
print("\33[92mYes\33[0m, \33[91mNo\33[0m or.. \33[94m\33[1mRUN?!\33[0m".center(85, " "))
while True:
    Usr_Decision = input("\n> ").lower()
    if Usr_Decision.replace("!","").replace("?","") == "yes":
        print("\n\n\33[3mVery well.. \33[0m\n\nChoose your difficulty:\nType '\33[92m1\33[0m' or '\33[92mnormal\33[0m' for normal difficulty.\nType '\33[94m2\33[0m' or '\33[94mveteran\33[0m' for veteran difficulty.\nType '\33[91m3\33[0m' or '\33[91mintermediate\33[0m' for intermediate difficulty.")
        while True:
            ChoosingDiffi = input("\n\n> ").lower()
            DifficultySelection(ChoosingDiffi)
            break
        break
    elif Usr_Decision.replace("!","").replace("?","") == "run":
        print("\n\n\33[3m\33[91mOh no you wont..\33[0m\33[3m\n\nThere's no escape! You have to give me an answer!\33[0m")
        time.sleep(1.5)
        print("\nAs punishment, I'll \33[91m\33[1mrandomly\33[0m choose the difficulty of your trial.")
        time.sleep(1.3)
        RandomDifficulty = random.choice(["veteran", "normal", "intermediate"])
        DifficultyComment(RandomDifficulty)
        time.sleep(1.3)
        DifficultySelection(RandomDifficulty)
        break
    elif Usr_Decision.replace("!","").replace("?","") == "no":
        print("\n\33[3mCome whenever you're ready!\33[0m")
        break
    elif Usr_Decision.replace("!","").replace("?","") == "maybe":
        print("\n\33[3mMake up your mind. Come whenever you're ready!\33[0m")
        break
    else:
        print("\33[91mUnknown command\33[0m")
        