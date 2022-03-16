def loadFile():
    with open('suborDat.csv') as f:
        data = f.readlines()
        return data

def check_responses_count(wantedCount):
    error_lines=[]
    for i in range(1,len(data)):
        if(data[i].count(';') != wantedCount):
            print(data[i])
            error_lines.append(i)
    
    return error_lines

data = loadFile()
print(len(data))
error_lines=check_responses_count(36)
for x in reversed(error_lines):
    data.remove(data[x])
print(len(data))

