#Question 7

import datetime

annee_actuelle = datetime.datetime.now().year

annees = list(range(1980, annee_actuelle + 1))

print(annees)

#Question 8
#10 lignes donc (1,10)
for i in range(1, 10):
    print('1' * i)

#Question 9

# Boucle pour chaque ligne
for i in range(1, 10):
    # Construction du motif pour chaque ligne
    motif = '[' * i + ' ' + ']' * i
    # Center : pour centrer le motif
    print(motif.center(10 * 3))