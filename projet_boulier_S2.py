############################
# Particpants : Ana Wassaf, Cyriac Thibaudeau, Kimbounou Prunelle S Sekongo, Samy Kolli
############################

############################
# Import de la librairie

import tkinter as tk 

############################
# Définition des constantes

# rayon des boules
r_boule = 50
# nombre de tiges dans le dictionnaire
n = 17

# hauteur du canevas
HAUTEUR = 600
# taille du canevas
LARGEUR = r_boule * n + 115

# position de la barre médiane
xA, yA, xB, yB = 10, 120, r_boule * 17 + 115, 120
# position du cadre du boulier
xCadre, yCadre, x1Cadre, y1Cadre = 10, 7, r_boule * 17 + 115, 600
# position des tiges des bouliers
xTige, yTige, x1Tige1, y1Tige1 = 45, 12, 45, HAUTEUR-10
# position des unaires et des quinaires
xBoule, yBoule, x1Boule, y1Boule = 20, HAUTEUR-5, 70, HAUTEUR-55
xBoule1, yBoule1, x1Boule1, y1Boule1 = 20 , 10, 70, 60

############################
# fonctions 

boule = {}

# MODE SIMULATION

               
def affiche_boulier() :
    """affiche la dimension du boulier selon 
    la demande de l'utilisateur"""
    global boule, cadre, I
    gestion(n)

    if I == True:
        q = 17
        I = False
    else :
        q = int(z_texte.get(index1 = "1.0", index2 = "end-1c"))   
        for i in boule : 
            canvas.delete("pre")

    for i in range(q): 
            liste1 = []
            canvas.create_line(xTige + i*55, yTige, x1Tige1+ i*55, y1Tige1, fill = '#F5F5DC', width = 3, tags = "pre")
            for a in range(5):
                x0,y0,x1,y1= xBoule + i*55, yBoule-a*55, x1Boule + i*55, y1Boule-a*55 
                tag=str(i+1)+"00"+str(a+1)
                liste1.append(canvas.create_oval( x0,y0,x1,y1, fill = 'black', tags="pre"))
                boule[f"{xBoule + i*55},{yBoule-a*55},{x1Boule + i*55},{y1Boule-a*55}"]=[tag]

            x0,y0,x1,y1= xBoule + i*55, yBoule1, x1Boule + i*55, y1Boule1
            tag=str(i+1)+"00"+str("e")
            liste1.append(canvas.create_oval( xBoule + i*55, yBoule1, x1Boule + i*55, y1Boule1, fill = 'black', tag =str(i+1)+"00"+"e", tags = "pre" ))
            boule[f"{xBoule + i*55},{yBoule1},{x1Boule + i*55},{y1Boule1}"]=[tag]

    canvas.config(height = HAUTEUR, width = 70+q*55)
    canvas.itemconfigure(tagOrId='cadre', fill= "white") 
    cadre = canvas.create_rectangle (xCadre, yCadre, 20+q*55, y1Cadre, width = 6, outline = 'maroon', tags = "pre")
    canvas.create_line(xA, yA, 20+q*55, yB, fill = 'maroon', width = '10', tags="pre")        

def init_boulier():
    """affiche un boulier avec les boules désactivées"""
    for i in range(q):
            liste1 = []
            for a in range(5):
                x0,y0,x1,y1= xBoule + i*55, yBoule1, x1Boule + i*55, y1Boule1
                canvas.create_oval(xBoule + i*55, yBoule-a*55, x1Boule + i*55, y1Boule-a*55, fill = 'black')
                liste1.append(canvas.create_oval( x0,y0,x1,y1, fill = 'black')) 

#def affiche_boulier2():
#    boules = []
#    q = int(z_texte.get(index1 = "1.0", index2 = "end-1c"))   
#    for i in range(q):
#        liste1 = []
#        for j in range(5):
#            liste1.append(canvas.create_oval(i*55, HAUTEUR-(i+j)*55, i+1*55, HAUTEUR-(j*55) ))
#            boule.append(liste1)
#    canvas.boule([i][j], 0, 55)


#def deplace_colonne(boule):
#    """sélectionne les boules 
# et les déplace les boules sélectionnées"
#    canvas.move(boule, 0, 55 * 6)
#    for i in range(5):
#        tag = str(colonne) + "00"+ str(i)
#        for j in boule :
#            if tag == j:
#                mvt_balle(j)
#    print(j)


def couleur_b():
    """"change de couleur les balles sélectionnées"""  
    pass


def gestion(q):
    """dictionnaire de boule"""
    global boule
    for i in range(q):
        for a in range(11):
            boule[f"{xBoule1 + i*55},{yBoule1-a*55},{x1Boule1 + i*55},{y1Boule1-a*55}"]=[None]


#def ev_boules(e) : 
#    """active les boules quand on clique dedans"""
#    global z_texte,n,boule
#    px, py =e.x, e.y
#    a,b=0,0
#    if px < 20+int(z_texte.get("1.0", "end"))*55:
#        a=int((px//55)*55+20)
#        b=int((py//55+1)*55-10)
#        if boule[f"{a},{b},{a+50},{b+50}"] !=None:
#             deplace_colonne(boule[f"{a},{b},{a+50},{b-50}"])


def sauvegarde():
    """ Ecrit le dictionnaire boule
        dans le fichier Boulier.txt
    """
    list(boule)
    fic = open("Boulier.txt", "w")
    fic.write(str(boule) + "\n")
    for i in range(q):
        for a in range(11):
            fic.write((f"{xBoule + i*55},{yBoule-a*55},{x1Boule + i*55},{y1Boule-a*55}") + "\n")
    fic.close()    


def load():
    """Lit le fichier Boulier.txt, met à jour les variables
    et modifie l'affichage
    """
    fic = open("Boulier.txt", "r")
    ligne = fic.readline()
    N = int(ligne)
    init_boulier()
    for ligne in fic:
        pass
    fic.close()
    affiche_boulier()

# MODE OPÉRATION
def calcul_e():
    "affiche les étapes des opérations"

############################
# programme principal 

# défintion des widgets
racine = tk.Tk()
racine.title(' Boulier type "Soroban" ')
canvas = tk.Canvas(racine, height = HAUTEUR, width = LARGEUR, bg = 'white')
dim = tk.Button(racine, text = "dimension", command = affiche_boulier )
res = tk.Button(racine, text = "reset", command = init_boulier)
sauv = tk.Button(racine, text = "sauvegarder", command = sauvegarde )

# permet à affiche_boulier() d'afficher un nouveau boulier en enlevant l'ancien
I = True
cadre = affiche_boulier()
I = False

# pour changer la dimension du boulier
z_texte = tk.Text(racine, width = 12, height = 1 )
z_texte.insert("1.0", 17)
q = int(z_texte.get(index1 = "1.0", index2 = "end-1c"))
# placement des widgets
canvas.grid(rowspan= 9, column = 2, row = 0)
z_texte.grid(row = 1)
dim.grid(row = 2)
sauv.grid(row = 5)
res.grid(row = 6)

# canvas.bind("Button-1", deplace_colonne)
# racine.bind("<Button-1>", ev_boules)

racine.mainloop()