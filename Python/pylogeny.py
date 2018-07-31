import random
#becuase we need it later

class Node(object) :
	def __init__( self, label ) :
	#self refers to self and is required to allow definition of any extra stuff
		self.left = None
		self.right = None
		
		self.label = label
		
	def addChildren( self, l, r ) :
		self.left = l
		self.right = r
	def __str__( self ) :
		s = 'node:%d' % self.label
		if self.left : 
			s += '\nChildren: %d , %d' % (self.left.label, self.right.label)
		else :
			s += '\nLeaf node'
		return s

#root = Node(-4)

#root.addChildren( Node(-3), Node(-2) )

#root.left.addChildren( Node(-1), Node(2) )
#root.right.addChildren( Node(3), Node(4) )

#root.left.left.addChildren( Node(0), Node(1) )
#above is a manual construction that we wouldn't do in real life

#Here we manually ittereated

#def randomTree(numeLeaves) :
	#for this example we only need the  number of leaf nodes
	#nodes = [ Node(x) for x in range(numLeaves)]
	#the Nodes are leaf nodes because they do not have lefts or rights described
	#also the Node((i,)) is a tuple so that we can group them in the next step at ancestor
	#since python likes to 
	#while len(nodes) > 1 :
	#	j,k = sorted(random.sample( range(len(nodes)), 2 ))
	#	ancestor = Node((nodes[j].label, nodes[k].label))
		
	#	del nodes[k]
	#	del nodes[j]
		#important to delete the node further down because the list will change and the indecise will be wrong
		
	#	nodes.append(ancestor)
	#return nodes[0] 

#Here we created random Trees
from math import factorial

def numTrees(N) :
	return factorial(2*N - 3)/((2**(N-2)) * factorial(N-2))
	
#Here we create every single possible Tree