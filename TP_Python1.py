#Question 1
print('My Python Code Forever')

#Question 2
print('''My Python 
      Code 
      every day''')

#Question 3
var1 = 'Hello',
var2 = 3.3 ,
var9 = 10 ,
var3 = True ,
var4 = [1, 2, 3, 4, 5] ,
var5 = ('red', 'pink', 'blue') ,
var6 = {1, 2, 3, 4, 5} ,
var7 = {'name': 'Marion', 'age': 24, 'city': 'Paris'} ,
var8 = None,
var9 = 10

#Question 4
my42count = 'quarante-deux'
print(len(my42count))

#Question 5
# Variable à vérifier
variable_a_verifier = 'Hi'

# Création d'un dictionnaire globals() contenant toutes les variables globales existantes
variables_globales = globals()

# Création de la variable souhaitée en utilisant get() pour obtenir la valeur de la variable si elle existe, sinon la valeur par défaut est 42
nouvelle_variable = variables_globales.get('No', 42)
print(nouvelle_variable)

#Question 6
myArray42 = list('quarante-deux')
print(myArray42)

#Question 7
myArray42Len = len(myArray42)
print(myArray42Len)

#Question 8
var11 = "La grande réponse sur la vie, l’univers et le reste !"
myArray42str = ''.join(myArray42)
print(myArray42str)

myArray42str2 = myArray42str + ' ' + var11
print(myArray42str2)

#Question 9
import random 
rand = random.randint(1, 42)
print(rand)
est_quarante_deux = (rand == 42)
print(est_quarante_deux)

#Question 10
var1 = 'Hello'
var2 = 3.3 
var9 = 10 
var3 = True 
var4 = [1, 2, 3, 4, 5] 
var5 = ('red', 'pink', 'blue') 
var6 = {1, 2, 3, 4, 5} 
var7 = {'name': 'Marion', 'age': 24, 'city': 'Paris'} 
var8 = None
var9 = 10

print(type(var1))

#Question 11
compute42 = 7 * 6
print(compute42)

compute42str = str(compute42)
print(compute42str)

#Question 12
var13 = '42424242'
var13bis = var13.replace('42','quarante-deux')
print(var13bis)

#Question 13
a=24
b=42
print(a,b)
c=a
a=b
b=c
print(a,b)


#Exercice2

#Question1
age = int(input("Entrez votre âge: "))

if age < 18:
    print(f"Vous ne pouvez pas entrer vous n'êtes pas majeur vous avez {age} ans.")
elif age >= 18 and age < 42:
    print(f"Vous pouvez entrer vous êtes majeur vous avez {age} ans.")
else:
    print("Félicitations, vous devenez le patron de la boîte de nuit !")

#Question4


