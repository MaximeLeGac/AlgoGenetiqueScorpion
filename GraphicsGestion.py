import matplotlib.pyplot as plt


def graphics(reach_tab, energy_tab, score_tab):

	plt.subplot(221)
	plt.plot(reach_tab, c='#FF0000')
	plt.title('Reach (in meters)')

	plt.subplot(222)
	plt.plot(energy_tab, c='#009900')
	plt.title('Energy (in grams of TNT)')

	plt.subplot(223)
	plt.plot(score_tab, c='#FFFF00')
	plt.title('Score')

	plt.show()


