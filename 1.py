import unittest
# MADE by Filip Novak and Samuel Kubala
# WINNER -> Filip Novak

roman_dict = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

#Function to check if there is a forbidden repetition of characters or bad count of characters
def checkMoreThanThree(romanNumber):
    key_list = list(roman_dict.keys())

    for x in range(len(key_list)):
        sum = 0
        maxSum = 1

        if x%2 == 0:
            maxSum = 3

        for element in romanNumber:
            if element == key_list[x]:
                sum += 1

                if sum > maxSum:
                    return False
    return True

#Check for invalid characters
def validateRomanElements(romanNumber):
    for element in romanNumber:
        if not (element in roman_dict):
            return False
    return True

#Check if number is in correct order
def correctNumberOrder(element, max, usedNumbers_list):
    for item in usedNumbers_list:
        if roman_dict[element] >= roman_dict[item]:
            return False
        
    if max == "I" and (element in ["L","C","D","M"]):
        return False
    if max == "V" and (element in ["X","L","C","D","M"]):
        return False
    if max == "X" and (element in ["D","M"]):
        return False
    if max == "L" and (element in ["C","D","M"]):
        return False
    if max == "D" and element == "M":
        return False
    
    return True

#Main function to convert roman to INT
def convertToInt(romanNumber):
    romanNumber = romanNumber.strip() # remove leading and trailing whitespaces

    if len(romanNumber) == 0:
        return -9999

    if validateRomanElements(romanNumber) == False:
        return -9999
    
    if checkMoreThanThree(romanNumber) == False:
        return -9999

    i = 0
    sum = 0
    max = None
    repetition = False
    usedNumbers_list = []
    prevElem = romanNumber[0]

    for element in romanNumber:
        if i == 0: 
            sum += roman_dict[element]
            max = element
            i += 1
            continue

        if correctNumberOrder(element, max, usedNumbers_list) == False:
            return -9999      

        if roman_dict[prevElem] < roman_dict[element]:
            if prevElem in ["V", "L", "D"]:
                return -9999
            if prevElem == "I" and not (element in ["V","X"]):
                return -9999
            if prevElem == "X" and not (element in ["L","C"]):
                return -9999
            if prevElem == "C" and not (element in ["D","M"]):
                return -9999
            if repetition:
                return -9999

            if roman_dict[max] < roman_dict[element]:
                max = element

            usedNumbers_list.extend([prevElem, element])
            sum -= 2 * roman_dict[prevElem]

        elif prevElem == element:
            repetition = True
        elif (roman_dict[prevElem] > roman_dict[element]) and repetition:
            repetition = False

        sum += roman_dict[element]
        prevElem = element
 
    if sum > 3999:
        return -9999
    return sum


#TEST FUNCTIONS
def test1():
    assert convertToInt("I") == 1, "Test1, should be 1"
   
def test2():
    assert convertToInt("V") == 5, "Test2, should be 5"
   
def test3():
    assert convertToInt("-I") == -9999, "Test3, should be -9999"

def test4():
    assert convertToInt("X") == 10, "Test4, should be 10"

def test5():
    assert convertToInt("III") == 3, "Test5, should be 3"
   
def test6():
    assert convertToInt("MMMM") == -9999, "Test6, should be -9999"

def test7():
    assert convertToInt("IIII") == -9999, "Test7, should be -9999"

def test8():
    assert convertToInt("DD") == -9999, "Test8, should be -9999"

def test9():
    assert convertToInt("IV") == 4, "Test9, should be 4"

def test10():
    assert convertToInt("VX") == -9999, "Test10, should be -9999"

def test11():
    assert convertToInt("LC") == -9999, "Test11, should be -9999"

def test12():
    assert convertToInt("DM") == -9999, "Test12, should be -9999"

def test13():
    assert convertToInt("IL") == -9999, "Test13, should be -9999"

def test14():
    assert convertToInt("IIV") == -9999, "Test14, should be -9999"

def test15():
    assert convertToInt("MXXXIV") == 1034, "Test15, should be 1034"

def test16():
    assert convertToInt("MCMLXXXVIII") == 1988, "Test16, should be 1988"

def test17():
    assert convertToInt("") == -9999, "Test17, should be -9999" 

def test18():
    assert convertToInt("  CXIX ") == 119, "Test18, should be 119"

def test19():
    assert convertToInt("CMCM") == -9999, "Test19, should be -9999"

def test20():
    assert convertToInt("CMM") == -9999, "Test20, should be -9999"

def test21():
    assert convertToInt("DCM") == -9999, "Test21, should be -9999"

#RUN TESTS
test1()
test2()
test3()
test4()
test5()
test6()
test7()
test8()
test9()
test10()
test11()
test12()
test13()
test14()
test15()
test16()
test17()
test18()
test19()
test20()
test21()