# Program 1: Number Sorter
# Create a program that ask 4 numbers. 
# Print the 4 numbers from highest to lowest using only if-else statement.

def Usr_Input(): #Input Function
    while True:
        Num_01 = input("Enter \x1B[1mfirst\x1B[0m number: ")
        Ev_Num_01= CommaReader_Single(Num_01)
        if (Ev_Num_01.replace(".","",1).replace("-","",1).isdecimal()) == True: #Initial Screening
            Num_02 = input("Enter \x1B[1msecond\x1B[0m number: ")
            Ev_Num_02= CommaReader_Single(Num_02)
            if Ev_Num_02.replace(".","",1).replace("-","",1).isdecimal() == True:
                Num_03 = input("Enter \x1B[1mthird\x1B[0m number: ")
                Ev_Num_03= CommaReader_Single(Num_03)
                if Ev_Num_03.replace(".","",1).replace("-","",1).isdecimal() == True:
                    Num_04 = input("Enter \x1B[1mfourth\x1B[0m number: ")
                    Ev_Num_04= CommaReader_Single(Num_04)
                    if Ev_Num_04.replace(".","",1).replace("-","",1).isdecimal() == True:
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
    elif StrEvaluee.isalnum() == True:
        return print("Input must be all numeric character!")
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

FNum, SNum, TNum, FtNum = Usr_Input()
HighestOutput, Re_01, Re_02, Re_03 = PrimaryFilter(float(FNum), float(SNum), float(TNum), float(FtNum))
SecondHighest, Re_11, Re_22 = SecondaryFilter(Re_01, Re_02, Re_03)
ThirdHighest, LowestOutput = TertiaryFilter(Re_11, Re_22)

print(f"\n{IntorFlt(HighestOutput)}, {IntorFlt(SecondHighest)}, {IntorFlt(ThirdHighest)}, {IntorFlt(LowestOutput)}")