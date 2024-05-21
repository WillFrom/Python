#Exercice 1 :
age=int(input("Donnez votre age : " ))
OK= age in (18,42)
NO= age in(0,17)
if OK ==True:
    print("Vous pouvez entrer vous êtes majeur vous avez ",age)
elif NO:
    print("Vous ne pouvez pas entrer vous n'êtes pas majeur vous avez",age)
elif age>=42:
    print("Hello patron")
else :
    print("Age n'existe pas, vérifiez votre valeur")

#Exercice 2 :
import random
temp=random.randint(0, 30)
print(temp)

if temp<=10:
    print("Cool")
elif 11<=temp<=20:
    print("Tepid")
else:
    print("Warm")

#Exercice 3 :
import datetime

jour_actuel = datetime.datetime.now().strftime('%A')
match jour_actuel:
    case 'Monday':
        print(f'Nous sommes Lundi')
    case 'Tuesday':
        print(f'Nous sommes Mardi')
    case 'Wednesday':
        print(f'Nous sommes Mercredi')
    case 'Thursday':
        print(f'Nous sommes Jeudi')
    case 'Friday':
        print(f'Nous sommes Vendredi')
    case 'Saturday':
        print(f'Nous sommes Samedi')
    case 'Sunday':
        print(f'Nous sommes Dimanche')

#Exercice 4 : 


#Exercice 5 : 


#Exercice 6 : 


#Exercice 7 : 
nbr=int(input("Donnez un nombre : "))
if nbr%2==0:
    print("Le nombre est pair")
else:
    print("Le nombre est impair")

