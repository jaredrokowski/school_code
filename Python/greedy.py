import random
from Tkconstants import CURRENT

G = [[(-5+i, -5+j) for i in range(0,11)] for j in  range(0,11)]

def Func(i,j) :
    x = -5 + i 
    y = -5 + j
    return x**3 - 27*x + y**3 - 12*y
F = []

for j in range(0,11):
    F.append([])
    for i in range(0,11):
        F[-1].append(Func(i,j))

Current_Pos = ()

x = random.randint(0, 11)
y = random.randint(0, 11)


print G
print F


def move(pos):  
    if pos > Func(x+1,y):
        pos = Func(x+1,y)  
        return pos  
    else :
        if pos > Func(x,y+1):
            pos = Func(x,y+1)
            return pos
        else :
            if pos > Func(x-1,y):
                Current_Pos = Func(x-1,y)
                return pos
            else:
                if pos > Func(x,y-1):
                    Current_Pos = Func(x,y-1)
                    return pos

while True:        
    Current_Pos = Func(x,y)
    while True:
        move(Current_Pos)
        print Current_Pos
        
    break