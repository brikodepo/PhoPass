#--------------------------------------------------------------------------------
#-----------------------------©--©--©--------------------------------------------
#------------------------CopyRight by lolo---------------------------------------
#---------------------------11/11/2023-------------------------------------------
#--------------------------------------------------------------------------------





#----------------------------------import---------------------------------------->>>
import os
import random
import colorama
from colorama import just_fix_windows_console
from colorama import Fore, Style
import time



#---------------------------------fonctions-------------------------------------->>>
def logo():
    os.system("cls")
    print(Fore.BLUE + " __________.__\n \______   \  |__   ____ ___________    ______ ______\n  |     ___/  |  \ /  _ \\____ \__  \  /  ___//  ___/\n  |    |   |   Y  (  <_> )  |_> > __ \_\___ \ \___ \ \n  |____|   |___|  /\____/|   __(____  /____  >____  >\n                \/       |__|       \/     \/     \/\n                                                     By lolo")
    print(Style.RESET_ALL)



def generer_mot_de_passe(longueur):
    voyelles = "a310u"
    consonnes = "bcdf8hjklmnpqr$tvwxyz"

    if longueur % 2 != 0:
        longueur += 1

    mot_de_passe = ""
    for _ in range(longueur // 2):
        mot_de_passe += random.choice(consonnes) + random.choice(voyelles)

    return mot_de_passe

def gen_mot_de_passe():
    longueur_mot_de_passe = int(input("Entrez la longueur du mot de passe phonétique (doit être paire, 12 préférable) : "))
    mot_de_passe_phonetique = generer_mot_de_passe(longueur_mot_de_passe)
    print(f"Mot de passe phonétique : ")
    print(Style.BRIGHT +Fore.RED + mot_de_passe_phonetique)
    print(Style.RESET_ALL)
    print("Entrer pour continuer")
    input("")


#------------------------------début du script----------------------------------->>>
while True:
    logo()
    choix = input("Générer un mot de passe OUI (O) / NON (N) : ")

    if choix == "O":
        gen_mot_de_passe()
    elif choix == "N":
        print("A bientôt ;)")
        time.sleep(2)
    else:
        print("Choix invalide")


    




