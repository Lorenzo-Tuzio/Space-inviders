"""
Code realisé par Perrichet Théotime et Tuzio Lorenzo
le 16/12/2021

"""

from tkinter import *
import fonction as f

def Clavier(event): #Gestion de l'évenement Appui sur une touche du clavier
    global PosX,PosY
    touche=event.keysym
    #déplacement vers la droite
    if touche== 'd' :
        if PosX<1650:
            PosX+=10
    #déplacement vers la gauche
    if touche=='q' :
        if PosX>50:
            PosX-=10
    if touche=='l':
        CreationTir()
        MouvTir()
    #on dessine le vaisseau à sa nouvelle place
    Canevas.coords(Vaisseau,PosX,PosY)

def CreationTir():
    global PosX,PosY,Laser,VerifLaser
    XLaser=PosX
    YLaser1=PosY
    Laser=Canevas.create_image(XLaser,YLaser1,image=Arc)

    
def MouvTir():
    global touche,YLaser,Laser,VerifLaser
    if VerifLaser:
        if Canevas.coords(Laser)[1]<=100:
            Canevas.bind('s',Clavier)
            Canevas.delete(Laser)
            VerifLaser=True
        else :
            Canevas.move(Laser,0,-10)
            fen.after(10,MouvTir)

#Création aliens
al=PhotoImage(file='enemy.gif')
def CreationAliens(X,Y):
    Alien=Canevas.create_image(X,Y,anchor=NW,image=al)
    return Alien
Aliens=""
TirAlien=[]

class vaisseau:
    def__init__(self,PosX,PosY):
        self.PosX=PosX
        self.PosY=PosY
    
    def Clavier(event): #Gestion de l'évenement Appui sur une touche du clavier
    touche=event.keysym
    #déplacement vers la droite
    if touche== 'd' :
        if PosX<1650:
            PosX+=10
    #déplacement vers la gauche
    if touche=='q' :
        if PosX>50:
            PosX-=10
    if touche=='l':
        CreationTir()
        MouvTir()
    #on dessine le vaisseau à sa nouvelle place
    Canevas.coords(Vaisseau,PosX,PosY)



fen=Tk()
fen.title('Space invaders')
photo = PhotoImage(file="space_invaders_wallpaper.gif")


Largeur = 1700
Hauteur = 800
Canevas = Canvas(fen,width = Largeur, height =Hauteur)
# vesseau = Canevas.create_polygon(vx1,vy1,vx2,vy1,vx3,vy,width=5,outline='black',fill='yellow')
item = Canevas.create_image(0,0,anchor=NW, image=photo)


Dab=PhotoImage(file='player.gif')
Arc=PhotoImage(file='laser.gif')

#Création vaisseau
PosX=450
PosY=750
Vaisseau=Canevas.create_image(PosX,PosY,image=Dab)
Canevas.focus_set()
Canevas.bind('d',Clavier)
Canevas.bind('q',Clavier)
Canevas.bind('l',Clavier)
Canevas.pack()

VerifLaser=True
YLaser=750

fen.mainloop()


#Canevas.coords(Vaisseau,X-rayon,Y-rayon,X+rayon,Y+rayon)
#fen.after(20,deplacement)

