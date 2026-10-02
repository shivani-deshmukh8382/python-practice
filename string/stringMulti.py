#input=a4b3c2
#output=aaaabbbcc

val=input('Enter any string value : ')
previous=''
output=''
if val.isalnum():
    for i in val:
        if i.isalpha():
            previous=i
        else:
            output=output+previous*int(i)
print(output)

