n=int(input())
s=input()
s=s.split()
l=[]
for i in range(0,len(s)):
    s[i]=int(s[i])
t=set(s)
for i in t:
    c=s.count(i)
    if(c>1):
        l.append(i)
if(len(l)==0):
        print("Unique")
else:
    l.sort()
    if(len(l)!=1):
        for y in l:
            print(y,end=" ")
    else:
        print(l[0])
