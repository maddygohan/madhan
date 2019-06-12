nr=int(input())
re=0
while(nr!=0):
    rem=nr%10
    re=re*10+rem
    nr//=10
print(re)
    
