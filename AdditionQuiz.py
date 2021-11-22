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
        QuestStatement = ("How about ", "Try ", "What? Try this instead  ", "Hmm. ", "This one: ", "Solve ", "Compute for ")
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


print("\n                Welcome to Add-trocious Monster's Quiz!\n Do you dare to take the TEST? Finish with a high score to get acknowledged.\n\nType '\33[92mstart\33[0m' to get started.\nType '\33[91mexit\33[0m' to close the program.")



QuizQuest("normal")
QuizQuest("veteran")