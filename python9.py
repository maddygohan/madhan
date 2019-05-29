a,b=input("").split()
a=int(a)
b=int(b)
s=0
for i in range(1,a+1):
    print(i,end=' ')
for j in range(0,b+1):
    s=s+j
print('\n',s)
