n=int(input())
s=input()
s=s.split()
l=[]
for i in range(0,n):
    if(i==int(s[i])):
        l.append(int(s[i]))
l.sort()
if(len(l)==0):
    print("-1")
else:
    for i in range(0,len(l)):
        if(i!=len(l)-1):
            print(l[i],end=" ")
        else:
            print(l[i])
