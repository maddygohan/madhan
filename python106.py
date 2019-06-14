N,k=map(int,input().split())
n=list(map(int,input().split()))
li=[]
for i in n:
    if(i%2!=0):
        li.append(i)
print(li[k-1])
