import sys
import unittest
import io


def load_file(inputFile):
    with open(inputFile) as f:
        data = f.readlines()
        if data[len(data)-1] in ['\n', '\r\n']:
            data.remove(data[len(data)-1])
        return data


def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()


# We uses this function to load output file for testing in a single string.
def load_output_string(outputFile):
    with open(outputFile, 'r') as file:
        output = file.read()
        return output


# This function chcecks if there is correct count of answers in every row.
def check_responses_len(data):
    error_lines = []
    wantedLen = data[0].count(';')
    for i in range(1, len(data)):
        if(data[i].count(';') != wantedLen):
            row = data[i].split(";")
            if is_integer(row[0]):
                print(
                    "Row with id {} has invalid number of answers. We are removing it from further analysis.".format(row[0]))
            else:
                print(
                    "There is a row without correct index and with missing records.")
            error_lines.append(i)

    return error_lines


# We check if there are correct indexes
def chech_indexes_errors(data):
    used_indexes = {}

    for i in range(1, len(data)):
        used_indexes[i] = 0
    for i in range(1, len(data)):
        row = data[i].split(";")
        if is_integer(row[0]):
            index = int(row[0])
            if index < 0:
                print("There is a record with negative index \"{}\".".format(index))
                continue
            if index >= len(data):
                print("There is a record with index out of bounds \"{}\".".format(index))
                continue
            used_indexes[index] += 1
        else:
            print("There is a record with non-integer index \"{}\".".format(
                row[0]))
    for i in range(1, len(data)):
        if(used_indexes[i] < 1):
            print("Index {} is missing from file.".format(i))
        elif used_indexes[i] > 1:
            print("Index {} has multiple occurences.".format(i))


# We chceck if the answers are within correct interval.
def check_valid_data(data, startIndex, endIndex, acceptedValues):
    for i in range(1, len(data)):
        row = data[i].split(";")
        row = list(map(str.strip, row))
        for d in range(startIndex, endIndex+1):
            isValid = True
            if row[d].isdigit():
                if not(row[d] in acceptedValues):
                    isValid = False
            else:
                isValid = False
            if isValid == False:
                print("There is an value error in row {}, in question {} the answer \"{}\" is wrong.".format(
                    row[0], d, row[d]))
                break


# We call previous function specifically for this dataset
def validate_data(data):
    check_valid_data(data, 1, 9, ["0", "1", "2", "3", "4", "5", "6", "7", "9"])
    check_valid_data(data, 10, 20, ["0", "1", "2", "3", "4", "9"])
    check_valid_data(
        data, 21, 21, ["0", "1", "2", "3", "4", "5", "6", "7", "9"])
    check_valid_data(data, 22, 22, ["0", "1", "2", "3", "4", "5", "9"])
    check_valid_data(data, 23, 27, ["0", "1", "2", "3", "4", "9"])
    check_valid_data(
        data, 28, 36, ["0", "1", "2", "3", "4", "5", "6", "7", "9"])


# The main section for error logging
data = load_file('suborDat.csv')
original_stdout = sys.stdout
with open('error_log.txt', 'w') as f:
    sys.stdout = f
    print("List of errors found in the dataset")
    print("Missing records:")
    chech_indexes_errors(data)
    print("")
    print("Checking if there is correct count of answers in one row:")
    error_lines = check_responses_len(data)
    for x in reversed(error_lines):
        data.remove(data[x])
    print("")
    print("Looking for invalid answers:")
    validate_data(data)
    print("")
    sys.stdout = original_stdout


# Testing section
class TestQuizDataMethods(unittest.TestCase):

    def setUp(self):
        self.capturedOutput = io.StringIO()
        sys.stdout = self.capturedOutput

    def reset(self):
        self.capturedOutput.truncate(0)
        self.capturedOutput.seek(0)

    # We test if the setup is working
    def test_setup(self):
        print("Hello")
        self.assertEqual(self.capturedOutput.getvalue(), 'Hello\n')
        self.reset()

    def test_indexes_correction(self):
        input = load_file("test1_input.txt")
        output = load_output_string("test1_output.txt")
        chech_indexes_errors(input)
        self.assertEqual(self.capturedOutput.getvalue(), output)
        self.reset()

    def test_data_row_len(self):
        input = load_file("test2_input.txt")
        output = load_output_string("test2_output.txt")
        check_responses_len(input)
        self.assertEqual(self.capturedOutput.getvalue(), output)
        self.reset()

    def test_validate_data(self):
        input = load_file("test3_input.txt")
        output = load_output_string("test3_output.txt")
        self.maxDiff = None
        validate_data(input)
        self.assertEqual(self.capturedOutput.getvalue(), output)
        self.reset()


# Run tests
if __name__ == '__main__':
    unittest.main()
