# A dictionary of movie critics and their ratings of a small
# set of movies
critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
 'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 3.5},
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
 'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
 'The Night Listener': 4.5, 'Superman Returns': 4.0,
 'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 2.0},
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}

from math import sqrt

## Euclidean distance between person1 & person2
def dist_euclidean(prefs,person1,person2):
	# Get the list of shared_items
	si={}
	for item in prefs[person1]:
		if item in prefs[person2]:
			 si[item]=1

	# if they have no ratings in common, return 0
	if len(si)==0: return 0

	# Add up the squares of all the differences
	sum_of_squares=sum([pow(prefs[person1][item]-prefs[person2][item],2) for item in si])

	return sqrt(sum_of_squares)

## Similarity based on Euclidean distance between person1 & person2
def sim_euclidean(prefs,person1,person2):

	return 1/(1+dist_euclidean(prefs,person1,person2))

# Returns Pearson correlation coefficient for p1 and p2 (can be used directly as similarity measure)
def sim_pearson(prefs,p1,p2):
	# Get the list of mutually rated items
	si={}
	for item in prefs[p1]:
		if item in prefs[p2]: si[item]=1
	
	# Find the number of elements
	n=len(si)
	
	# if they have no ratings in common, return 0
	if n==0: return 0
	
	# Add up all the preferences
	sum1=sum([prefs[p1][it] for it in si])
	sum2=sum([prefs[p2][it] for it in si])
	
	# Sum up the squares
	sum1Sq=sum([pow(prefs[p1][it],2) for it in si])
	sum2Sq=sum([pow(prefs[p2][it],2) for it in si])
	
	# Sum up the products
	pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])
	
	# Calculate Pearson score
	num=pSum-(sum1*sum2/n)
	den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
	if den == 0: return 0
	r=num/den
	
	return r

def sim_pearson_list(expr,orf1,orf2):
	
	# Add up all the preferences
	sum1=sum( expr[orf1] )
	sum2=sum( expr[orf2] )
	
	# Sum up the squares
	sum1Sq=sum([pow(e,2) for e in expr[orf1]])
	sum2Sq=sum([pow(e,2) for e in expr[orf2]])
	
	n = len(expr[orf1])
	
	# Sum up the products
	pSum = ( [ e1*e2 for (e1,e2) in zip(expr[orf1],expr[orf2])]  )
	
	# Calculate Pearson score
	num=pSum-(sum1*sum2/n)
	den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
	if den == 0: return 0
	r=num/den
	
	return r

# Returns distance based on Pearson correlation

def dist_pearson(prefs,p1,p2):
	
	return 1. - sim_pearson(prefs,p1,p2)


# Returns the best matches for person from the prefs dictionary.
# Number of results and similarity function are optional params.
def topMatches(prefs,person,n=5,similarity=sim_pearson):
	scores=[(similarity(prefs,person,other),other) for other in prefs if other!=person]

	# Sort the list so the highest scores appear at the top
	scores.sort()
	scores.reverse()
	return scores[0:n]
	
	
# Gets recommendations for a person by using a weighted average
# of every other user's rankings
def getRecommendations(prefs,person,similarity=sim_pearson):
	totals={}
	simSums={}
	for other in prefs:
		# don't compare me to myself
		if other==person: continue
		sim=similarity(prefs,person,other)

		# ignore scores of zero or lower
		if sim<=0: continue
		for item in prefs[other]:

			# only score movies I haven't seen yet
			if item not in prefs[person] or prefs[person][item]==0:
				# Similarity * Score
				totals.setdefault(item,0)
				totals[item] += prefs[other][item]*sim
				# Sum of similarities
				simSums.setdefault(item,0)
				simSums[item]+=sim
				
 # Create the normalized list
	rankings=[(total/simSums[item],item) for item,total in totals.items()]

	# Return the sorted list
	rankings.sort()
	rankings.reverse()
	return rankings
	
lines = open('yeastData.txt').readlines()

header = lines.pop(0)

header = header.rstrip().split('\t')
header.pop(0)
header.pop(0)

NVALS = leng(header)

expr = []
ORFs = []
for line in lines :
	tokens = line.rstrip().split('\t')
	
	orf = tokens.pop(0)
	desc = tokens.pop(0)
	
	vals = [ float(t) if t else 0. for t in tokens ]
	if len(vals) != NVALS :
		vals.append(0.)
	
	ORFs.append(orf)
	expr.append(vals)
	
from scipy.stats import pearsonr

linearDist = []

for orf1 in range(len(ORFs) - 1) :
	for orf2 in range(orf1 + 1,  len(ORFs) ) :
		r = pearsonr( expr[orf1], expr[orf2] )[0]
		d = 1. -r
		linearDists.append(d)
		




