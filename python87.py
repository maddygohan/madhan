N,M=map(int,input().split())
i=1
while(i<=N and i<=M):
    if(N%i==0 and M%i==0):
        gcd=i
    i+=1
print(gcd)
