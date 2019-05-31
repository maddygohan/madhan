n1,n2=map(int,input("").split())
n1=n1 ^ n2
n2=n1 ^ n2
n1=n1 ^ n2
print(n1,n2)
