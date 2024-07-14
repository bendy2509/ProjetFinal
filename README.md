# Projet Final - Gestion des Salles et des Cours

## Introduction
Ce projet vise à gérer les bâtiments, les salles et les cours du CHC-UEH-L, facilitant l'organisation des ressources pour les administrateurs et les professeurs.

## Fonctionnalités

### Interface de Départ (main.py)
Lorsque vous lancez l'application à l'aide du fichier `main.py`, l'interface de départ guide l'utilisateur à travers plusieurs étapes pour utiliser les fonctionnalités du système :

1. **Menu de Configuration Initial** :
   - L'utilisateur a le choix entre :
     - Se connecter en tant qu'administrateur : il devra fournir une adresse e-mail et un mot de passe pour accéder aux fonctionnalités avancées.
     - Créer un compte administrateur : s'il n'existe pas encore de comptes administrateurs dans la base de données, l'utilisateur peut en créer un en fournissant les informations nécessaires.
     - Se connecter en tant qu'invité : les fonctionnalités de modification, suppression et enregistrement sont restreintes dans tous les modules.

2. **Gestion des Cours, Salles, Bâtiments, Professeurs et Horaires** :
   - Chaque section du menu principal (de 1 à 6) offre des fonctionnalités spécifiques pour gérer les ressources éducatives.
   - Les actions disponibles varient selon le type d'utilisateur :
     - **Administrateur** : a accès à toutes les fonctionnalités du système, y compris la création, modification et suppression de données.
     - **Invité** : peut uniquement consulter les données existantes sans possibilité de les modifier.

Ce modèle d'accès garantit que les administrateurs peuvent pleinement gérer les ressources éducatives tandis que les invités ont un accès limité aux fonctions d'observation uniquement.

# Menu Gestion des Bâtiments

## Options Disponibles

1. **Enregistrer un bâtiment (admin)** : Permet à un administrateur d'enregistrer un nouveau bâtiment dans le système.

2. **Ajouter une salle à un bâtiment (admin)** : Permet à un administrateur d'ajouter une nouvelle salle à un bâtiment existant.

3. **Modifier le nom d'un bâtiment (admin)** : Permet à un administrateur de modifier le nom d'un bâtiment déjà enregistré dans le système.

4. **Afficher les bâtiments** : Affiche la liste de tous les bâtiments enregistrés dans le système, avec leurs salles associées.

5. **Supprimer un bâtiment (admin)** : Permet à un administrateur de supprimer complètement un bâtiment et toutes les salles qui lui sont associées.

6. **Retour au menu principal** : Permet de retourner au menu principal où d'autres options de gestion sont disponibles.

### Gestion des Salles
- **Ajout de salles** : Ajoute des salles à un bâtiment avec des détails comme le numéro, le type, la capacité et l'étage.
- **Affichage des salles** : Affiche toutes les salles d'un bâtiment spécifique.

## Menu Gestion des Cours

# Options Disponibles

1. **Enregistrer un cours (Admin)** : Permet à un administrateur d'enregistrer un nouveau cours dans le système.

2. **Lister les cours** : Affiche la liste de tous les cours enregistrés dans le système.

3. **Modifier un cours (Admin)** : Permet à un administrateur de modifier les détails d'un cours existant, comme son nom, sa durée, etc.

4. **Rechercher un cours** : Permet de rechercher un cours spécifique dans la base de données en utilisant son code ou son nom.

5. **Assigner un professeur à un cours (Admin)** : Permet à un administrateur d'assigner un professeur à un cours existant. Vérifie d'abord si le cours n'a pas déjà de professeur assigné.

6. **Filtrer par les cours ayant des professeurs** : Affiche uniquement les cours qui ont déjà un professeur assigné.

7. **Filtrer par les cours qui n'ont pas de professeur** : Affiche uniquement les cours qui n'ont pas encore de professeur assigné.

0. **Retour au menu principal** : Permet de revenir au menu principal où d'autres options de gestion sont disponibles.

# Menu Gestion des Professeurs

## Options Disponibles

1. **Enregistrer un Professeur (Admin)** : Permet à un administrateur d'enregistrer un nouveau professeur dans le système.

2. **Lister les professeurs** : Affiche la liste de tous les professeurs enregistrés dans le système.

3. **Rechercher un professeur** : Permet de rechercher un professeur spécifique dans la base de données.

4. **Modifier les informations d'un Professeur (Admin)** : Permet à un administrateur de modifier les informations (nom, email, etc.) d'un professeur existant.

5. **Supprimer un Professeur (Admin)** : Permet à un administrateur de supprimer complètement un professeur de la base de données.

0. **Retour au menu principal** : Permet de retourner au menu principal où d'autres options de gestion sont disponibles.

# Menu Gestion des Salles

## Options Disponibles

1. **Lister les salles d'un bâtiment** : Affiche toutes les salles disponibles dans un bâtiment spécifique.

2. **Ajouter une salle dans un bâtiment (Admin)** : Permet à un administrateur d'ajouter une nouvelle salle à un bâtiment existant.

3. **Supprimer une salle d'un bâtiment (Admin)** : Permet à un administrateur de supprimer une salle spécifique d'un bâtiment. Cette action supprime également tous les horaires associés à cette salle.

4. **Retour au menu principal** : Permet de retourner au menu principal où d'autres options de gestion sont disponibles.
# Menu Gestion des Horaires

## Options Disponibles

1. **Enregistrer une horaire (Admin)** : Permet à un administrateur d'enregistrer un nouvel horaire pour une salle et un cours spécifiques.

2. **Afficher l'horaire d'une salle** : Affiche l'horaire complet d'une salle donnée, indiquant les jours de la semaine, les heures de début et de fin, ainsi que les détails du cours associé.

3. **Vérifier la disponibilité d'une salle** : Permet de vérifier si une salle est disponible à un horaire spécifique avant d'y programmer un cours.

4. **Supprimer horaires par salle (Admin)** : Permet à un administrateur de supprimer tous les horaires associés à une salle spécifique. Cette action est irréversible.

5. **Supprimer horaire par ID (Admin)** : Permet à un administrateur de supprimer un horaire spécifique en utilisant son identifiant unique. Cette action est irréversible.

6. **Retour au menu principal** : Permet de retourner au menu principal où d'autres options de gestion sont disponibles.

# Menu Gestion des Administrateurs

## Options Disponibles

1. **Ajouter un administrateur** : Permet d'ajouter un nouvel administrateur au système en spécifiant son email et son mot de passe.

2. **Lister les administrateurs** : Affiche la liste de tous les administrateurs enregistrés dans le système, avec leurs informations de base.

3. **Supprimer un administrateur** : Permet de supprimer un administrateur existant du système. Cette action est irréversible.

4. **Retourner au menu principal** : Permet de retourner au menu principal où d'autres options de gestion sont disponibles.

### Contraintes
- **Bâtiments** :
    - Un bâtiment peut avoir jusqu'à 18 salles réparties sur 3 étages.
    - Supprimer un bâtiment supprime toutes les salles associées ainsi que leurs horaires.
- **Salles** :
    - Les salles d'un bâtiment sont stockées dans une base de données SQLite.
    - Supprimer une salle supprime également tous les horaires associés à cette salle.
- **Professeurs et Cours** :
    - Les codes des professeurs et des cours doivent être uniques.
    - Un cours ne peut pas avoir plus d'un professeur assigné à la fois.

## Utilisation
Veuillez utiliser l'un de ces comptes pour connecter en tant que admin:
- email: bendy.servilus@student.ueh.edu.ht
- password: Servilus_2509

- email: blemy.joseph@student.ueh.edu.ht
- password: Blemy_001

- email : albikendy.jean@student.ueh.edu.ht
- password: pythons&Albe--}

- email: dually.dagobert@student.ueh.edu.ht
- password: ATEIEIZ9mike

1. **Enregistrer un bâtiment** : Fournit le nom du bâtiment pour l'ajouter à la base de données.
2. **Ajouter des salles à un bâtiment** : Sélectionne un bâtiment existant et ajoute des salles avec les informations requises.
3. **Enregistrer des cours** : Ajoute des cours avec tous les détails nécessaires pour les identifier.
4. **Assigner un professeur à un cours** : Assigne un professeur existant à un cours en vérifiant les conflits.
5. **Afficher et gérer les horaires** :
    - **Consulter les horaires des salles** : Affiche les horaires actuellement enregistrés pour une salle spécifique.
    - **Vérifier la disponibilité des salles** : Avant d'ajouter un cours, vérifie si une salle est libre à un moment donné.
    - **Supprimer des horaires** : Permet de supprimer tous les horaires associés à une salle ou un horaire spécifique par son ID.

## Installation
Clonez le repository et suivez les instructions pour configurer l'environnement de développement et la base de données.

```bash
git clone https://github.com/bendy2509/ProjetFinal.git
cd ProjetFinal
