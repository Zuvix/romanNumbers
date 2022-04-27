import RomanToNumberConverter as roman


def maxNumberFromRomanLetters(alphabet):
    index = len(alphabet)-1
    final_sequence = ""
    while(index >= 0):
        if index % 2 == 0:
            if alphabet[index] not in final_sequence:
                final_sequence += alphabet[index]*3
            if index > 0:
                if index-2 >= 0:
                    final_sequence += alphabet[index-2]
                    final_sequence += alphabet[index]
                    index = index-2
                elif index-1 >= 0:
                    final_sequence += alphabet[index-1]
                    return final_sequence
            else:
                return final_sequence
        if index % 2 == 1:
            final_sequence += alphabet[index]
            index -= 1

