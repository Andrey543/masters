a = list(map(int, input().split()))
for i in range(int(input())):
   a[a[len(a)-1]],a[a[len(a)-1]+1:]=a[len(a)-1],a[a[len(a)-1]:len(a)-1]
   print(len(a),a[len(a)-1],len(a)-1)
   print(a)