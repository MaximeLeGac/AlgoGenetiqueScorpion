import math
import random


TAILLE_POPULATION_SCORPIONS = 10

def init():
    for i in range(TAILLE_POPULATION_SCORPIONS):
        population_scorpions[i] = genererPopulation()

    return 0


# Methode d'initialisation d'un scorpion
def genererPopulation():
    angle_hausse     = random.randint(0, 90)
    long_bras         = round(random.uniform(0.5, 5), 1)
    base_section     = round(random.uniform(0.1, 0.5), 1)
    hauteur_section = round(random.uniform(0.1, 0.5), 1)
    long_corde         = round(random.uniform(1, 10), 1)
    long_fleche     = round(random.uniform(0.5, 5), 1)

    scorpion = [
                angle_hausse         # Angle de la hausse en degres
                ,long_bras           # Longueur du bras de l'arc en metres
                ,base_section        # Base de la section du bras en metres
                ,hauteur_section     # Hauteur de la section du bras en metres
                ,long_corde          # Longueur de la corde en metres
                ,long_fleche         # Longueur de la fleche en metres
                ] # on stocke ces valeurs dans un tableau pour pouvoir realiser le croisement plus facilement

    return scorpion

# Methode de croisement de 2 scorpions
# permet de creer 2 nouveaux scorpions a partir des valeurs des 2 scorpions en parametre
def croisementScorpions(scorpion1, scorpion2):
    hauteur_croisement = random.randint(0,5) # Nombre pour choisir au niveau de quel attribut "couper" les scorpions parents

    # Creation de la 1ere moitie de chaque enfant
    for i in range(hauteur_croisement):
        bebe_scorpion1[i] = scorpion1[i]
        bebe_scorpion2[i] = scorpion2[i]

    # Creation de la 2eme moitie de chaque enfant
    for i in range(hauteur_croisement, 6):
        bebe_scorpion1[i] = scorpion1[i]
        bebe_scorpion2[i] = scorpion2[i]

    return bebe_scorpion1, bebe_scorpion2


def calculDistance():

    return 0






