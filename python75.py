St=list(input())
mid=len(St)//2
if len(St)%2==0:
    St[mid]='*'
    St[mid-1]='*'
else:
    St[mid]='*'
for i in St:
    print(i,end='')
