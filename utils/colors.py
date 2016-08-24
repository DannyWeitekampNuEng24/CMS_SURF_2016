
#A list of colors that contrast <- well sort of there is probably a better list
colors_contrasting = \
[
#Shade 0
(0.675,0.412,0.231),
(0.224,0.204,0.471),
(0.494,0.631,0.216),
(0.145,0.427,0.38),
(0.675,0.573,0.231),
(0.553,0.188,0.38),


#Shade 1
(1,0.745,0.573),
(0.518,0.502,0.753),
(0.816,0.949,0.541),
(0.424,0.757,0.702),
(1,0.91,0.608),
(0.863,0.49,0.686),

#Shade 3
(0.631,0.255,0),
(0.125,0.09,0.584),
(0.392,0.592,0),
(0,0.875,0.725),
(0.843,0.647,0.012),
(0.49,0,0.259),

#Shade 2
(0.988,0.408,0.012),
(0.286,0.255,0.682),
(0.62,0.922,0.012),
(0.173,0.663,0.58),
(0.98,0.812,0.267),
(0.867,0,0.459),


#Shade 4
(0.404,0.212,0.078),
(0.078,0.059,0.361),
(0.278,0.376,0.075),
(0.012,0.325,0.271),
(0.518,0.4,0.012),
(0.322,0.094,0.216)
]

def showColors(colors):
	'''Plots a list of colors with outlines taken from the same list'''
	fig, ax = plt.subplots(1)
	fig.set_size_inches((10,10))

	# Show the whole color range
	for i in range(len(colors)):
	    x = np.random.normal(loc=(i%4)*3, size=100)
	    y = np.random.normal(loc=(i//4)*3, size=100)
	    c = colors[i]
	    j = (i * 3 +4) % len(colors)
	    b = colors[j]
	    
	    ax.scatter(x, y, label=str(i), alpha=.7, edgecolor=b,s=60, facecolor=c, linewidth=1.0)