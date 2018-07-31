HRCost = []

for ((HSet,HCost),(RSet,RCost)) in zip(HAsSetWithCost,RAsSetWithCost) :
	if len(HSet.intersect(RSet)) > 0 :
		HRCost.append( (HSet.intersect(RSet),HCost+RCost) )
	else :
		HRCost.append( (HSet.union(RSet), HCost+RCost+1) )
	
def TreeCost(node, sequences) :
#Taking the node and the sequence as an argument for this recursive function
	if not node.left :
#First thing to do is to create your termination event
		return [ (set(c),0) for c in sequences[node.label] ]
	else :
		nodeCost = []
		
		for ((LSet,LCost),(RSet,RCost)) in zip(TreeCost(node.left, sequences),TreeCost(node.right, sequences) ) :
			if len(LSet.intersect(RSet)) > 0 :
				nodeCost.append( (LSet.intersect(RSet),LCost+RCost) )
			else :
				nodeCost.append( (LSet.union(RSet), LCost+RCost+1) )
		
		return nodeCost


def fitch(node, sequences) :
	finalCosts = treeCost(node, sequences)
	
	cost = sum( [ c for (s,c) in finalCosts ] )
	
	return cost