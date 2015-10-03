from random import *
output=open('int.data.txt','w')
for i in range(1,1000000):
    print(randint(1,100),end=' ',file=output)