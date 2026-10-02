stringVal = input('Enter some string :')
# oddNo=stringVal[1::2]
# evenNo=stringVal[0::2]
# print('Oddnumber character :',oddNo)
# print('even number character :',evenNo)
evenNo2=''
oddNo2=''
for i in stringVal:
    if stringVal.index(i)%2!=0 :
        evenNo2=evenNo2+i
    else:
        oddNo2=oddNo2+i
print('Oddnumber character :',oddNo2)
print('even number character :',evenNo2)