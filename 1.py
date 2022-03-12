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

def convertToInt(romanNumber):
    sum = 0
    for element in romanNumber:
        if element in roman_dict:
            sum += roman_dict[element]
        else: 
            return -9999
    
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

test1()
test2()
test3()
test4()
test5()
test6()
test7() 