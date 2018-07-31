import glob
#look up how to grab all files of ending .concise
import random
files = glob.glob('*.concise')

TRAINING = open('training.txt','w')
VALIDATION = open('validation.txt','w')
#This is a new file that will write these as examples
#later we will use some as training and other as validation
#JK actually did it now LOL
SIZE = 11
#Odd is good because it will have the same pixles on both sides

codeToVector = {
	'A':'1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
	'C':'0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
	'D':'0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
	'E':'0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
	'F':'0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
	'G':'0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
	'H':'0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0',
	'I':'0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0',
	'K':'0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0',
	'L':'0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0',
	'M':'0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0',
	'N':'0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0',
	'P':'0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0',
	'Q':'0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0',
	'R':'0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0',
	'S':'0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0',
	'T':'0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0',
	'V':'0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0',
	'W':'0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0',
	'Y':'0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1'
}
#Building our code in as vectors, hardwired way

labels = { 'H':'1,0,0', 'E':'0,1,0', '-':'0,0,1'}

for f in files :
	
	##read file data (list of lines)
	
	lines = open(f).readlines()
	#gotta open the files to get anything from them
	
	## Get DSSP and Origseq lines
	sequence = None 
	dssp = None
	#this is just in case the file don't have a dssp, so down stream it will trhow an error if dssp is still None
	for line in lines :
		if line.startswith('OrigSeq') :
			sequence = line.rstrip()[9:]
			# this one starts after the OrigSeq, splices after it and grabs the rest
			sequence = line.rstrip().split[':'][1]
			#  split will split based on ':' and [1] grabs the sequence
			#either one is fine
		if line starts with('dssp') :
			dssp = line.rstrip()[5:]	
			dssp = line.rstrip().split[':'][1]
			#again more of the same from above
			
	#out of the file now because we don't need anything else from it
	for k in range(len(sequence) - SIZE+1) :
		#range using a window size, range does something funky and doesn't include the
		#final character so SIZE+1 accounts for that I guess
		window = sequence[k:k+SIZE]
		#LOL what? something about making a window and its parameters
		combined = ''
		#gonna use this where we combine the residues
		for res in window :
			combined += codeToVector[res]
			
		combined += labels[dssp[k + (SIZE-1)/2 ] ]
		
		if random.random() < 0.8 :
			TRAINING.write(combined + '\n')	
		else :	
			VALIDATION.write(combined + '\n')
			#This is to write randomly 80% into training data and 20% into validation files
TRAINING.close()
VALIDATION.close()
#close out both files duh