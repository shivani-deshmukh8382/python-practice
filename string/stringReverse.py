# val1 = input('Enter any string value : ')
# reversedString = val1[::-1]
# print(reversedString)

val=input('Enter any string : ')
print(''.join(reversed(val)))

val2=input('Enter some String :')#shivani
stringLength = len(val2)#7
target=''
i = stringLength-1
while i>=0:
    target = target+val2[i]
    i = i-1
print(target)




