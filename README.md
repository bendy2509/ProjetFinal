# Projet Final - Gestion des Salles et des Cours

#Introduction
Ce projet permet de gérer les bâtiments, les salles et les cours d'un établissement. Il est conçu pour être utilisé par des administrateurs et des professeurs afin d'organiser les ressources de manière efficace.

# Fonctionnalités

# Gestion des Bâtiments
- Enregistrement d'un bâtiment : Un bâtiment est ajouté avec son nom uniquement.
- Affichage des bâtiments : Afficher tous les bâtiments ainsi que les salles associées.
- Recherche de bâtiments : Permet de rechercher un bâtiment spécifique.

# Gestion des Salles
- Ajout de salles : Les salles peuvent être ajoutées à un bâtiment. Chaque salle stocke des informations telles que son numéro, le type, la capacité et l'étage.
- Affichage des salles : Afficher toutes les salles d'un bâtiment spécifique.

# Gestion des Cours
- Enregistrement d'un cours : Un cours peut être enregistré avec des détails comme le nom, le code, la durée, la session et l'année.
- Affichage des cours : Afficher tous les cours enregistrés.
- Assignation de professeur à un cours : Les professeurs peuvent être assignés à des cours. Une vérification est faite pour s'assurer que le cours n'a pas déjà un professeur assigné.
- Liste des cours assignés/non assignés : Afficher les cours en fonction de leur assignation à un professeur.

# Gestion des Horaires
- Affichage des horaires : Afficher l'horaire d'une salle sous forme de tableau avec les jours de la semaine et les heures.
- Vérification de disponibilité : Vérifier si une salle est disponible à un horaire donné avant d'ajouter un cours à cet horaire.

# Contraintes
- Bâtiments : Un bâtiment peut avoir jusqu'à 18 salles réparties sur 3 étages.
- Salles : Les salles d'un bâtiment sont stockées dans une base de données SQLite.
- Professeurs et Cours : Les codes des professeurs et des cours doivent être uniques. Les cours ne peuvent pas avoir plus d'un professeur assigné.

# Utilisation
1. Enregistrer un bâtiment : Fournir le nom du bâtiment.
2. Ajouter des salles à un bâtiment : Sélectionner un bâtiment et ajouter des salles avec les informations requises.
3. Enregistrer des cours : Ajouter des cours avec les détails nécessaires.
4. Assigner un professeur à un cours : Vérifier et assigner un professeur à un cours en s'assurant qu'il n'est pas déjà assigné.
5. Afficher et gérer les horaires : Consulter et gérer les horaires des salles.

# Installation
Clonez le repository et suivez les instructions pour configurer l'environnement de développement et la base de données.

```bash
git clone https://github.com/bendy2509/ProjetFinal.git
cd ProjetFinal
