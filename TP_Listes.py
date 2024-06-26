#Question 1

# Création des tables de multiplication
tables = [1, 2, 3, 5, 8]
resultats = []

for table in tables:
    table_resultat = []
    for i in range(1, 11):  # On va de 1 à 10 pour chaque table
        table_resultat.append(table * i)
    resultats.append(table_resultat)


for idx, table in enumerate(tables):
    print(f"Table de {table}: {resultats[idx]}")

#Autre méthode avec map()
liste = [1, 2, 3, 5, 8]

def myfunc(a) :
    return [a * i for i in range (11)]

result =list(map(myfunc, liste))
print(result)

#Question 2

# Création de la liste de 1 à 10
nombres = range(1, 10 + 1)

# Liste pour stocker les résultats sous forme de chaînes
resultats_table_5 = []

# Résultats de la table de 5 sous forme de chaînes de caractères String
for nombre in nombres:
    resultat = 5 * nombre
    resultat_str = f"5 x {nombre} = {resultat}"
    resultats_table_5.append(resultat_str)

for ligne in resultats_table_5:
    print(ligne)

#Question 3

# Initialisation du compteur
i = 1
# Liste pour stocker les résultats sous forme de chaînes
resultats_table_5 = []

# Boucle while avec condition True
while True:
    # Calcul du résultat de la multiplication
    resultat = 5 * i
    # Création de la chaîne de caractères
    resultat_str = f"5 x {i} = {resultat}"
    # Ajout de la chaîne à la liste
    resultats_table_5.append(resultat_str)

    print(resultat_str)
    # Incrémentation du compteur
    i += 1
    # Condition d'arrêt pour sortir de la boucle
    if i > 10:
        break

for ligne in resultats_table_5:
    print(ligne)

#Question 4
# Création du dictionnaire
dictionnaire = {"a": 42, "b": 42, "c": 42, "d": 42}

# Initialisation de l'accumulateur avec la valeur de la première clé
accumulateur = dictionnaire["a"]

# Parcourir chaque clé et effectuer les opérations spécifiées
for key in dictionnaire:
    if key == "a":
        # Déjà initialisé
        continue
    elif key == "d":
        accumulateur -= dictionnaire[key]
    else:
        accumulateur *= dictionnaire[key]

print(accumulateur)

#Question 5
# Nombre d'étoiles
n = 5

# Création du motif sur une seule ligne
motif = ""

# Boucle pour chaque groupe d'étoiles
for i in range(1, n + 1):
    # Ajouter les étoiles pour chaque groupe
    motif += '*' * i
    # Ajouter un espace après chaque groupe sauf le dernier
    if i < n:
        motif += ' '

print(motif)

#Autre méthode avec map()
print( ' ' .join(list(map(lambda x : x * "*" , range(1,6)))))

#Question 6

def tri_bulles(nbr) :
    n = len(nbr)
    for i in range(n-1):
        for j in range(0, n - i - 1):
            if nbr[j] > nbr[j + 1]:
            # Échange des éléments
               nbr[j], nbr[j + 1] = nbr[j + 1], nbr[j]

nbr = [5, 4, 3, 2, 1]
tri_bulles(nbr)
print(nbr)

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
