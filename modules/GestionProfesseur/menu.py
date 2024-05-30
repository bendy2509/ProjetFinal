

from modules.GestionProfesseur.modules.getInfos import Coordinates
from modules.createData import *

file_ = "dataProfesseur.db"
professor = Professor(file_)
cordonates = Coordinates()
data = Databases(file_)

def adminMenu():
    """ """
    # clearner = Coordinates()
    Coordinates.clear_screen()
    print("\t" * 5 + " ACCES D'ADMINISTRER ACCORDE ")
    print("\t" * 2, "*" * 75)
    print()
    print("\t" * 4 + "*" + "\t" + "1. Lister les professeurs.", "\t" * 3 + "*")
    print("\t" * 4 + "*" + "\t" +  "2. Rechercher un professeur.", "\t" * 3 + "*")
    print("\t" * 4 + "*" + "\t" +  "3. Enregistrer un Professeur.", "\t" * 3 + "*")
    print("\t" * 4 + "*" + "\t" +  "4. Modifier infos d'un Professeur.", "\t" * 2 + "*")
    print("\t" * 4 + "*" + "\t" + "5. Suprimer un Professeur.", "\t" * 3 + "*")
    print("\t" * 4 + "*" + "\t" +  "0. Tourner au menu principal.", "\t" * 3 + "*")
    print()
    print("\t" * 2, "*" * 75)

def adminChoice():
    """ """
    adminMenu()
    while True:
        try :
            admin_choice = int(input("\t" * 5 + "   Faites votre choix : "))
            if 0 <= admin_choice <= 5:
                return admin_choice
            print()
            print("\t" * 5 + "Veillez Saisir un entier compris entre [0, 5]") 

        except ValueError as error:
            print()
            print("\t" * 5 + f"Erreur: Veillez Saisir un entier compris entre [0, 5] ")             


def userMenu():
    """ """
    Coordinates.clear_screen()
    print("\t" * 3, "*" * 75)
    print()
    print("\t" * 4 + "*" +  "\t"  + "1. Lister les professeurs.", "\t" * 3 + "*")
    print("\t" * 4 + "*" +  "\t"  + "2. Rechercher un professeur.", "\t" * 3 + "*")
    print("\t" * 4 + "*" +  "\t"  + "3. Connecter antant qu'Administrateur.", "\t" * 2 + "*")
    print("\t" * 4 + "*" +  "\t"  + "0. Laisser le Programme.", "\t" * 3 + "*")
    print()
    print("\t" * 3, "*" * 75)

def userChoice():
    """ """
    userMenu()
    while True:
        try :
            user_choice = int(input("\t" * 4 +  "\t" + "   Faites votre choix : "))
            if 0 <= user_choice <= 3:
                return user_choice
            print()
            print("\t" * 5 + "Veillez Saisir un entier compris entre [0, 3]") 

        except ValueError as error:
        
            print()
            print("\t" * 5 + f"Erreur: Veillez Saisir un entier compris entre [0, 3] ")             

def findProfessor_():
    """ """
    print()
    password = input("\t" * 5 + "Le du code Professeur : ")
    while password == "":
        print("Le code ne doit pa vide.")
        password = input("\t" * 5 + "Le du code Professeur : ")

    professor_find = professor.search_professor(password)
    print()
    if professor_find:
        print("\t" * 5, "Le professeur trouve : ")
        print("\t", "*" * 120 )
        print("\t" * 2, "{:<15}{:<15}{:<15}{:<10}{:<30}{:<15}{:<15}".format("CODE","NOM","PRENOM","SEXE","EMAIL","TELEPHONE", "CODE_COURS"))
        print()
        for coordonate in professor_find:
            print("\t" * 2, "{:<15}{:<15}{:<15}{:<10}{:<30}{:<15}{:<15}".format(coordonate[0],coordonate[1],
            coordonate[2],coordonate[3],coordonate[4],coordonate[5], coordonate[6]))

        print()
        print("\t", "*" * 120 )

    print()
    input("\t" * 5 + "Pressez ENTER pour continuer...")

def mainAdmin():
    """ """
    while True:
        admin_choice = adminChoice()
        if admin_choice == 1:
            professor.get_all_professors()
            print()
            input("\t" * 5 + "Pressez ENTER pour continuer...")

        elif admin_choice == 2:
            findProfessor_()

        elif admin_choice == 3:
            Coordinates.clear_screen()
            parameters = cordonates.get_coordinates()
            professor.add_professor(parameters)


        elif admin_choice == 4:
            pass

        elif admin_choice == 5:
            professor.get_all_professors()
            codep = input("\t" * 5 + "Le  code du Professeur : ")
            while codep == "":
                print("Le code ne doit pas vide.")
                codep = input("\t" * 5 + "Le  code du Professeur : ")
            professor.delete_professor(codep)
            print()
            input("\t" * 5 + "Pressez ENTER pour continuer...")
            professor.get_all_professors()
            print()

        else:
            Coordinates.clear_screen()
            userChoice()
        admin_choice = -1

def mainUser():
    """ """
    data.connect()
    while True:
        user_choice = userChoice()
        if user_choice == 1:
            professor.get_all_professors()
            print()
            input("\t" * 5 + "Pressez ENTER pour continuer...")
        elif user_choice == 2:
            findProfessor_()
        elif user_choice == 3:
            Coordinates.clear_screen()
            admin_name = Coordinates.validate_name("nom")
            admin_password = input("\t" * 5 + "Code d'acces : ")
            confirmation = data._hash_password(admin_password)
            if confirmation:
                Coordinates.clear_screen()
                mainAdmin()

        elif user_choice == 0:
            Coordinates.clear_screen()
            print("\t" * 5 + "Vous quittez le programme.")
            print()
            break

