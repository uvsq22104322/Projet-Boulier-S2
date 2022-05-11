# Projet-Boulier-S2

#########################################
# groupe BI TD04

# Ana Wassaf 
# Cyriac Thibaudeau 
# Kimbounou Prunelle S Sekongo
# Samy Kolli

# https://github.com/uvsq22104322/Projet-Boulier-S2
#########################################
# sujet de projet : simulation d'un boulier "Soroban"


## Langage et interface utilisés : Python 3.9.7 et Tkinter


### Table des matières
# 1. Mode simulation (attribuée à Ana Wassaf et Cyriac Thibaudeau)
# - Affichage du cadre et des boules 
#   - création d'un dictionnaire pour repérer les boules grâce à leur clé (fonction gestion)
#   - matrice affichant les boules et les tiges (fonction affiche_boulier)
# - Modification de la dimension du boulier 
#   - création d'une zone de texte en interaction avec l'utilisateur 
# reliée à la matrice affichant le boulier (fonction affiche_boulier)
# - Changement de couleur des boules (non entamé)
# - Déplacement des boules (non achevé)
# - Modification de la vitesse des déplacements (non entamé)
# - Enregistrer la position des boules dans un fichier .txt (non achevé)
# - Réintialisation des boules (non achevé)

# 2. Mode opération (attribuée à Kimbounou Prunelle S Sekongo et Samy Kolli)
# - Pas d'interaction possible avec les boules
# - Soustraction et addition avec le boulier (non achevé)
# - Multiplication et division avec le boulier (non entamé)


#### Fonctionnement 
# Après exécution du script dans un terminal :
# Affichage d'un boulier avec la plus petite dimension possible
# Saisir un nombre entier dans la zone de texte 
# Appuyer sur le bouton "dimension" pour augmenter/diminuer le nombre de tiges
# Appuyer sur le bouton "sauvegarder" pour enregistrer les clés 
# et les coordonnées des boules dans un fichier .txt
# le déplacement des boules n'étant pas rédigé, il n'est pas possible de réinitialiser le boulier.


##### Statut du projet
# Première et Deuxième partie pas achevées dans le temps imparti
# Erreurs présentes dans les fonctions : 
# - Fonctions pour déplacer les boules : ev_boules, deplace_colonne et mvt_balle
# - Fonction pour additionner et soustraire : operation
# - Fonction pour enregistrer les données des boules dans un fichier après leur déplacement