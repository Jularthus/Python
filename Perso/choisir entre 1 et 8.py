joueurs = input('Nombre de joueurs ? Max = 8 Min = 2\n\n')
nbrjr = int(joueurs)
if nbrjr > 8: 
    print("C\'est 8 max.")
if nbrjr < 2: 
    print("C\'est 2 min.")
import random
nbr = random.randint(1,2) 
prenom1 = input('Prénom du joueur 1 ?\n\n')
prenom2 = input('\nPrénom du joueur 2 ?\n\n')
if nbrjr > 2: 
    prenom3 = input('\nPrénom du joueur 3 ?\n\n')
if nbrjr > 3:
    prenom4 = input('\nPrénom du joueur 4 ?\n\n')
if nbrjr > 4:
    prenom5 = input('\nPrénom du joueur 5 ?\n\n')
if nbrjr > 5:
    prenom6 = input('\nPrénom du joueur 6 ?\n\n')
if nbrjr > 6:
    prenom7 = input('\nPrénom du joueur 7 ?\n\n')
if nbrjr > 7:
    prenom8 = input('\nPrénom du joueur 8 ?\n\n')


if nbr == 1:
    print('C\'est ' + prenom1 + ' qui gagne.')
elif nbr == 2:
    print('C\'est ' + prenom2 + ' qui gagne.')
elif nbr == 3:
    print('C\'est ' + prenom3 + ' qui gagne.')
elif nbr == 4:
    print('C\'est ' + prenom4 + ' qui gagne.')
elif nbr == 5:
    print('C\'est ' + prenom5 + ' qui gagne.')
elif nbr == 6:
    print('C\'est ' + prenom6 + ' qui gagne.')
elif nbr == 7:
    print('C\'est ' + prenom7 + ' qui gagne.')
elif nbr == 8:
    print('C\'est ' + prenom8 + ' qui gagne.')
