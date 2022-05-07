import tkinter as tk

racine=tk.Tk()
racine.title("Projet Boulier")

i=0
y=1
x=1

#1er essai:

#def Start():
#    for i in range(136):
#        canvas1.create_oval(x,y, fill="red")
#        if y%8==0:
#                x += 1
#                y += 1
#        else:
#                y += 1
#        i += 1

#2eme essai

def Start():
        pass



canvas1 = tk.Canvas(racine, width=1300, height=700, bg="black", borderwidth=4 )
button1 = tk.Button(racine, text="start", bg="red", command = Start)

canvas1.grid(column=1, row=1, rowspan=9, columnspan=17)
button1.grid(column=0, row=0)


racine.mainloop()




#test if :
DIM_BOULIER = (17,9)
WIDTH = 1300
HEIGHT = 700
ecart_width = WIDTH/DIM_BOULIER[0]
ecart_height = HEIGHT/DIM_BOULIER[1]


def Start():
    for x in range(DIM_BOULIER[0]):
        for y in range(DIM_BOULIER[1]):
            if y == 1 or y == 3:
                canvas1.create_oval(x*ecart_width,y*ecart_height,x*ecart_width+ecart_width,y*ecart_height+ecart_height,fill="gray",tags="boules")
            elif y == 2:
                        if y == 2 and x%3 == 0 :
                                canvas1.create_oval(x*ecart_width,y*ecart_height,x*ecart_width+ecart_width,y*ecart_height+ecart_height,fill="white")
                        else :   
                                canvas1.create_oval(x*ecart_width,y*ecart_height,x*ecart_width+ecart_width,y*ecart_height+ecart_height,fill="black")
            else:
                canvas1.create_oval(x*ecart_width,y*ecart_height,x*ecart_width+ecart_width,y*ecart_height+ecart_height,fill="red",tags="boules")


