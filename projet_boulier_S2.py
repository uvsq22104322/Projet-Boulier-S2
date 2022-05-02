import tkinter as tk 

n = 17

# constantes
r_boule = 50
HAUTEUR = 600
LARGEUR = r_boule * n + 115
# coordonnées barre médiane
x0, y0, x1, y1 = 10, 120, r_boule * 17 + 115, 120
# dimension cadre
xCadre, yCadre, x1Cadre, y1Cadre = 10, 10, r_boule * 17 + 115, 600
# dimension lignes
xTige1, yTige1, x1Tige1, y1Tige1 = 45, 12, 45, HAUTEUR-10
xTige2, yTige2, x1Tige2, y1Tige2 = 100, 12, 100, HAUTEUR-10
# dimension boules
xBoule1, yBoule1, x1Boule1, y1Boule1 = 20, HAUTEUR-5, 70, HAUTEUR-55
xBoule2, yBoule2, x1Boule2, y1Boule2 = 20, HAUTEUR-55, 70, HAUTEUR-105
xBoule3, yBoule3, x1Boule3, y1Boule3 = 20, HAUTEUR-105, 70, HAUTEUR-155
xBoule4, yBoule4, x1Boule4, y1Boule4 = 20, HAUTEUR-155, 70, HAUTEUR-205
xBoule5, yBoule5, x1Boule5, y1Boule5 = 20, HAUTEUR-205, 70, HAUTEUR-255
xBoule6, yBoule6, x1Boule6, y1Boule6 = 20 , 10, 70, 60

########## fonctions ##########
boule={}
# MODE SIMULATION

def generation_boules(n) :
    global boule
    for i in range(n): 
        liste1 = []
        for a in range(5):
            x0,y0,x1,y1= xBoule1 + i*55, yBoule1-a*55, x1Boule1 + i*55, y1Boule1-a*55
            tag=str(i+1)+"00"+str(a+1)
            liste1.append(canvas.create_oval( x0,y0,x1,y1, fill = 'black', tags=tag))
            boule[f"{xBoule1 + i*55},{yBoule1-a*55},{x1Boule1 + i*55},{y1Boule1-a*55}"]=[tag]
        x0,y0,x1,y1= xBoule1 + i*55, yBoule6, x1Boule1 + i*55, y1Boule6
        tag=str(i+1)+"00"+str("e")
        liste1.append(canvas.create_oval( xBoule1 + i*55, yBoule6, x1Boule1 + i*55, y1Boule6, fill = 'black', tags=str(i+1)+"00"+"e" ))
        boule[f"{xBoule1 + i*55},{yBoule6},{x1Boule1 + i*55},{y1Boule6}"]=[tag]


def tiges(n) :
    tiges = []
    for i in range(n):
        canvas.create_line(xTige1 + i*55, yTige1, x1Tige1+ i*55, y1Tige1, fill = '#F5F5DC', width = 3, tags="tiges" )


def init_boulier(n):
    "affiche un nouveau boulier selon la dimension choisie"
    gestion(n)
    tiges(n)
    generation_boules(n)
    da=(17,21,23)
    if n in da :
        "le boulier se supprime et affiche un nouveau boulier avec 17 tiges"
        canvas.config(height = HAUTEUR, width = 70+n*55)
        canvas.itemconfigure(tagOrId='cadre', fill= "white") 
        canvas.create_rectangle (xCadre, yCadre, 20+n*55, y1Cadre, width = 6, outline = 'maroon', tags = "cadre")
        canvas.create_line(x0, y0, 20+n*55, y1, fill = 'maroon', width = '10', tags="cadre")


def gestion(n):
    global boule
    for i in range(n):
        for a in range(11):
            boule[f"{xBoule1 + i*55},{yBoule1-a*55},{x1Boule1 + i*55},{y1Boule1-a*55}"]=[None]


def ev_boules(e) : 
    global z_texte,n,boule
    "quand on clique sur une boule on l'active. Sélectionner les boules grâce à leur indice dans leur liste"
    "quand la boule est activée on peut la déplacer vers le haut/vers le bas. Elle bouge les autres boules avec elle"
    "elle-s change-nt de couleur. boule['fill']=red"
    px, py =e.x, e.y
    a,b=0,0
    if px < 20+int(z_texte.get("1.0", "end"))*55:
        a=int((px//55)*55+20)
        b=int((py//55+1)*55-10)
        if boule[f"{a},{b},{a+50},{b-50}"] !=None:
            ahhhhhhhhhh()


def ahhhhhhhhhh():
    """movement de chaque balle"""
    pass


def ohhhhhh():
    """calcul l'ensemble des balle impliquer dans le mouvement et les change de couleur avec ehhhhhhhhhhhhhhhhhhhhhh()"""
    pass


def ehhhhhhhhhhhhhhhhhhhhhh():
    """"change de couleur les balles et les fait bouger"""
    pass


# MODE OPÉRATION
def calcul_e():
    "affiche les étapes des opérations"

########## affichage de base ##########
racine = tk.Tk()
racine.title(' Boulier type "Soroban" ')
canvas = tk.Canvas(racine, height = HAUTEUR, width = LARGEUR, bg = 'white')
racine.bind("<Button-1>", ev_boules)
# pour changer la dimension du boulie
z_texte = tk.Text(racine, height = 1, width = 10)
z_texte.insert(tk.INSERT, "17")
taille = tk.Button(racine, text = 'dimension du boulier', command = init_boulier(int(z_texte.get("1.0", "end"))))
# positionnement des widgets
canvas.grid(rowspan= 5, columnspan= 2)
taille.grid(row = 0, column = 2)
z_texte.grid(row = 1, column = 2)
racine.mainloop()