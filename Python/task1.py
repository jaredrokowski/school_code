import random

def fizz_buzz(I):
    if I%3 == 0 and I%5 != 0:
        print "fizz"
    if I%3 != 0 and I%5 == 0:
        print "buzz"
    if I%3 == 0 and I%5 == 0:
        print "fizzbuzz"
    

for i in range(1,100) :
    R = random.randint(0, 10000000000000000)
    fizz_buzz(R)

    



print "ha! Peter!"