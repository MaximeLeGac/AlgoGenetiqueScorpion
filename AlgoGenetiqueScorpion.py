import math
import random
import CalculFormules


TAILLE_POPULATION_SCORPIONS = 10
NB_GENERATIONS = 10
TAUX_MUTATION = 5

def init():
    population_scorpions = []
    for i in range(TAILLE_POPULATION_SCORPIONS):
        population_scorpions.append(genererPopulation())

    for i in range(NB_GENERATIONS):
        print("----------------------------------------------------------------------------------------------")
        print("GENERATION "+str(i))

        for i in range(TAILLE_POPULATION_SCORPIONS):    
            evaluationTirScorpion(population_scorpions[i])
            print(str(i)+" = "+str(population_scorpions[i][0])+" | "+str(population_scorpions[i][1])+" | "+str(population_scorpions[i][2])+" | "+str(population_scorpions[i][3])+" | "+str(population_scorpions[i][4])+" | "+str(population_scorpions[i][5])+" | "+str(population_scorpions[i][6])+" | "+str(population_scorpions[i][7])+" | "+str(population_scorpions[i][8])+" | "+str(population_scorpions[i][9]))

        population_scorpions = selectionParentsScorpions(population_scorpions)


#################################################################################################################################
# Methode permettant de generer les valeurs des caracteristiques d'un scorpion
def generationValeurs(index):
    if index == 0:
        return random.randint(0, 90)
    elif index == 1:
        return round(random.uniform(0.5, 5), 1)
    elif index == 2:
        return round(random.uniform(0.1, 0.5), 1)
    elif index == 3:
        return round(random.uniform(0.1, 0.5), 1)
    elif index == 4:
        return round(random.uniform(1, 10), 1)
    elif index == 5:
        return round(random.uniform(0.5, 5), 1)
    elif index == 6:
        return 7850
    elif index == 7:
        return 210
    elif index == 8:
        return 0.24
    elif index == 9:
        return 9.81


#################################################################################################################################
# Methode d'initialisation d'un scorpion
def genererPopulation():
    angle_hausse                = generationValeurs(0)
    long_bras                   = generationValeurs(1)
    base_section                = generationValeurs(2)
    hauteur_section             = generationValeurs(3)
    long_corde                  = generationValeurs(4)
    long_fleche                 = generationValeurs(5)
    masse_volumique_materiau    = generationValeurs(6)
    module_young                = generationValeurs(7)
    coeff_poisson_materiau      = generationValeurs(8)
    gravite                     = generationValeurs(9)

    scorpion = [
                angle_hausse                # 0 - Angle de la hausse en degres
                ,long_bras                  # 1 - Longueur du bras de l'arc en metres
                ,base_section               # 2 - Base de la section du bras en metres
                ,hauteur_section            # 3 - Hauteur de la section du bras en metres
                ,long_corde                 # 4 - Longueur de la corde en metres
                ,long_fleche                # 5 - Longueur de la fleche en metres
                ,masse_volumique_materiau   # 6 - Masse volumique du materiau en kg/m au cube
                ,module_young               # 7 - Module de Young en Gpa
                ,coeff_poisson_materiau     # 8 - Coefficient de Poisson du materiau utilise
                ,gravite                    # 9 - Gravite terrestre
                ] # on stocke ces valeurs dans un tableau pour pouvoir realiser le croisement plus facilement

    return scorpion


#################################################################################################################################
# Methode permettant de noter les scorpions en fonction de leur tir
def evaluationTirScorpion(scorpion):
    
    ressort                 = CalculFormules.ressort(scorpion[7], scorpion[8])
    longueur_a_vide         = CalculFormules.longueurAVide(scorpion[1], scorpion[4])
    longueur_deplacement    = CalculFormules.longueurDeplacement(scorpion[5], longueur_a_vide)
    masse_projectile        = CalculFormules.masseProjectile(scorpion[6], scorpion[2], scorpion[3], scorpion[5])
    velocite                = CalculFormules.velocite(ressort, longueur_deplacement, masse_projectile)
    portee                  = CalculFormules.portee(velocite, scorpion[9], scorpion[0])
    energie_impact          = CalculFormules.energieImpact(masse_projectile, velocite)
    energie_gramme_TNT      = CalculFormules.equivalenceJouleGrammeTNT(energie_impact)
    moment_quadratique      = CalculFormules.momentQuadratique(scorpion[2], scorpion[3])
    force_traction          = CalculFormules.forceTraction(ressort, scorpion[5])
    fleche_bras_max         = CalculFormules.flecheBrasMax(force_traction, scorpion[1], scorpion[7], moment_quadratique)

    scorpion.append(0)

    # Si le bras casse
    if longueur_deplacement > fleche_bras_max:
        scorpion[10] += 1
    else:
        scorpion[10] += 3

    # Si longueur a vide est superieure a la longueur de le fleche
    if longueur_a_vide > scorpion[5]:
        scorpion[10] += 1
    else:
        scorpion[10] += 3

    # Si longueur de la corde est superieure a la longueur de l'arc
    if scorpion[4] > scorpion[1]:
        scorpion[10] += 1
    else:
        scorpion[10] += 3

    # Si la portee du tir s'approche des 300m
    if 250 <= portee <= 350:
        scorpion[10] += 10
    else:
        scorpion[10] += 1

    # Si la puissance du tir est importante



#################################################################################################################################
# On utilise la methode de selection par tournoi
def selectionParentsScorpions(population_scorpions):
    index = 0
    paires = []
    parents = []
    nouvelle_generation = []

    # On creer autant de paires de parents qu'il y a de scorpion
    for i in range(TAILLE_POPULATION_SCORPIONS):
        if index == 9:
            paires.append([population_scorpions[index], population_scorpions[0]])
        else:
            paires.append([population_scorpions[index], population_scorpions[index+1]])

        index += 1

    for i in range(TAILLE_POPULATION_SCORPIONS):
        proba_selection = random.randint(0, 100) # probabilite que le meilleur scorpion soit choisi
        # On genere un tableau qui va contenir tous les scorpions choisient pour etre parents
        if 0 <= proba_selection <= 80:
            if paires[i][0][10] > paires[i][1][10]:
                parents.append(paires[i][0])
            else:
                parents.append(paires[i][1])
        else:
            if paires[i][0][10] < paires[i][1][10]:
                parents.append(paires[i][0])
            else:
                parents.append(paires[i][1])
    
    index = 0
    while index != 10:
        #nouvelle_generation.append(croisementScorpions(parents[index], parents[index+1]))
        croisementScorpions(parents[index], parents[index+1], nouvelle_generation)
        index += 2

    random.shuffle(nouvelle_generation)
    return nouvelle_generation


#################################################################################################################################
# Methode de croisement de 2 scorpions
# permet de creer 2 nouveaux scorpions a partir des valeurs des 2 scorpions en parametre
def croisementScorpions(scorpion1, scorpion2, nouvelle_generation):
    hauteur_croisement = random.randint(0,9) # Nombre pour choisir au niveau de quel attribut "couper" les scorpions parents

    bebe_scorpion1 = []
    bebe_scorpion2 = []

    # Creation de la 1ere moitie de chaque enfant
    for i in range(hauteur_croisement):
        bebe_scorpion1.append(scorpion1[i])
        bebe_scorpion2.append(scorpion2[i])

    # Creation de la 2eme moitie de chaque enfant
    for i in range(hauteur_croisement, 10):
        bebe_scorpion1.append(scorpion1[i])
        bebe_scorpion2.append(scorpion2[i])

    mutation(bebe_scorpion1)
    mutation(bebe_scorpion2)

    nouvelle_generation.append(bebe_scorpion1)
    nouvelle_generation.append(bebe_scorpion2)

    return bebe_scorpion1, bebe_scorpion2


#################################################################################################################################
# Chaque enfant a une probabilite qu'une de ses caracteristiques change
def mutation(bebe_scorpion):
    mutation_rate = random.randint(0,100)

    if 0 <= mutation_rate <= TAUX_MUTATION:
        index_caracteristique = random.randint(0,5) # Chiffre permettant de choisir la caracteristique a faire muter
        bebe_scorpion[index_caracteristique] = generationValeurs(index_caracteristique)