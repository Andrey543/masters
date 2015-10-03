a=input().split()
max=None
for i in range(len(a)):
     if max==None or max<int(a.count(a[i])):
        max=a.count(a[i])
        d=a[i]
print(d)

