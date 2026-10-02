#input = b3h4uj
#output = bjhu34

stringVal = input('Enter any string value : ')
output=''
if stringVal.isalnum():
    l=list(stringVal)
    i = 0
    alpha=''
    num=''
    while i<len(l):
        if l[i].isalpha():
            alpha=alpha+l[i]
        else:
            num = num+l[i]
        i+=1
    output=''.join(sorted(alpha))+''.join(sorted(num))
print(output)