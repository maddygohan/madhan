n=int(input())
ao=list(map(int,input().split()))
for i in range (0,n-1):
    if(ao[i]!=i+1):
        print(i)
        break
