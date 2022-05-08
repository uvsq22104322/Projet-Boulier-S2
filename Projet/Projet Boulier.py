import tkinter as tk

#Variables Global
DIM_BOULIER = (17,9)
WIDTH = 1300
HEIGHT = 700
ecart_width = WIDTH/DIM_BOULIER[0]
ecart_height = HEIGHT/DIM_BOULIER[1]
boules = []

#Obtenir les coordonnées et l'ID des boules 
def clic(event):
    x, y = event.x, event.y
    print("Clic en",x,",",y)
    print(canvas1.find_closest(x,y)," est l'objet cliqué.")


#Mise en place du Canvas
racine=tk.Tk()
racine.title("Projet Boulier")

canvas1 = tk.Canvas(racine, width=WIDTH, height=HEIGHT, bg="black", borderwidth=4 )

#Création des boules

def Start():
    global ID_boules
    for x in range(DIM_BOULIER[0]):
        for y in range(DIM_BOULIER[1]):
            if y == 1 or y == 3:
                ID_boules = canvas1.create_oval(x*ecart_width,y*ecart_height,x*ecart_width+ecart_width,y*ecart_height+ecart_height,fill="gray",tags="boules")
            elif y == 2:
                if y == 2 and x%3 == 1 :
                    ID_boules = canvas1.create_oval(x*ecart_width,y*ecart_height,x*ecart_width+ecart_width,y*ecart_height+ecart_height,fill="white", tag="boules")
                else :
                    ID_boules = canvas1.create_oval(x*ecart_width,y*ecart_height,x*ecart_width+ecart_width,y*ecart_height+ecart_height,fill="black")
            else:
                ID_boules = canvas1.create_oval(x*ecart_width,y*ecart_height,x*ecart_width+ecart_width,y*ecart_height+ecart_height,fill="red",tags="boules")
            boules.append(ID_boules)
    print(boules) #vérif ID_boules

#Supression des boules (pour l'instant, ne vide uniquement la liste boules)
def Clear():
    #for i in range(ID_boules):
    #    boules[i] = 0
    #    i += 1
    boules.clear()
    print(boules) #Vérif ID_boules

def callback():
    canvas1.itemconfig(ID_boules,fill='red')
    print(boules)

#Mise en place des boutons 
button1 = tk.Button(racine, text="start", bg="red", command = Start)
button2 = tk.Button(racine, text="clear", bg="red", command = callback)

#Positionnement des éléments
canvas1.grid(column=1, row=1, rowspan=9, columnspan=17)
button1.grid(column=0, row=0)
button2.grid(column=0, row=1)
canvas1.tag_bind("boules","<Button-1>",clic)

#Activation de l'interface graphique
racine.mainloop()