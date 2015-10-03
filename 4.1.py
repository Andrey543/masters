a=input().split()
a[:len(a)-1:2],a[1::2]=a[1::2],a[:len(a)-1:2]
print(' '.join(a))