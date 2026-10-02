#Remove duplicate characters from the String
stringval = input('Enter any string value :  ')
stringval2 = ''
for i in stringval:
    if i not in stringval2:
        stringval2+=i
print(stringval2)