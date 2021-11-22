# Program 1: Number Sorter
# Create a program that ask 4 numbers. 
# Print the 4 numbers from highest to lowest using only if-else statement.

def Usr_Input(): #Input Function
    while True:
        while True:
            Num_01 = input("\nEnter \x1B[1mfirst\x1B[0m number: ")
            Ev_Num_01= CommaReader_Single(Num_01)
            if (SecuringNegativ(Ev_Num_01)) == True: #Initial Screening
                while True:
                    Num_02 = input("\nEnter \x1B[1msecond\x1B[0m number: ")
                    Ev_Num_02= CommaReader_Single(Num_02)
                    if (SecuringNegativ(Ev_Num_02)) == True:
                        while True:
                            Num_03 = input("\nEnter \x1B[1mthird\x1B[0m number: ")
                            Ev_Num_03= CommaReader_Single(Num_03)
                            if (SecuringNegativ(Ev_Num_03)) == True:
                                while True:
                                    Num_04 = input("\nEnter \x1B[1mfourth\x1B[0m number: ")
                                    Ev_Num_04= CommaReader_Single(Num_04)
                                    if (SecuringNegativ(Ev_Num_04)) == True:
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

def ValidationState(StrEvaluee):
    if StrEvaluee.isalpha() == True:
        return print("Input must be a number!")
    elif (StrEvaluee.isspace()) or (StrEvaluee == (None or "")) == True:
        return print("This field must have an input to proceed.")
    elif StrEvaluee.replace(".","").replace("-","").isalnum() == True:
        return print("Input must be all numeric character!")
    elif " " in StrEvaluee:
        print("Inputs must not have a space!")
    else:
        print("Please enter a valid number.")

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

def IntorFlt(EvalNum):
    Number = str(EvalNum)
    if "." not in Number:
        return int(Number)
    else:
        WholeNum, SignificantVal_Dec = Number.split(".") 
        if int(SignificantVal_Dec) > 0:
            return float(Number)
        elif int(SignificantVal_Dec) == 0:
            return int(WholeNum)

def DisregardNegativeDecim(StrEvaluee_01):
    return StrEvaluee_01.replace(".","").replace("-","")

def DisregardListChar(StrEvaluee_02):
    return StrEvaluee_02.replace("'","").replace("[","").replace("]","").replace(",","")

def SecuringNegativ(ConflictStr): #Function for Initial Screening - Checks for eligibility of input. 
    if ConflictStr.isdigit() == True:
        return True
    elif DisregardNegativeDecim(ConflictStr).isalpha() == True:
        return False
    elif DisregardNegativeDecim(ConflictStr).isalnum() == True:
        Alt_Conflict = str(sorted(ConflictStr))
        for i in Alt_Conflict:
            if i.isalpha() == True:
                Mixed_alpha, Mixed_num = Alt_Conflict.split(i,1)
                break
        if (DisregardListChar(DisregardNegativeDecim(Mixed_alpha)).isalpha() == True) and (DisregardListChar(DisregardNegativeDecim(Mixed_num)).isdigit() == True):
            return False #CHECKPOINT - Error Occurs, Will Fix
    else:
        if "-" or "." in ConflictStr: #Check strings with negative values and decimal points.
            if "-" in ConflictStr:
                if ConflictStr[0] == " ":
                    for i in ConflictStr:
                        if i != " ":
                            if i != "-":
                                    return False
                            elif i == "-":
                                if " " in ConflictStr:
                                    return False
                                else:
                                    return True
                elif ConflictStr[0] == "-":
                    if " " in ConflictStr:
                        return False
                    else:
                        return True
                elif "." in ConflictStr:
                    if (ConflictStr.count(".")) > 1:
                        return False
                    else:
                        return True
                else:
                    return False
            elif "." in ConflictStr:
                if (ConflictStr.count(".")) > 1:
                    return False
                else:
                    return True

FNum, SNum, TNum, FtNum = Usr_Input()
HighestOutput, Re_01, Re_02, Re_03 = PrimaryFilter(float(FNum), float(SNum), float(TNum), float(FtNum))
SecondHighest, Re_11, Re_22 = SecondaryFilter(Re_01, Re_02, Re_03)
ThirdHighest, LowestOutput = TertiaryFilter(Re_11, Re_22)

print(f"\n\33[91m{IntorFlt(HighestOutput):,}\33[0m, \33[92m{IntorFlt(SecondHighest):,}\33[0m, \33[93m{IntorFlt(ThirdHighest):,}\33[0m, \33[94m{IntorFlt(LowestOutput):,}\33[0m".center(24," "))