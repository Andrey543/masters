input=open('float_data.txt','r')
sum=0
k=0
sumkv=0
x=''
for i in range(1000000):
    x1=input.read(1)
    if (x1==' ')or (x1=='\n'):
        y=float(x)
        #print(y)
        x=''
        sum+=y
        sumkv+=y**2
    else:
        x+=x1
sum=sum/1000000
sumkv=(sumkv/1000000)**0.5
print(sum)
print((2*sumkv**2-2*sumkv*sum)**0.5)