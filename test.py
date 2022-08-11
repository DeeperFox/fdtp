s=(('123',),('123',))

a=list(s)
j=0
for i in a:
    a[j] = list(i)
    j+=1
print(a[0][0])

l=[]
l.append(a)
print(l)

