n1,s,n2=input().split()
n1=int(n1)
n2=int(n2)
if(s=='/'):
    ans=n1//n2
else:
    ans=n1%n2
print(ans)
