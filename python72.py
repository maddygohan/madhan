st=input()
c=0
vow=['a','e','i','o','u','A','E','I','O','U']
for i in st:
    if i in vow:
        c+=1
        break
if(c>0):
    print("yes")
else:
    print("no")
        
        
