# method -1
s='krish'
print(s[: :-1])
# method 2
rev="".join(reversed(s))
print(rev)

# method 3
rev1=""
for ch in s:
    rev1=ch+rev1
print(rev1)    

