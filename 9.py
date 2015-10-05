a=input().split()
a[::2],a[1::2]=a[:len(a)//2+len(a)%2],a[len(a)//2+len(a)%2:][::-1]
print(a)

