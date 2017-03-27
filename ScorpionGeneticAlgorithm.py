import math
import random
import ScorpionFormulas
import GraphicsGestion


#################################################################################################################################
POPULATION_SIZE             = 2000          # Number of scorpions in a generation
NB_GENERATIONS              = 50           # Number of generations of scorpions
MUTATION_RATE               = 0.1           # Percentage of chance that a mutation occurs to a baby scorpion
TARGET_DISTANCE             = 350           # Distance (in meters) to the target

# Physical properties of the scorpions's arm material
MATERIAL_DENSITY            = 7850
MATERIAL_YOUNG_MODUL        = 210

# Physical properties of the arrow's material
MATERIAL_COEFF_POISSON      = 0.27
ARROW_DENSITY               = 7850

GRAVITY                     = 9.81
#################################################################################################################################

def init():
    # Creation of all necessary tables
    scorpionsPopulation = []
    reach_tab = []
    energy_tab = []
    score_tab = []
    all_reach_tab = []
    all_energy_tab = []
    all_score_tab = [] = []
    score_tab_generation = []
    mass_tab = []
    velocity_tab = []
    variance_tab = []

    print("Population size      = "+str(POPULATION_SIZE))
    print("Number of generation = "+str(NB_GENERATIONS))
    print("Mutation rate        = "+str(MUTATION_RATE))
    print("Target distance      = "+str(TARGET_DISTANCE))

    # Creation of the first generation of scorpions
    for i in range(POPULATION_SIZE):
        scorpionsPopulation.append(generate_scorpion())

    # Loop on all generations
    for i in range(NB_GENERATIONS):
        '''print("*******************************************************************************************************")
                                print("******************************************** "+"GENERATION "+str(i)+" ********************************************")
                                print("*******************************************************************************************************")'''
        score_tab_generation = []

        # Loop on the population of the current generation
        for i in range(POPULATION_SIZE):
            '''if i == NB_GENERATIONS:
                    print("----------------------------------------------------------------------------------")
                    print("--------------------------------------- "+str(i)+" ---------------------------------------")
                    print("----------------------------------------------------------------------------------")
                    print("Angle                = "+str(scorpionsPopulation[i][0]))
                    print("Arm length           = "+str(scorpionsPopulation[i][1]))
                    print("Arm's section base   = "+str(scorpionsPopulation[i][2]))
                    print("Arm's section height = "+str(scorpionsPopulation[i][3]))
                    print("Rope length          = "+str(scorpionsPopulation[i][4]))
                    print("Arrow length         = "+str(scorpionsPopulation[i][5]))
                    print("Arrow diameter       = "+str(scorpionsPopulation[i][6]))'''

            # Call to the function of evaluation of the current scorpion's shoot
            scorpionEvaluation(scorpionsPopulation[i], reach_tab, energy_tab, score_tab, score_tab_generation, mass_tab, velocity_tab)

        # To have better graphics, we calculate the average value of each generation for the reach, the energy (in grams of TNT) and the score
        all_reach_tab.append(get_average_generation(reach_tab))
        reach_tab = []
        all_energy_tab.append(get_average_generation(energy_tab))
        energy_tab = []
        all_score_tab.append(get_average_generation(score_tab))
        score_tab = []

        # Call to the fitness function that will select the parents who will reproduce
        # The next generation will be created from the individuals of the current generation selected
        # A mutation has a chance to occurs on each children
        scorpionsPopulation = selectionByTournament(scorpionsPopulation)

        # Calculation of the variance
        variance = GraphicsGestion.get_variance(score_tab_generation) # We get a variance score for each generation based on the scores of each generations
        variance_tab.append(variance)

    # Call to the function who will create the graphics of variance, reach, energy, score, projectile's mass and velocity
    GraphicsGestion.graphics(variance_tab, all_reach_tab, all_energy_tab, all_score_tab, mass_tab, velocity_tab)


#################################################################################################################################
# Return the average value of the table passed in parameter (table of values for a single generation)
def get_average_generation(tab_generations):
    tab_by_generation = []
    somme_tab = 0

    for i in range(len(tab_generations)):
        somme_tab += tab_generations[i]

    return (somme_tab/POPULATION_SIZE)


#################################################################################################################################
# Generate the values of the caracteristics of a scorpion
def values_generation(index):
    if index == 0:
        return random.randint(5, 85) # 0 - Angle of the scorpion in degrees
    elif index == 1:
        return round(random.uniform(1, 30), 1) # 1 - Arm length in meters
    elif index == 2:
        return round(random.uniform(0.1, 10), 1) # 2 - Arm's section base in meters
    elif index == 3:
        return round(random.uniform(0.1, 10), 1) # 3 - Arm's section height in meters
    elif index == 4:
        return round(random.uniform(1, 50), 1) # 4 - Rope length in meters
    elif index == 5:
        return round(random.uniform(0.5, 20), 1) # 5 - Arrow length in meters
    elif index == 6:
        return round(random.uniform(0.1, 10), 1) # 6 - Arrow diameter in meters


#################################################################################################################################
# Create a scorpion
def generate_scorpion():
    # The values are generated randomly
    angle                   = values_generation(0)
    arm_length              = values_generation(1)
    section_base            = values_generation(2)
    section_height          = values_generation(3)
    rope_length             = values_generation(4)
    arrow_length            = values_generation(5)
    arrow_diameter          = values_generation(6)

    scorpion = [
                angle                   # 0 - Angle of the scorpion in degrees
                ,arm_length             # 1 - Arm length in meters
                ,section_base           # 2 - Arm's section base in meters
                ,section_height         # 3 - Arm's section height in meters
                ,rope_length            # 4 - Rope length in meters
                ,arrow_length           # 5 - Arrow length in meters
                ,arrow_diameter         # 6 - Arrow diameter in meters
                ]

    return scorpion


#################################################################################################################################
# Evaluation of a scorpion on his shoot
def scorpionEvaluation(scorpion, reach_tab, energy_tab, score_tab, score_tab_generation, mass_tab, velocity_tab):

    # Calculation of the shoot based on the scorpion caracteristics

    spring              = ScorpionFormulas.spring(MATERIAL_YOUNG_MODUL, MATERIAL_COEFF_POISSON)
    empty_length        = ScorpionFormulas.empty_length(scorpion[1], scorpion[4])
    movement_length     = ScorpionFormulas.movement_length(scorpion[5], empty_length)

    quadratic_moment    = ScorpionFormulas.quadratic_moment(scorpion[2], scorpion[3])
    traction_force      = ScorpionFormulas.traction_force(spring, movement_length)
    arrow_arm_max       = ScorpionFormulas.arrow_arm_max(traction_force, scorpion[1], MATERIAL_YOUNG_MODUL, quadratic_moment)

    projectile_mass     = ScorpionFormulas.projectile_mass(ARROW_DENSITY, scorpion[6], scorpion[5])
    velocity            = ScorpionFormulas.velocity(spring, movement_length, projectile_mass)
    reach               = ScorpionFormulas.reach(velocity, GRAVITY, scorpion[0])
    impact_energy       = ScorpionFormulas.impact_energy(projectile_mass, velocity)
    energy_grams_TNT    = ScorpionFormulas.energy_grams_TNT(impact_energy)

    scorpion.append(1) # Initialisation of the scorpion's score

    # -------- Calculation of the score

    # If the arm doesn't break
    if movement_length > arrow_arm_max:
        scorpion[7] += 1
    else:
        scorpion[7] += 10

    # If length when empty is inferior to the length of the arrow
    if empty_length > scorpion[5]:
        scorpion[7] += 1
    else:
        scorpion[7] += 10

    # If the arrow's length is inferior to the arc's length
    if scorpion[4] > scorpion[1]:
        scorpion[7] += 1
    else:
        scorpion[7] += 10

    # If the shoot's reach goes near the target
    if reach <= 0:
        scorpion[7] += 1
    else:
        scorpion[7] += (TARGET_DISTANCE-abs(TARGET_DISTANCE-reach))*10

    # If the shoot's power is significant enough
    scorpion[7] += energy_grams_TNT*10

    '''print("")
                print("empty_length = "+str(empty_length))
                print("movement_length = "+str(movement_length))
                print("projectile_mass = "+str(projectile_mass))
                print("velocity = "+str(velocity))
                print("reach = "+str(reach))
                print("impact_energy = "+str(impact_energy))
                print("energy_grams_TNT = "+str(energy_grams_TNT))
                print("SCORE = "+str(scorpion[7]))'''

    # The results are put in tables which will be used to create the graphics
    reach_tab.append(reach)
    energy_tab.append(energy_grams_TNT)
    score_tab.append(scorpion[7])
    score_tab_generation.append(scorpion[7])
    mass_tab.append(projectile_mass)
    velocity_tab.append(velocity)


#################################################################################################################################
# Selection of the scorpions who will become parents of the next generation
def selectionByTournament(scorpionsPopulation):
    index = 0
    pairs = []
    parents = []
    new_generation = []

    # We create as much pairs of parents than scorpions in our population (ex : 20 scorpions = 20 pairs of 2 scorpions)
    for i in range(POPULATION_SIZE):
        if index == (POPULATION_SIZE-1):
            pairs.append([scorpionsPopulation[index], scorpionsPopulation[0]])
        else:
            pairs.append([scorpionsPopulation[index], scorpionsPopulation[index+1]])
        index += 1

    # Loop on all the pairs
    for i in range(POPULATION_SIZE):
        selection_probability = random.randint(0, 100) # probability that the best scorpion (the one with the best score) of the match is chosen
        # We generate a table which will contain all the scorpions chosen to be parents

        if 0 <= selection_probability <= 80: # The best scorpion is the winner of the match
            if pairs[i][0][7] > pairs[i][1][7]:
                parents.append(pairs[i][0])
            else:
                parents.append(pairs[i][1])
        else: # The worst scorpion is the winner of the match
            if pairs[i][0][7] < pairs[i][1][7]:
                parents.append(pairs[i][0])
            else:
                parents.append(pairs[i][1])

    index = 0
    while index != POPULATION_SIZE:
        #new_generation.append(scorpionsCrossbreeding(parents[index], parents[index+1]))
        scorpionsCrossbreeding(parents[index], parents[index+1], new_generation) # Call to the crossbreeding who will create the next generation
        index += 2

    random.shuffle(new_generation)
    return new_generation


#################################################################################################################################
# Allow to create 2 new scorpions from the values of 2 parents scorpions passed in parameters
def scorpionsCrossbreeding(scorpion1, scorpion2, new_generation):
    crossing_height = random.randint(1,6) # Number to chose at which level of the table scorpion to "cut" the parents

    baby_scorpion_1 = []
    baby_scorpion_2 = []

    #print("*******************************************************************************************")
    #print("PARENT 1 = "+str(scorpion1[0])+" | "+str(scorpion1[1])+" | "+str(scorpion1[2])+" | "+str(scorpion1[3])+" | "+str(scorpion1[4])+" | "+str(scorpion1[5])+" | "+str(scorpion1[6])+" ==> "+str(scorpion1[7]))
    #print("PARENT 2 = "+str(scorpion2[0])+" | "+str(scorpion2[1])+" | "+str(scorpion2[2])+" | "+str(scorpion2[3])+" | "+str(scorpion2[4])+" | "+str(scorpion2[5])+" | "+str(scorpion2[6])+" ==> "+str(scorpion2[7]))
    #print("crossing_height : "+str(crossing_height))

    # Creation of the first half of each child based on the first half of each parents
    for i in range(crossing_height):
        baby_scorpion_1.append(scorpion1[i])
        baby_scorpion_2.append(scorpion2[i])

    # Creation of the second half of each child based on the second half of each parents
    for i in range(crossing_height, 7):
        baby_scorpion_1.append(scorpion2[i])
        baby_scorpion_2.append(scorpion1[i])

    #print("BABY 1 = "+str(baby_scorpion_1[0])+" | "+str(baby_scorpion_1[1])+" | "+str(baby_scorpion_1[2])+" | "+str(baby_scorpion_1[3])+" | "+str(baby_scorpion_1[4])+" | "+str(baby_scorpion_1[5])+" | "+str(baby_scorpion_1[6]))
    #print("BABY 2 = "+str(baby_scorpion_2[0])+" | "+str(baby_scorpion_2[1])+" | "+str(baby_scorpion_2[2])+" | "+str(baby_scorpion_2[3])+" | "+str(baby_scorpion_2[4])+" | "+str(baby_scorpion_2[5])+" | "+str(baby_scorpion_2[6]))

    # Call to the mutation function on each child
    mutation(baby_scorpion_1)
    mutation(baby_scorpion_2)

    #print("BABY 1 = "+str(baby_scorpion_1[0])+" | "+str(baby_scorpion_1[1])+" | "+str(baby_scorpion_1[2])+" | "+str(baby_scorpion_1[3])+" | "+str(baby_scorpion_1[4])+" | "+str(baby_scorpion_1[5])+" | "+str(baby_scorpion_1[6]))
    #print("BABY 2 = "+str(baby_scorpion_2[0])+" | "+str(baby_scorpion_2[1])+" | "+str(baby_scorpion_2[2])+" | "+str(baby_scorpion_2[3])+" | "+str(baby_scorpion_2[4])+" | "+str(baby_scorpion_2[5])+" | "+str(baby_scorpion_2[6]))

    new_generation.append(baby_scorpion_1)
    new_generation.append(baby_scorpion_2)

    return baby_scorpion_1, baby_scorpion_2


#################################################################################################################################
# Each child has a probability that one of its values mutate
def mutation(baby_scorpion):
    mutation_rate = random.randint(0,100)
    #print("mutation_rate : "+str(mutation_rate))

    if 0 <= mutation_rate <= MUTATION_RATE:
        value_index = random.randint(0,6) # Number allowing us to know which value to change
        baby_scorpion[value_index] = values_generation(value_index)






