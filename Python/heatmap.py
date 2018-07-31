import numpy as np
import matplotlib.pyplot as plt


def heatMapForDATA( DATA, rowlabels, collabels, fignum, userowlabels=True, usecollabels=False ) :
	## Need corners of quads for color map
	X = [ [] for i in range(0,len(collabels)+1) ]
	Y = [ [] for j in range(0,len(collabels)+1) ]
	for j in range(0,len(collabels)+1) :
		for i in range(0,len(rowlabels)+1) :
			X[j].append(j)
			Y[j].append(i)

	Z = [ [] for i in range(0,len(collabels)) ]
	
	for j in range(0,len(collabels)):
		for k in range(0,len(rowlabels)) :
			Z[j].append(DATA[k][j])

	X = np.array(X)
	Y = np.array(Y)
	Z = np.array(Z)

	fig = plt.figure(fignum)
	ax = fig.add_subplot(111)
	cmap = plt.get_cmap('hot')
	cm = ax.pcolormesh(X, Y, Z, cmap=cmap )
	ax.set_ylim([0.,len(rowlabels)])
	ax.set_xlim([0.,len(collabels)])
	if usecollabels :
		xticks = [ 0.5 + j for j in range(0,len(collabels)) ]
		ax.set_xticks(xticks)
		ax.set_xticklabels(collabels)
	if userowlabels :
		yticks = [ 0.5 + j for j in range(0,len(rowlabels)) ]
		ax.set_yticks(yticks)
		ax.set_yticklabels(rowlabels)
	plt.colorbar(cm, ax=ax)
	plt.draw()
