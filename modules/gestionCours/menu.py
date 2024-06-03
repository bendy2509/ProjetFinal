from os import system

def menu_gestion_cours():
    """Afficher le menu des cours"""
    print("\n", "*" * 10 , "Menu Gestion des Cours", "*" * 10 ,"\n")
    print("1. Enregistrer un cours")
    print("2. Afficher les cours")
    print("3. Modifier un cours")
    print("4. Rechercher un cours")
    print("5. Retour au menu principal")

    choice = int(input("\nEntrez votre choix : "))
    return choice

def menu_cours(manager):
    """menu cours"""
    while True:
        choice = menu_gestion_cours()
        system("cls")
        if choice == 1:
            manager.enregistrer_cours()
        elif choice == 2:
            manager.afficher_cours()
        elif choice == 3:
            manager.modifier_cours()
        elif choice == 4:
            manager.rechercher_cours()
        elif choice == 5:
            break
        else:
            print("Choix invalide. Veuillez réessayer...\n")
