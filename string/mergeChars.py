#input : a= 'shiva'  b='ash'
#output: sahshiva

stringVal=input('Enter two String values :')
stringVals=stringVal.split()
tlist1=list(stringVals[0])
tlist2=list(stringVals[1])
print(len(tlist1) ,len(tlist2))
i,j=0,0
output=''
while i<=len(tlist1) or j<len(tlist2):
    output=output+tlist1[i]+tlist2[j]
    i+=1
    j+=1
print(output)

