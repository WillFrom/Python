#Question 1

def myPutStr(valeur):
    # On vérifie si la valeur est un nombre (entier ou flottant)
    if isinstance(valeur, (int, float)):
        return "et pourquoi pas 42 ?"
    # Sinon, retourner la valeur en string
    else:
        return valeur
    
print(myPutStr('non'))

#Question 2

def computeSurfaceM2(longueur, largeur):
    # Calculer la surface en m²
    surface = longueur * largeur
    # Formater le résultat en string
    resultat = "Votre surface est de {} m2".format(surface)
    return resultat

print(computeSurfaceM2(5,10))

#Question 3

age = int(input("Entrez votre âge: "))

def detectMyAgeByNight(age) :
    if age < 18:
       return print(f"Vous ne pouvez pas entrer vous n'êtes pas majeur vous avez {age} ans.")
    elif age >= 18 and age < 42:
       return print(f"Vous pouvez entrer vous êtes majeur vous avez {age} ans.")
    else:
       return print("Félicitations, vous devenez le patron de la boîte de nuit !")

message = detectMyAgeByNight(age)
print(message)

#Question 4

Data1 = [1 , 2 , 3.33]
Data2 = [3 , 2 , 1]
Data3 = [6.7 , 4 , 2]


#Question 5

from datetime import datetime

heure = datetime.now().time()

print(heure)

#Question 6

def check_palindrome(v): 
    reverse = v[::-1]  
  
    if (v == reverse): 
        return True
    return False
  
var = input(("Entrez une valeur: "))
if(check_palindrome(var)):
    print("True") 
else:
    print("False") 