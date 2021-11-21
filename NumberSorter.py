# Program 1: Number Sorter
# Create a program that ask 4 numbers. 
# Print the 4 numbers from highest to lowest using only if-else statement.

def Usr_Input():
    Num_01 = int(input("Enter first number: "))
    Num_02 = int(input("Enter second number: "))
    Num_03 = int(input("Enter third number: "))
    Num_04 = int(input("Enter fourth number: "))
    return Num_01, Num_02, Num_03, Num_04

def PrimaryFilter(firstNum, secondNum, thirdNum, fourthNum):
    if (firstNum > secondNum) and (firstNum > thirdNum) and (firstNum > fourthNum):
        return firstNum, secondNum, thirdNum, fourthNum
    elif (secondNum > firstNum) and (secondNum > thirdNum) and (secondNum > fourthNum):
        return secondNum, firstNum, thirdNum, fourthNum
    elif (thirdNum > firstNum) and (thirdNum > secondNum) and (thirdNum > fourthNum):
        return thirdNum, firstNum, secondNum, fourthNum
    elif (fourthNum > firstNum) and (fourthNum > secondNum) and (fourthNum > thirdNum):
        return fourthNum, firstNum, secondNum, thirdNum
    else:
        print() #Insert conditions for secondary screening of inputs.

def SecondaryFilter(Remain_01, Remain_02, Remain_03):
    if (Remain_01 > Remain_02) and (Remain_01 > Remain_03):
        return Remain_01, Remain_02, Remain_03
    elif (Remain_02 > Remain_01) and (Remain_02 > Remain_03):
        return Remain_02, Remain_01, Remain_03
    elif (Remain_03 > Remain_01) and (Remain_03 > Remain_02):
        return Remain_03, Remain_01, Remain_02

FNum, SNum, TNum, FtNum = Usr_Input()
HighestOutput, Re_01, Re_02, Re_03 = PrimaryFilter(FNum, SNum, TNum, FtNum)
SecondHighest, Re_11, Re_22 = SecondaryFilter(Re_01, Re_02, Re_03)

FirstTwoHigh = HighestOutput, SecondHighest
print(FirstTwoHigh)