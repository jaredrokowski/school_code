
## To generate all the words in the ktuple lexicon, mainly for testing

alphabet = 'AMN...'

lexicon = []

for c1 in alphabet:
	for c2 in alphabet:
		for c3 in alphabet :
			word = c1 + c2 + c3
				lexicon.append(word)

lexiset = set(lexicon)

ktupledict (already defined)

ktupleset = set(ktupledict.keys())

ktupleset - lexiset

######################################################


### Here is one approach to generating the raw sequence data in preparation for further processing
### Assume that all the 'topdomains' data has been imported to the list 'lines'. Data for each domain is exported to 
### a pair of files in the pre-created 'domains' directory, one holds just the accession numbers (for ease of use in
### pulling the fasta data from uniprot), the other holds the entire #=GS lines (so that the sequence range data is preserved)

currentDomain = None
fACCONLY = None
fALL = None

for line in lines :
	if line.startswith('#=GF ID') :
		if fACCONLY :
			fACCONLY.close()
			fALL.close()
		currentDomain = line.rstrip().split()[2]
		fACCONLY = open('domains/' + currentDomain + '_ACCONLY.txt', 'w' )
		fALL = open('domains/' + currentDomain + '_ALL.txt', 'w' )
	elif line.startswith('#=GS') :
		tokens = line.rstrip().split()
		if tokens[2] != 'AC' : continue
		acc = tokens[3].split('.')[0]
		fACCONLY.write(acc + '\n')
		fALL.write( line )

######################################################

##### Following is pulled from interactive session in class, using the file-based approach above

>>> files = glob.glob('domains/*txt')

>>> domainnames = []
>>> for f in files :
...     s = re.search(r'domains/(.+)_ACCONLY.txt', f )
...     if not s : continue
...     domainnames.append(s.group(1))
... 
>>> len(domainnames)
99

domain = 'Thioredoxin'

>>> domain
'Thioredoxin'
>>> 
>>> ## Accession number to full sequence 
>>> accToSeq = {}
>>> lines = open('thioredoxin.fa').readlines()
>>> 
>>> for line in lines :
...     if line.startswith('>') :
...             acc = line.split('|')[1]
...             accToSeq[acc] = ''
...     else :
...             accToSeq[acc] += line.rstrip()

>>> thioredoxinSeqs = []
>>> 
>>> lines = open('domains/Thioredoxin_ALL.txt').readlines()
>>> ## Sequences to extacted ranges (actually contain domain representative)
for line in lines :
	s = re.search( r'^#=GS\s+([^_]+)_.+\/([0-9]+)\-([0-9]+)\s', line )
	if not s : continue
	acc = s.group(1)
	start = s.group(2)
	end = s.group(3)
	if acc not in accToSeq : continue
	seq = accToSeq[acc]
	start = int(start) - 1
	end = int(end) - 1
	extract = seq[start:end+1]
	thioredoxinSeqs.append(extract)

alphabet = 'ARNDCQEGHILKMFPSTWYV'

### One way to get raw data for the document vector, just record counts of all k-tuples that occur
### SIZE is the k-tuple/word size we are using

>>> seqTupleCounts = []
>>> 
for seq in thioredoxinSeqs :
	tupleCounts = {}
	for k in range(len(seq)-SIZE+1) :
		tuple = seq[k:k+SIZE]
		if tuple in tupleCounts :
			tupleCounts[tuple] += 1
		else :
			tupleCounts[tuple] = 1
	seqTupleCounts.append(tupleCounts)

### Here is maybe a better approach - assign each possible tuple a distinct index, 0 through (len(alphabet)**SIZE - 1)
def tupleToNumber( tuple, alphabet ) :
	num = 0
	for k in range(len(tuple)) :
		if tuple[k] not in alphabet :
			## check for 'illegal' symbol (i.e. wildcard)
			return -1
		num += alphabet.index(tuple[k]) * len(alphabet)**k
	return num

### Here is machinery to efficiently retain our 'document vectors'
from scipy.sparse import dok_matrix

def sequencesToVectors( seqs, alphabet, SIZE ) :
	lexisize = (len(alphabet))**SIZE
	VECTORS = dok_matrix((len(seqs),lexisize))
	
	## Each row is one training/validation example, corresponding to one sequence extract ('document')
	for row in range(len(seqs)) :
		tuples = [ seq[k:k+SIZE]  for k in range(0,len(seq)-SIZE+1) ]
		
		indices = [  tupleToNumber( t, alphabet )  for t in tuples  if tupleToNumber( t, alphabet ) > 0 ]
		
		for index in indices :
			if VECTORS.has_key((row,index)) :
				VECTORS[row,index] += 1
			else :
				VECTORS[row,index] = 1
	
	return VECTORS
	
