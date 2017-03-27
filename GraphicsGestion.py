import matplotlib.pyplot as plt
import numpy as np
from ScorpionGeneticAlgorithm import *

def graphics(variance_tab, reach_tab, energy_tab, score_tab, mass_tab, velocity_tab):

	plt.subplot(221)
	plt.plot(variance_tab, c='#FF7400')
	plt.title('Variance')

	plt.subplot(222)
	plt.plot(reach_tab, c='#162EAE')
	plt.plot([0, NB_GENERATIONS], [TARGET_DISTANCE, TARGET_DISTANCE], c='#FF0000') # RED LINE
	plt.axis([0, NB_GENERATIONS, 0, TARGET_DISTANCE*(1.5)])
	plt.title('Reach (in meters)')

	plt.subplot(223)
	plt.plot(energy_tab, c='#009900')
	plt.title('Energy (in grams of TNT)')

	plt.subplot(224)
	plt.plot(score_tab, c='#FFFF00')
	plt.title('Score')

	'''
	plt.subplot(221)
	plt.plot(mass_tab, c='#FFFF00')
	plt.title('Arrow mass')

	plt.subplot(222)
	plt.plot(velocity_tab, c='#FFFF00')
	plt.title('Velocity')
	'''

	plt.show()



def get_variance(score_tab_generation):
	return np.var(score_tab_generation)



