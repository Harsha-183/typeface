def base(n):
    b=3
    if n==0:
        return(0)
    a=[]
    while n:
        n,r=divmod(n,b)
        a.append(str(r))
    return ''.join(reversed(a))
n=int(input())
print(base(n))
    
