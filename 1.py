import unittest

roman_dict = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

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
            else: 
                sum=0
    return True

def validateRomanElements(romanNumber):
    for element in romanNumber:
        if not (element in roman_dict):
            return False
    return True

def convertToInt(romanNumber):
    if validateRomanElements(romanNumber) == False:
        return -9999
    
    if checkMoreThanThree(romanNumber) == False:
        return -9999

    i = 0
    sum = 0
    prevElem = romanNumber[0]

    for element in romanNumber:
        if i == 0: 
            sum += roman_dict[element]
            i += 1
            continue

        if roman_dict[element] > roman_dict[prevElem]:
            if prevElem in ["V", "L", "D"]:
                return -9999
            if prevElem == 'I' and not (element in ['V',"X"]):
                return -9999
            if prevElem == 'X' and not (element in ['L',"C"]):
                return -9999
            if prevElem == 'C' and not (element in ['D',"M"]):
                return -9999
            sum -= 2*roman_dict[prevElem]

        sum += roman_dict[element]
        prevElem = element
        i += 1
 

    if sum > 3999:
        return -9999
    return sum


def test1():
    assert convertToInt("I") == 1, "Should be 1" #Filip
   
def test2():
    assert convertToInt("V") == 5, "Should be 5" #Samo
   
def test3():
    assert convertToInt("-I") == -9999, "Should be -9999" #Filip

def test4():
    assert convertToInt("X") == 10, "Should be 10" #Samo

def test5():
    assert convertToInt("III") == 3, "Should be 3" #Filip
   
def test6():
    assert convertToInt("MMMM") == -9999, "Should be -9999" #Samo

def test7():
    assert convertToInt("IIII") == -9999, "Should be -9999" #Filip

def test8():
    assert convertToInt("DD") == -9999, "Should be -9999" #Samo

def test9():
    assert convertToInt("IV") == 4, "Should be 4" #Filip

def test10():
    assert convertToInt("VX") == -9999, "Should be -9999" #Samo

def test11():
    assert convertToInt("LC") == -9999, "Should be -9999" #Filip

def test12():
    assert convertToInt("DM") == -9999, "Should be -9999" #Samo

def test13():
    assert convertToInt("IL") == -9999, "Should be -9999" #Filip

def test14():
    assert convertToInt("IIV") == -9999, "Should be -9999" #Samo

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