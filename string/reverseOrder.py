#input='my name is shivani'
#output='shivani is name my'

input= input('Enter one line of string : ')
list = input.split(' ')
print(list)
tList=[]
i = len(list)-1
while i>=0:
    tList.append(list[i])
    i = i-1
print(tList)
print(' '.join(tList))

targetList = ' '.join(reversed(list))
print(targetList)