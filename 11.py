k,n=int(input()),int(input())
a=[1]*k
for i in range(n-k+1):
   a[:len(a)-1],a[len(a)-1]=a[1:],sum(a)
print(a[k-1])