n=int(input(""))
a=0
b=1
for i  in range(n):
    c=a+b
    a=b
    print(b,end=' ')
    b=c
