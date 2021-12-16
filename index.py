"""
Code realisé par Perrichet Théotime et Tuzio Lorenzo
le 16/12/2021

"""


from tkinter import *
import fonction as f

rayon = 10
vx1=400
vy=50
vx2=450
vx3=425
vy1=100

fen=Tk()
fen.title('Space invaders')
photo = PhotoImage(file="..\TP_SpaceVader\space_invaders_wallpaper.gif")

start = Button(fen, text='Nouvelle Partie')
start.pack(anchor=N, padx=5, pady=5)

# Création d'un widget Button (bouton quitter)
Quitter = Button(fen, text ='Quitter',command=fen.destroy)
Quitter.pack(anchor=NE, padx = 5, pady = 5)

score = Label(fen, text="Score :" , fg="black")
score.pack(anchor=N, padx = 5, pady = 5)


Largeur = 1700
Hauteur = 800
Canevas = Canvas(fen,width = Largeur, height =Hauteur)
vesseau = Canevas.create_polygon(vx1,vy1,vx2,vy1,vx3,vy,width=5,outline='black',fill='yellow')
#item = Canevas.create_image(0,10,anchor=NW, image=photo)
Canevas.bind('<Key>',f.dep_vaisseau)
Canevas.pack()

fen.mainloop()

#Canevas.coords(Vaisseau,X-rayon,Y-rayon,X+rayon,Y+rayon)
#fen.after(20,deplacement)

