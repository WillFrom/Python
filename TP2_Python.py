#Exercice2

#Question1
age = int(input("Entrez votre âge: "))

if age < 18:
    print(f"Vous ne pouvez pas entrer vous n'êtes pas majeur vous avez {age} ans.")
elif age >= 18 and age < 42:
    print(f"Vous pouvez entrer vous êtes majeur vous avez {age} ans.")
else:
    print("Félicitations, vous devenez le patron de la boîte de nuit !")