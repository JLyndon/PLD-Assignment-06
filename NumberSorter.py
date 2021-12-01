import time

# ---------- Context ------------
# Program A: Number Sorter
# Create a program that ask 4 numbers. 
# Print the 4 numbers from highest to lowest using only if-else statement.

def Usr_Input(): #Input Function
    while True:
        DecorativeProgress(0)
        Num_01 = input("\n\n\n\33[94mStart:\33[0m\nEnter \x1B[1mfirst\x1B[0m number: ")
        Ev_Num_01= CommaReader_Single(Num_01)
        if (SecuringNegativ(Ev_Num_01)) == True: #Initial Screening
            time.sleep(1.4)
            DecorativeProgress(5)
            while True:
                Num_02 = input("\n\nEnter \x1B[1msecond\x1B[0m number: ")
                Ev_Num_02= CommaReader_Single(Num_02)
                if (SecuringNegativ(Ev_Num_02)) == True:
                    time.sleep(1.4)
                    DecorativeProgress(10)
                    while True:
                        Num_03 = input("\n\nEnter \x1B[1mthird\x1B[0m number: ")
                        Ev_Num_03= CommaReader_Single(Num_03)
                        if (SecuringNegativ(Ev_Num_03)) == True:
                            time.sleep(1.4)
                            DecorativeProgress(17)
                            while True:
                                Num_04 = input("\n\nEnter \x1B[1mfourth\x1B[0m number: ")
                                Ev_Num_04= CommaReader_Single(Num_04)
                                if (SecuringNegativ(Ev_Num_04)) == True:
                                    time.sleep(1.4)
                                    DecorativeProgress(24)
                                    return Ev_Num_01, Ev_Num_02, Ev_Num_03, Ev_Num_04
                                else:
                                    ValidationState(Ev_Num_04) #Validation/Input Remarks - Statements
                        else:
                            ValidationState(Ev_Num_03)
                else:   
                    ValidationState(Ev_Num_02)         
        else:
            ValidationState(Ev_Num_01) 

def CommaReader_Single(StringVal): #Duplicate of CommaReader code block from previous exer.
    if "," in StringVal:
        CommaOmmi = StringVal.replace(",","")
        return CommaOmmi
    else:
        return StringVal

def ValidationState(StrEvaluee): #Third Layer of Validation - Displays a Reminder if the input is invalid.
    if StrEvaluee.isalpha() == True:
        return print("\33[91mInput must be a number!\33[0m")
    elif (StrEvaluee.isspace()) or (StrEvaluee == (None or "")) == True:
        return print("\33[91mThis field must have an input to proceed.\33[0m")
    elif StrEvaluee.replace(".","",1).replace("-","",1).isalnum() == True:
        if StrEvaluee[0] == "-":
            return print("\33[91mInput must be all numeric character!\33[0m")
        else:
            print("\33[91mSigns must be on the left side!\33[0m")
    elif " " in StrEvaluee:
        print("\33[91mInputs must not have a space!\33[0m")
    else:
        print("\33[91mPlease enter a valid number.\33[0m")

def PrimaryFilter(firstNum, secondNum, thirdNum, fourthNum): #Function for determining the highest value.
    if (firstNum >= secondNum) and (firstNum >= thirdNum) and (firstNum >= fourthNum):
        return firstNum, secondNum, thirdNum, fourthNum
    elif (secondNum >= firstNum) and (secondNum >= thirdNum) and (secondNum >= fourthNum):
        return secondNum, firstNum, thirdNum, fourthNum
    elif (thirdNum >= firstNum) and (thirdNum >= secondNum) and (thirdNum >= fourthNum):
        return thirdNum, firstNum, secondNum, fourthNum
    elif (fourthNum >= firstNum) and (fourthNum >= secondNum) and (fourthNum >= thirdNum):
        return fourthNum, firstNum, secondNum, thirdNum

def SecondaryFilter(Remain_01, Remain_02, Remain_03): #Function for determining second highest value.
    if (Remain_01 >= Remain_02) and (Remain_01 >= Remain_03):
        return Remain_01, Remain_02, Remain_03
    elif (Remain_02 >= Remain_01) and (Remain_02 >= Remain_03):
        return Remain_02, Remain_01, Remain_03
    elif (Remain_03 >= Remain_01) and (Remain_03 >= Remain_02):
        return Remain_03, Remain_01, Remain_02

def TertiaryFilter(Remain_11, Remain_22): #Function for comparing the remaining 2 
    if Remain_11 >= Remain_22:
        return Remain_11, Remain_22
    elif Remain_22 >= Remain_11:
        return Remain_22, Remain_11

def IntorFlt(EvalNum): # Converts String into either Float or Int Val depending on their decimal value.
    Number = str(EvalNum)
    if "." not in Number:
        return int(Number)
    else:
        WholeNum, SignificantVal_Dec = Number.split(".") 
        if int(SignificantVal_Dec) > 0:
            return float(Number)
        elif int(SignificantVal_Dec) == 0:
            return int(WholeNum)

def DisregardNegativeDecim(StrEvaluee_01): #Function for disregarding Negative Sign and Decimal Points for Evaluation.
    return StrEvaluee_01.replace(".","",1).replace("-","",1)

def DisregardListChar(StrEvaluee_02): #Function to disregard additional characters in list.
    return StrEvaluee_02.replace("'","").replace("[","").replace("]","").replace(",","") 

def SecuringNegativ(ConflictStr): #Function for Initial Screening - Checks for eligibility of input. 
    if "-" or "." in ConflictStr: #Check strings with negative values and decimal points.
        if (ConflictStr.count("-")) > 1:
            return False
        elif (ConflictStr.count(".")) > 1:
            return False
        else:
            if "-" in ConflictStr:
                if ConflictStr[0] == " ":
                    for i in ConflictStr:
                        if i != " ":
                            if i != "-":
                                return False
                            elif i == "-":
                                if " " in ConflictStr:
                                    return False
                elif ConflictStr[0] == "-":
                    if " " in ConflictStr:
                        return False
                    elif (ConflictStr[0] == "-") and (len(ConflictStr) == 1):
                        return False
                else:
                    return False

    if (DisregardListChar(DisregardNegativeDecim(ConflictStr)).isdigit()) == True: # Second layer of Validation -
        return True                                           #Are those inputs valid without negative sign and decimal pt?
    elif DisregardNegativeDecim(ConflictStr).isalpha() == True:
        return False
    elif DisregardNegativeDecim(ConflictStr).isalnum() == True:
        Alt_Conflict = list(sorted(ConflictStr))
        for i in Alt_Conflict:
            if i.isalpha() == True:
                position = int(Alt_Conflict.index(i))
                Alt_Conflict.insert(position,"s")
                ReadyConflict= str(Alt_Conflict)
                Mixed_num, Mixed_alpha = ReadyConflict.split("s",1)
                break
        if (DisregardListChar(DisregardNegativeDecim(Mixed_alpha)).isalpha() == True) and (DisregardListChar(DisregardNegativeDecim(Mixed_num)).isdigit() == True):
            return False # Error: Disregards Third layer Validation (Fixed)

def DecorativeProgress(HowFar): #Decor - prints a progress bar.
    print("\n\n\33[3m\33[34mProgress Bar:\33[0m\33[0m")
    ProgSymb = "◉"
    for progress in range(0,25):
        print("\33[90m━\33[0m",end="")
        if progress == HowFar:
            if HowFar == 0:
                ProgressMark = ""
            elif HowFar == 5:
                ProgressMark = "\33[3m2.5\33[0m"
            elif HowFar == 10:
                ProgressMark = "\33[90m━━\33[0m\33[3m5\33[0m"
            elif HowFar == 17:
                ProgressMark = "\33[3m7.5\33[0m"
            elif HowFar == 24:
                ProgressMark = "\33[3m100\33[0m"
                ProgSymb = "\33[1m★\33[0m"
                print(f"{ProgressMark}\33[93m{ProgSymb} \33[0m",end="")
                break
            print(f"{ProgressMark}\33[92m{ProgSymb} \33[0m",end="")
    print("")

#Main Program
print("\n                 Welcome to Number Sorter!\nGive me numbers, I'll sort them out for you in \33[93mdescending\33[0m order.\n\nType '\33[92mstart\33[0m' to get started.\nType '\33[91mexit\33[0m' to close the program.")
while True:
    Usr_Decision = input("\n> ").upper() #Usr Command - tells whether to proceed or not.
    if Usr_Decision == "START":
        while True:
            FNum, SNum, TNum, FtNum = Usr_Input()
            HighestOutput, Re_01, Re_02, Re_03 = PrimaryFilter(float(FNum), float(SNum), float(TNum), float(FtNum))
            SecondHighest, Re_11, Re_22 = SecondaryFilter(Re_01, Re_02, Re_03)
            ThirdHighest, LowestOutput = TertiaryFilter(Re_11, Re_22)

            time.sleep(2)
            #Print Statement
            print(f"\n\nHere you go:\n\33[91m\33[1mH\33[0m\33[0m \33[90m━━━━━━━━━━━━━━>\33[0m \33[94m\33[1mL\33[0m\33[0m\n\n \33[91m{IntorFlt(HighestOutput):,}\33[0m, \33[92m{IntorFlt(SecondHighest):,}\33[0m, \33[33m{IntorFlt(ThirdHighest):,}\33[0m, \33[94m{IntorFlt(LowestOutput):,}\33[0m")
            time.sleep(3)
            RepeatorTerminate = input("\n\nDo you wish to sort another set?\n          \33[92mYes\33[0m or \33[91mNo\33[0m\n\n> ").upper()  #Prompts Usr to choose an action (Repetition or Termination)
            while True: #Usr Command - Verify Action 
                if RepeatorTerminate == "YES":
                    RepeatorTerminate = "repeat_process"
                    break
                elif RepeatorTerminate == "NO":
                    RepeatorTerminate = "exit_prog"
                    print("\n\33[3mOkay! Have a good one!\33[0m :)")
                    break
                else:
                    print("\33[91mUnknown command\33[0m")
            if RepeatorTerminate == "repeat_process":
                continue
            elif RepeatorTerminate == "exit_prog":
                break
        break
    elif Usr_Decision == "EXIT": 
        Usr_Verify = input("\n\n\nAre you sure?\n  \33[92mYes\33[0m or \33[91mNo\33[0m\n\n> ").upper()
        while Usr_Verify != "YES" or "NO": #Usr Command - Verify Leave
            if Usr_Verify == "YES":
                Usr_Verify = "proceed_exit"
                print("\n\33[3m'Til next time!\33[0m :)")
                break
            elif Usr_Verify == "NO":
                Usr_Verify = "proceed_prog"
                print("\n\33[3m I knew it!\33[0m ;)\nShall we start?")
                print("\n\nType '\33[92mstart\33[0m' to get started.\nType '\33[91mexit\33[0m' to close the program.")
                break
            else:
                print("\33[91mUnknown command\33[0m")
        if Usr_Verify == "proceed_exit":
            break
        elif Usr_Verify == "proceed_prog":
            continue
    else:
        print("\33[91mUnknown command\33[0m")