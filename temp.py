import numpy as np
def t(l):
    l=np.array(l)
    l[0]=0
    print(l)
l=[1,2,3]
l=np.array(l)
t(l)
print(l)