s=input()
from itertools import combinations
l=[]
l.append(s[0])
for i in range(1,len(s)):
    if s[i]!=s[i-1]and s[i] not in l:
        l.append(s[i])
print(len(l))   

