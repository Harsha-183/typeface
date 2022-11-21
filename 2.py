a=input()
b=input()
c=b[len(b)-1]
count=0
for i in a:
    if i==c:
        count+=1
print(count)
