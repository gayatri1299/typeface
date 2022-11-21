strr = input()
c =0 
s = strr.split(",")
r = s[1][-2] 
for i in range(len(s[0])):
    if s[0][i] == r:
        c+=1
print(c)
