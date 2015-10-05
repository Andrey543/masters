input=open('int_data.txt','r')
x=''
k=0
a=[0]*101
for i in range(1000000):
    x1=input.read(1)
    if (x1==' ')or (x1=='\n'):
        y=int(x)
        a[y]+=1
        #print(y)
        x=''
    else:
        x+=x1
for i in range(1,101):
    print(i,'-',a[i])
    if a[i]!=0:
        k+=1
print('Most valuable number:',a.index(max(a)))
print('List valuable number:',a.index(min(a[1::])))
print('This is',k,'different number in this file.')