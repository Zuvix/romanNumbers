
roman_dict = {}


def set_alphabet(alphabet):
    current_value = 1
    index = 0
    global roman_dict
    for letter in alphabet:
        roman_dict[letter] = current_value
        if index % 2 == 0:
            current_value *= 5
        else:
            current_value *= 2
        index += 1
    print(roman_dict)


def find_max(alphabet):
    set_alphabet(alphabet)
    index = len(roman_dict)-1
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


print(find_max("IVXLCDM"))
