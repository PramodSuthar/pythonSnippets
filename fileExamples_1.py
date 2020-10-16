def sequanceFilter(line):
    return '>' not in line

with open('./file_2.txt') as readFile:
    lines = readFile.readlines()
    print(list(filter(sequanceFilter, lines)))
    
