#input= 'my name is shivani'
#output='ym eman si inavihs'

val =input('Enter one line of String : ')
tList=val.split()#list is splitted into multiple string values
tList2=[]
for i in tList:#here one string value
    stringVal=list(i)#string is converted into list of string characters
    stringLength=len(stringVal)-1
    lp=''
    while stringLength>=0:#characters are itereted one by one from left to right
        lp=lp+stringVal[stringLength]#create one empty string and append
                                    #characters from last index to 0th index
                                    #and join to that empty string so hat we can get reversed
                                    #String 
        stringLength-=1
    tList2.append(lp)#created one empty list value and append reversed string
                    #empty list value
print(' '.join(tList2))

    
        
    