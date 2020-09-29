import random
alea = random.randint(1,3000)
nb = 0
nbr = 0
print("Le but est de trouver le nombre généré aléatoirement(entre 1 et 30)")
while (nbr != alea) :
    nb = input ("Entrer un nombre :\n")
    nbr = int(nb)
    #if nbr > 30:
        #return()
    if nbr > alea:
      print("            C'est moins que " + nb + "\n")
    elif nbr < alea:
      print("            C'est plus que " + nb + "\n")
    else:
        print("Gagné ! C'était " + nb + ".\n")