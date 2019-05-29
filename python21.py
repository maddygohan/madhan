n,a,d=map(int,input().split())
s=0
for i in range(n):
    s=s+a
    a=a+d
    i+=1
print(s)
