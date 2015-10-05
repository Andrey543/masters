import time
input=open('float_data.txt','r')
max=0
i=0
x=''
min=None
max=None
mini=0
maxi=0
for i in range(1000000):
    x1=input.read(1)
    if (x1==' ')or (x1=='\n'):
        y=float(x)
        #print(y)
        x=''
        if (max==None) or (y> max):
            max=y
            maxi=i
        if (min==None) or(min>y):
            min=y
            mini=i
    else:
        x+=x1
print(min,mini)
print(max,maxi)
