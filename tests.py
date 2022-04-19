import RomanConverter as roman
# TEST FUNCTIONS


def test1():
    assert roman.convert_to_int("I") == 1, "Test1, should be 1"


def test2():
    assert roman.convert_to_int("V") == 5, "Test2, should be 5"


def test3():
    assert roman.convert_to_int("-I") == -9999, "Test3, should be -9999"


def test4():
    assert roman.convert_to_int("X") == 10, "Test4, should be 10"


def test5():
    assert roman.convert_to_int("III") == 3, "Test5, should be 3"


def test6():
    assert roman.convert_to_int("MMMM") == -9999, "Test6, should be -9999"


def test7():
    assert roman.convert_to_int("IIII") == -9999, "Test7, should be -9999"


def test8():
    assert roman.convert_to_int("DD") == -9999, "Test8, should be -9999"


def test9():
    assert roman.convert_to_int("IV") == 4, "Test9, should be 4"


def test10():
    assert roman.convert_to_int("VX") == -9999, "Test10, should be -9999"


def test11():
    assert roman.convert_to_int("LC") == -9999, "Test11, should be -9999"


def test12():
    assert roman.convert_to_int("DM") == -9999, "Test12, should be -9999"


def test13():
    assert roman.convert_to_int("IL") == -9999, "Test13, should be -9999"


def test14():
    assert roman.convert_to_int("IIV") == -9999, "Test14, should be -9999"


def test15():
    assert roman.convert_to_int("MXXXIV") == 1034, "Test15, should be 1034"


def test16():
    assert roman.convert_to_int(
        "MCMLXXXVIII") == 1988, "Test16, should be 1988"


def test17():
    assert roman.convert_to_int("") == -9999, "Test17, should be -9999"


def test18():
    assert roman.convert_to_int("  CXIX ") == 119, "Test18, should be 119"


def test19():
    assert roman.convert_to_int("CMCM") == -9999, "Test19, should be -9999"


def test20():
    assert roman.convert_to_int("CMM") == -9999, "Test20, should be -9999"


def test21():
    assert roman.convert_to_int("DCM") == -9999, "Test21, should be -9999"


def test22():
    assert roman.convert_to_int("XCIX") == 99, "Test22, should be 99"


def test23():
    assert roman.convert_to_int("MMMCM") == 3900, "Test23 should be 3900"


def test24():
    assert roman.convert_to_int("CDC") == -9999, "Test24 should be -9999"


def test25():
    assert roman.convert_to_int("IXIV") == -9999, "Test25 should be -9999"


def test26():
    assert roman.convert_to_int("XXXVIX") == -9999, "Test26 should be -9999"


def test27():
    assert roman.convert_to_int("DCD") == -9999, "Test27 should be -9999"


def test28():
    assert roman.convert_to_int(None) == -9999, "Test28 should be -9999"


# RUN TESTS
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
test22()
test23()
test24()
test25()
test26()
test27()
test28()
