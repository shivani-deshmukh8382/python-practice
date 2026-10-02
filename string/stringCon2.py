string = input('Enter any String vslue...  : ')
n = 'is' in string
print(n)
d= {}
for i in string:
    if i in d:
        d[i]=d.values()+1
    else:
        d[i]=1
    