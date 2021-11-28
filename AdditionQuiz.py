import random
import time

# --------------- Context --------------------
# Program B: Addition Quiz
# Create a program that automatically generate two random numbers to add (0 to 99)
# Let the user answer and evaluate if the user has the correct answer
# The program will ask the user 10 addition operation
# Display the result summary of the 10 operations (ex 9/10)

def RandNumPickerBegin(Set_Item, Difficulty, Number_Itm): #Function for Formulation of Addition Questions
    if Set_Item == 0:
        randNum_01, randNum_02 = Randomize(Difficulty)            #Always start with "What is ___" for naturality
        print(f"\n\n{Number_Itm}.) What is \33[92m{randNum_01}\33[0m + \33[92m{randNum_02}\33[0m = ____ ?")
        Usr_Answer_0 = input("\n\33[1m\33[3m\33[94mYour answer: \33[0m")
        Item_Result_0 = CheckingAns(str(Usr_Answer_0), str(randNum_01), str(randNum_02))
        return Item_Result_0
    elif Set_Item == 1:                                            #Random prompts for Addition Questions
        QuestStatement = ["How about ", "Try ", "What? Try this instead ", "Hmm. ", "This one: ", "Solve ", "Compute for "]
        randNum_11, randNum_22 = Randomize(Difficulty)
        print(f"\n\n{Number_Itm}.) {random.choice(QuestStatement)}\33[92m{randNum_11}\33[0m + \33[92m{randNum_22}\33[0m = ____ ?")
        Usr_Answer_1 = input("\n\33[1m\33[3m\33[94mYour answer: \33[0m")
        Item_Result_1 = CheckingAns(str(Usr_Answer_1), str(randNum_11), str(randNum_22))
        return Item_Result_1

def Randomize(Set_Difficulty): # Randomizer - Digit Generator Function
    if Set_Difficulty == "normal":
        random_01 = random.randint(0,99)
        random_02 = random.randint(0,99)
        return random_01, random_02 
    else:
        random_11 = random.uniform(0,99)
        random_22 = random.uniform(0,99)
        if Set_Difficulty == "veteran":
            rand_11 = round(random_11, 2)
            rand_22 = round(random_22, 2) 
            return rand_11, rand_22
        elif Set_Difficulty == "intermediate":
            rand_11 = round(random_11, 4)
            rand_22 = round(random_22, 4) 
            return rand_11, rand_22

def CheckingAns(Answer, FirstRandom, SecondRandom): # Asnwer Checker Function - returns 'correct,' 'wrong' and equivalent strings
    if (Answer == None) or (Answer == "") or (Answer.isspace() == True):
        return "wrong", "noinput"
    else:
        if "." in FirstRandom and SecondRandom:
            sum_0 = round(float(FirstRandom) + float(SecondRandom),4)
            if Answer.replace(".","", 1).isdecimal() == True:
                if float(Answer) == sum_0:
                    return "correct", sum_0
                else:
                    return "wrong", sum_0
            else:
                return "wrong", "invalid"
        elif "." not in FirstRandom and SecondRandom:
            sum_1 = (int(FirstRandom) + int(SecondRandom))
            if Answer.isdecimal() == True:
                if int(Answer) == sum_1:
                    return "correct", sum_1
                else:
                    return "wrong", sum_1
            else:
                return "wrong", "invalid"
        else:
            return "wrong", "invalid"

def QuizQuest(Chosen_Difficulty): # After Checking, Inputs and Results will be reevaluated and interpreted
    global Usr_Score                # thru this function
    Usr_Score = 0
    Item_Num = 0
    while Item_Num < 10:
        Item_Num += 1
        if Item_Num == 1:
            Question, Total = RandNumPickerBegin(0, Chosen_Difficulty, Item_Num)
            if Question == "correct":
                print("\n\33[92mCorrect!\33[0m")
                Usr_Score += 1
            elif Question == "wrong":
                if Total == "noinput":
                    print("\33[91mIncorrect! You have no input!\33[0m")
                elif Total == "invalid":
                    print("\n\33[91mIncorrect! Invalid answer format.\33[0m")
                else:
                    print(f"\n\33[91mIncorrect!\33[0m The correct answer is \33[93m{Total}\33[0m")
        elif Item_Num > 1:
            Question_, Total_ = RandNumPickerBegin(1, Chosen_Difficulty, Item_Num)
            if Question_ == "correct":
                print("\n\33[92mCorrect!\33[0m")
                Usr_Score += 1
            elif Question_ == "wrong":
                if Total_ == "noinput":
                    print("\33[91mIncorrect! You have no input!\33[0m")
                elif Total_ == "invalid":
                    print("\n\33[91mIncorrect! Invalid answer format.\33[0m")
                else:
                    print(f"\n\33[91mIncorrect!\33[0m The correct answer is \33[93m{Total_}\33[0m")
    #Final Score Interpretations
    if Usr_Score <= 4:
        print(f"\n\n\n                 You scored \33[91m{Usr_Score}\33[0m out of 10.\n","━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━".center(60, " "))
    elif Usr_Score <= 7:
        print(f"\n\n\n                You scored \33[93m{Usr_Score}\33[0m out of 10 \33[93m\33[1m ★\33[0m\n","━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━".center(60, " "))
    elif Usr_Score <= 9:
        print(f"\n\n\n               You scored \33[92m{Usr_Score}\33[0m out of 10 \33[93m\33[1m ★ ★\33[0m\n", "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━".center(60, " "))
    elif Usr_Score == 10:
        print(f"\n\n\n              You scored \33[94m{Usr_Score}\33[0m out of 10 \33[93m\33[1m  ★ ★ ★\33[0m\n","━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━".center(60, " "))
    # Decor - Further interpret the Results
    UsrsFate(Usr_Score)

def DifficultySelection(DifficOfChoice): #Function for Displaying Quiz Difficulty
    if (DifficOfChoice == "normal") or (DifficOfChoice == "1"):
        print("\n\n\n                    \33[100m NORMAL DIFFICULTY \33[0m\n","━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━".center(60, " "))
        print("  For normal level, solve for the sum of \33[93mwhole\33[0m values".center(67, " "))
        return QuizQuest('normal')
    elif (DifficOfChoice == "veteran") or (DifficOfChoice == "2"):
        print("\n\n\n                    \33[44m VETERAN DIFFICULTY \33[0m\n","━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━".center(60, " "))
        print("  For veteran level, solve for the sum of values with".center(60, " "),"\n","\33[94m(2)\33[0m decimal places. \n".center(67, " "))
        return QuizQuest('veteran')
    elif (DifficOfChoice == "intermediate") or (DifficOfChoice == "3"):
        print("\n\n\n                  \33[41m INTERMEDIATE DIFFICULTY \33[0m\n","━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━".center(60, " "))
        print(" For intermediate level, solve for the sum of values with".center(60, " "),"\n","\33[91m(4)\33[0m decimal places. \n".center(66, " "))
        return QuizQuest('intermediate')
    else:
        print("\33[91mUnknown Difficulty\33[0m")
        return "notvalid"

def DifficultyComment(RandomDiffic): # Function for ADD-trocious Monter's commentaries 
    if RandomDiffic == "normal":
        return print("\n\n\n\33[92mLucky you!\33[0m Answer in:")
    elif RandomDiffic == "veteran":
        return print("\n\n\n\33[94mGood luck\33[0m answering in:")
    elif RandomDiffic == "intermediate":
        return print("\n\n\n\33[91mOho. \33[0mBrace yourself as you will answer in:")

def Decor_MonsterFace(ProgPhase): # Decor - Function for Monter Pattern display
    output = ""
    if ProgPhase == "start": # Displays Angry version/pattern
        for row in range(0, 11):
            for column in range(0, 36):
                if (column == 20 and (row == 0 or row == 1)) or (column == 21 and (row >= 2 and row <= 5 or row == 10)) or (column == 22 and (row >= 3 and row <= 5 or row == 9)) or (column == 23 and (row >= 3 and row <= 5 or row == 8)) or (column == 24 and (row >= 3 and row <= 5 or row == 9)) or (column == 25 and (row >= 4 and row <= 5 or row == 10)) or (column == 26 and row == 9) or (column == 27 and row == 8) or (column == 28 and row == 9) or (column == 29 and (row >= 4 and row <= 5  or row == 10)) or (column == 30 and (row >= 3 and row <= 5 or row == 9)) or (column == 31 and (row >= 3 and row <= 5 or row == 8)) or (column == 32 and (row >= 3 and row <= 5 or row == 9)) or (column == 33 and (row >= 2 and row <= 5 or row == 10)) or (column == 34 and (row == 0 or row == 1)):
                    output = output+"\33[91m▉\33[0m"
                else:
                    output = output+" "
            output = output + "\n"
        return print(output)
    elif ProgPhase == "tamed": #Displays Friendly version/pattern
        for rw in range (0, 11):
            for col in range(0,36):
                if (col == 20 and rw == 7) or (col == 21 and (rw == 2 or rw == 8)) or (col == 22 and (rw >= 2 and rw <= 3 or rw == 9)) or (col == 23 and (rw >= 2 and rw <= 3 or rw == 8)) or (col == 24 and (rw == 2 or rw == 7)) or (col == 25 and  rw == 8) or (col == 26 and rw == 9) or (col == 27 and rw == 8) or (col == 28 and (rw == 2 or rw == 7)) or (col == 29 and (rw >= 2 and rw <= 3  or rw == 8)) or (col == 30 and (rw >= 2 and rw <= 3 or rw == 9)) or (col == 31 and (rw == 2 or rw == 8)) or (col == 32 and rw == 7):
                    output = output+"\33[94m▉\33[0m"
                else:
                    output = output+" "
            output = output + "\n"
        return print(output)

def Introduction(): #Prompts Name input
    global Usr_Name
    print("\nPsst..")
    time.sleep(2)
    print("\n\nPssssssst!\n\n")
    time.sleep(1.2)
    print("  \33[91mWho are you?\33[0m\nWhat's your name?")
    while True:
        Usr_Name = input("\n\n> ")
        if (Usr_Name.isspace() == True) or (Usr_Name == ""):
            print("Please enter a name.")
        elif (Usr_Name != "") or (Usr_Name != None) or (Usr_Name.isspace() == False):
            if " " in Usr_Name:
                print("Name must be at least 3 characters long and must not contain a space.")
            elif (len(Usr_Name)) <= 2: 
                print("Name must be at least 3 characters long.")
            elif (len(Usr_Name)) > 10:
                print("Name should be a maximum of 10 characters.")
            else:
                print("\n\nOh..")
                return print(f"\nHello, \33[93m\33[1m{Usr_Name}\33[0m")

def UsrsFate(TestScore): # Selection for TestScores
    if TestScore <= 4:
        print(f"\33[91mHow unfortunate,\33[93m Lyndon\33[0m\n".center(71, " "))
        Decor_MonsterFace("start")
        print("\33[91m*gulp*\33[0m".center(65, " "))
    elif TestScore <= 7:
        print(f"\33[93m{Usr_Name}\33[0m, you passed! Feel free to leave/escape.".center(70, " "))
    elif TestScore <= 9:
        print("Congratulations! You're almost there, keep it up!".center(62, " "))
    elif TestScore == 10:
        Decor_MonsterFace("tamed")
    print("\33[93m\33[1mWonderful!!\33[0m".center(70, " "),"\n","With your intelligence, you tamed the \33[41m\33[1m ADD-trocious Monster \33[0m!".center(70, " "))

#Main Program
Introduction()
time.sleep(1.7)
print("\n       Welcome to \33[41m\33[1m ADD-trocious Monster's \33[0m\33[100m\33[1m QUIZ \33[0m!")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n".center(60, " "))
Decor_MonsterFace("start")
print("Do you think you're brave enough to take the test?".center(60, " "))
print("\33[92m\33[1mYes\33[0m, \33[1m\33[91mNo\33[0m or.. \33[93mmaybe\33[0m \33[94m\33[1mRUN?!\33[0m".center(105, " "))
while True:
    Usr_Decision = input("\n> ").lower() # Users will get redirected into any of the 4 paths based on input.
    if Usr_Decision.replace("!","").replace("?","") == "yes":
        print("\n\n\33[3m\33[92mVery well.. \33[0m")
        time.sleep(1.7)
        print("\n\nChoose your difficulty:\nType '\33[92m1\33[0m' or '\33[92mnormal\33[0m' for normal difficulty.\nType '\33[94m2\33[0m' or '\33[94mveteran\33[0m' for veteran difficulty.\nType '\33[91m3\33[0m' or '\33[91mintermediate\33[0m' for intermediate difficulty.")
        while True:
            ChoosingDiffi = input("\n\n> ").lower()
            IsInptValid = DifficultySelection(ChoosingDiffi)
            if IsInptValid == "notvalid":
                pass
            else:
                break
        break
    elif Usr_Decision.replace("!","").replace("?","") == "run": #If users decided to choose "run," the program will force them to answer the quiz.
        print("\n\n\33[3m\33[91mOh no you won't..\33[0m\33[3m\n\nThere's no escape! You have to give me an answer!\33[0m")
        time.sleep(1.7)
        print("\nAs punishment for running away, I'll \33[91m\33[1mrandomly\33[0m select the difficulty of your trial.\n\33[40m   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\33[0m")
        time.sleep(1.9)
        RandomDifficulty = random.choice(["veteran", "normal", "intermediate"])
        DifficultyComment(RandomDifficulty)
        time.sleep(1.3)
        DifficultySelection(RandomDifficulty)
        break
    elif Usr_Decision.replace("!","").replace("?","") == "no": #If they choose "no," the program will have no follow-ups.
        print("\n\33[3mCome whenever you're ready!\33[0m")
        break
    elif Usr_Decision.replace("!","").replace("?","") == "maybe": #Same path as "no"
        print("\n\33[3mMake up your mind. Come whenever you're ready!\33[0m")
        break
    else:
        print("\33[91mUnknown command\33[0m")