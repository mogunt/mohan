# your code goes here
n,k=input().split()
s=input().split()
s=list(map(int,s))
s.sort(reverse=True)
print(s[int(k)-1])
