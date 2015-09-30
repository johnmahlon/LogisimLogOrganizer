file_from = raw_input("Please enter filename: ")

listOfLines = []

with open(file_from) as f:
    header = f.readline()
    for line in f:
        listOfLines.append(line)

print header


setOfLines = set(listOfLines)   # converts to a set which deletes duplicates

myList = sorted(setOfLines)     # sort

print "Understand the file you type in will be truncated."
file_to = raw_input("Please enter new filename to write to: ")

target = open(file_to, 'w')

target.write(header)
for line in myList:
    target.write(line)

