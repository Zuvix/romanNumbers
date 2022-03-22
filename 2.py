import sys
def loadFile():
    with open('suborDat.csv') as f:
        data = f.readlines()
        return data

def check_responses_len(wantedLen,data):
    error_lines=[]
    for i in range(1,len(data)):
        if(data[i].count(';') != wantedLen):
            row = data[i].split(";")
            if row[0].isdigit():
                print("Row with id {} has invalid number of answers. We are removing it from further analysis.".format(row[0]))
            error_lines.append(i)
    
    return error_lines

def checkMissingIndexes(data):
    current_index=1
    for i in range(1,len(data)):
        row = data[i].split(";")
        if row[0].isdigit():
            if current_index!=int(row[0]):
                print("Record with index {} is missing from dataset.".format(current_index))
                current_index+=1
            current_index+=1

def checkValidData(data, startIndex, endIndex, acceptedValues):
    for i in range(1,len(data)):
        row = data[i].split(";")
        row=list(map(str.strip,row))
        for d in range(startIndex,endIndex+1):
            isValid=True
            if row[d].isdigit():
                if not(row[d] in acceptedValues):
                    isValid=False                   
            else:
                isValid=False
            if isValid==False:
                print("There is an value error in row {}, in question {} the answer \"{}\" is wrong.".format(row[0],d,row[d]))
                break
                

def validateData(data):
    checkValidData(data, 1,9,["0","1","2","3","4","5","6","7","9"])
    checkValidData(data, 10,20,["0","1","2","3","4","9"])
    checkValidData(data, 21,21,["0","1","2","3","4","5","6","7","9"])
    checkValidData(data, 22,22,["0","1","2","3","4","5","9"])
    checkValidData(data, 23,27,["0","1","2","3","4","9"])
    checkValidData(data, 28,36,["0","1","2","3","4","5","6","7","9"])


data = loadFile()
original_stdout = sys.stdout
with open('error_log.txt', 'w') as f:
    sys.stdout = f
    print("List of errors found in the dataset")
    print("Missing records:")
    checkMissingIndexes(data)
    print("")
    print("Checking if there is correct count of answers in one row:")
    error_lines=check_responses_len(36,data)
    for x in reversed(error_lines):
        data.remove(data[x])
    print("")
    print("Looking for invalid answers:")
    validateData(data)
    print("")
    sys.stdout = original_stdout