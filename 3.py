

valid=[0,1,2,5,6,8,9]

def check(k):
    k=str(k)
    for i in k:
        if int(i) not in valid:
            return False
    return True

n = int(input())
if n < len(valid):
    print(valid[n-1])
else:
    count=len(valid)
    k=valid[-1]
    while(count<=n):
        k+=1
        if check(k):
            count+=1
    print(k)
