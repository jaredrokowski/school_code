#!/usr/bin/env python
import sys
from scipy import arange
try:
	first_arg = float(sys.argv[1])
	second_arg = float(sys.argv[2])
	third_arg = float(sys.argv[3])
except:
	print "You must input number 1, number 2, and step"
	sys.exit(1)


def simplefun(x, y, c):
	if y == x:
		print x
		return
	if c == 0:
		print "ivalid input!"
		return
	if x > y and c > 0:
		print "invalid input!"
		return
	if c != 0:
		total = 0
	if c > 1:
		for i in arange(x, y+1, c):
			t = abs(i)
			total += t
			print t
	else:
		for i in arange(x, y+c, c):
			t = abs(i)
			total += t
			print t
		if y < x:
			for i in arange(y, x, c):
				print i
	print total
def main():
	x = first_arg
	y = second_arg
	c = third_arg
	simplefun(x, y, c)

if __name__ == "__main__":
	main()

	#could use array for absolute value