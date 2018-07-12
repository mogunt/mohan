n=int(input())
s=input()
s=s.split()
s.sort()
t="".join(s)
t=t[::-1]
print(t)
