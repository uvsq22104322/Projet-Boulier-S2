import tkinter as tk 

# constantes
r_boule = 50
HAUTEUR = 600
LARGEUR = r_boule * 17 + 115


# coordonnées barre médiane
x0, y0, x1, y1 = 10, 120, r_boule * 17 + 115, 120
# dimension cadre
xCadre, yCadre, x1Cadre, y1Cadre = 10, 10, r_boule * 17 + 115, 600
# dimension ligne
xTige1, yTige1, x1Tige1, y1Tige1 = 45, 10, 45, HAUTEUR-10
xTige2, yTige2, x1Tige2, y1Tige2 = 100, 10, 100, HAUTEUR-10

# dimension boule
xBoule1, yBoule1, x1Boule1, y1Boule1 = 20, HAUTEUR-5, 70, HAUTEUR-55
xBoule2, yBoule2, x1Boule2, y1Boule2 = 20, HAUTEUR-55, 70, HAUTEUR-105
xBoule3, yBoule3, x1Boule3, y1Boule3 = 20, HAUTEUR-105, 70, HAUTEUR-155
xBoule4, yBoule4, x1Boule4, y1Boule4 = 20, HAUTEUR-155, 70, HAUTEUR-205
xBoule5, yBoule5, x1Boule5, y1Boule5 = 20, HAUTEUR-205, 70, HAUTEUR-255
xBoule6, yBoule6, x1Boule6, y1Boule6 = 20 , 10, 70, 60

# fonctions
def dimension_boulier(n) :
        "affiche boulier avec différentes dimensions"
        canvas.config(cadre, height = HAUTEUR, width = r_boule * n + 115)
        
def petit() :
    dimension_boulier(17)

def moyen() :
    dimension_boulier(21)

def grand() :
    dimension_boulier(23)
def ahhhhhh():
    pass

def boules() :
    list1 = []    
    for i in range(17): 
        for j in range(6):
            canvas.create_oval( xBoule1 + i*55, yBoule1, x1Boule1 + i*55, y1Boule1, fill = 'black' )
            canvas.create_oval( xBoule2 + i*55, yBoule2, x1Boule2 + i*55, y1Boule2, fill = 'black' )
            canvas.create_oval( xBoule3 + i*55, yBoule3, x1Boule3 + i*55, y1Boule3, fill = 'black' )
            canvas.create_oval( xBoule4 + i*55, yBoule4, x1Boule4 + i*55, y1Boule4, fill = 'black' )
            canvas.create_oval( xBoule5 + i*55, yBoule5, x1Boule5 + i*55, y1Boule5, fill = 'black' )
            canvas.create_oval( xBoule6 + i*55, yBoule6, x1Boule6 + i*55, y1Boule6, fill = 'black' )
        pass

def tiges() :
    for i in range(17):
        for j in range(6):
            canvas.create_line( xTige1, yTige1, x1Tige1, y1Tige1, fill = '#F5F5DC', width = 3)
            canvas.create_line( xTige2, yTige2, x1Tige2, y1Tige2, fill = '#F5F5DC', width = 3)

        

### 

racine = tk.Tk()
racine.title(' Boulier type "Soroban" ')
canvas = tk.Canvas(racine, height = HAUTEUR, width = LARGEUR, bg = 'white')
barre_mediane = canvas.create_line(x0, y0, x1, y1, fill = 'maroon', width = '10')

# éxécution des fonctions

tiges()
cadre = canvas.create_rectangle (xCadre, yCadre, x1Cadre, y1Cadre, width = 6, outline= 'maroon' )
boules()
# affichage du menu
frame = tk.Frame (racine, height = 50, width = 100, padx = 5, pady = 15)
OngletA = tk.Menubutton ( frame , text = "Nombres de colonnes" )
MNU_OptionA = tk.Menu ( OngletA )
MNU_OptionA.add_command ( label = "17 colonnes" , command = ahhhhhh() )
MNU_OptionA.add_command ( label = "21 colonnes" , command = ahhhhhh() )
MNU_OptionA.add_command ( label = "23 colonnes" , command = ahhhhhh() )
OngletA [ "menu" ] = MNU_OptionA

frame.grid ( row = 0 , column = 1)
OngletA.grid ( row = 0 , column = 0 )
canvas.grid()

racine.mainloop()