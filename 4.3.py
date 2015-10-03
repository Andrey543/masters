a=input().split()
while len(a)>0:
    if a.count(a[0])==1:
        print(a.pop(0), end=' ')
    else:
        s=a[0]
        while a.count(s)>0:
            s=a.pop(a.index(s))
        
        
        
