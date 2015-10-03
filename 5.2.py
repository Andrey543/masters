import math
from random import *
output=open('float_data.txt','w')
for i in range(1000000):
    print(math.trunc(random()*10000)/100,end=' ',file=output)