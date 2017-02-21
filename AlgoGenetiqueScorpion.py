import math
import random


TAILLE_POPULATION_SCORPIONS = 10

def init():
    for i in range(TAILLE_POPULATION_SCORPIONS):
        population_scorpions[i] = genererPopulation()

    return 0


# Methode d'initialisation d'un scorpion
def genererPopulation():
    angle_hausse                = random.randint(0, 90)
    long_bras                   = round(random.uniform(0.5, 5), 1)
    base_section                = round(random.uniform(0.1, 0.5), 1)
    hauteur_section             = round(random.uniform(0.1, 0.5), 1)
    long_corde                  = round(random.uniform(1, 10), 1)
    long_fleche                 = round(random.uniform(0.5, 5), 1)
    masse_volumique_materiau    = 7850
    module_young                = 210
    coeff_poisson_materiau      = 0.24 # Le materiau utilise est l'acier
    gravite                     = 9.81

    scorpion = [
                angle_hausse                # 0 - Angle de la hausse en degres
                ,long_bras                  # 1 - Longueur du bras de l'arc en metres
                ,base_section               # 2 - Base de la section du bras en metres
                ,hauteur_section            # 3 - Hauteur de la section du bras en metres
                ,long_corde                 # 4 - Longueur de la corde en metres
                ,long_fleche                # 5 - Longueur de la fleche en metres
                ,masse_volumique_materiau   # 6 - Masse volumique du materiau en kg/m au cube
                ,module_young               # 7 - Module de Young en Gpa
                ,coeff_poisson_materiel     # 8 - Coefficient de Poisson du materiau utilise
                ,gravite                    # 9 - Gravite terrestre
                ] # on stocke ces valeurs dans un tableau pour pouvoir realiser le croisement plus facilement

    return scorpion

# Methode de croisement de 2 scorpions
# permet de creer 2 nouveaux scorpions a partir des valeurs des 2 scorpions en parametre
def croisementScorpions(scorpion1, scorpion2):
    hauteur_croisement = random.randint(0,9) # Nombre pour choisir au niveau de quel attribut "couper" les scorpions parents

    # Creation de la 1ere moitie de chaque enfant
    for i in range(hauteur_croisement):
        bebe_scorpion1[i] = scorpion1[i]
        bebe_scorpion2[i] = scorpion2[i]

    # Creation de la 2eme moitie de chaque enfant
    for i in range(hauteur_croisement, 10):
        bebe_scorpion1[i] = scorpion1[i]
        bebe_scorpion2[i] = scorpion2[i]

    return bebe_scorpion1, bebe_scorpion2

# Methode permettant de noter les scorpions en fonction de leur tir
def evaluationTirScorpion():

    return 0


def ruptureBras(scorpion):
    

    return 0


def calculDistance():

    return 0






