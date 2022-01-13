"""
Code realisé par Perrichet Théotime et Tuzio Lorenzo
le 16/12/2021

"""

from tkinter import *
import fonction as f
from random import *

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
        DestructionLaser()
    #on dessine le vaisseau à sa nouvelle place
    Canevas.coords(Vaisseau,PosX,PosY)

def CreationTir():
    global PosX,PosY,Laser,VerifLaser
    XLaser=PosX
    YLaser1=PosY
    Laser=Canevas.create_image(XLaser,YLaser1,image=Arc)
    VerifLaser=True

    
def MouvTir():
    global touche,YLaser,Laser,VerifLaser
    if VerifLaser:
        if Laser and Canevas.coords(Laser)[1]<=0:
            Canevas.delete(Laser)
        else :
            Canevas.move(Laser,0,-10)
            fen.after(10,MouvTir)

#Déplacement de l'alien
def deplacementAl():
    global X,Y,dX,dY,Largeur,Hauteur
    TailleAlien=50
    XP=Canevas.coords(Aliens[0][0])[0]
    XD=Canevas.coords(Aliens[0][-1])[0]
    #rebond à gauche
    if XP+dX<0:
        X=0
        dX=-dX
        Y+=TailleAlien
    #rebond à droite
    if XD+TailleAlien+dX>Largeur:
        X=Largeur-TailleAlien-500
        dX=-dX
        Y+=TailleAlien
    #nouvelle direction
    X=X+dX
    Y=Y+dY
    #affichage
    for i in range(len(Aliens)):
        for j in range(len(Aliens[i])):
            Canevas.coords(Aliens[i][j],X+j*100,Y+i*100)
    if Y>=700:
        Canevas.unbind('l')
    #déplacement
    fen.after(40,deplacementAl)

def CreationTirAlien():
    global Aliens,TirAlien,YAlien
    i=randint(0,len(Aliens)-1)
    j=randint(0,len(Aliens[i])-1)
    XAlien=Canevas.coords(Aliens[i][j])[0]
    YAlien=Canevas.coords(Aliens[i][j])[1]
    TirAlien.append(Canevas.create_image(XAlien,YAlien,image=Arc))
    DestructionTirAlien()
    fen.after(1000,CreationTirAlien)

def MouvTirAlien():
    global Aliens,TirAlien,YAlien
    for k in range(len(TirAlien)-1):
        if Canevas.coords(TirAlien[k])[1]==900:
            Canevas.delete(TirAlien[k])
            TirAlien.pop(k)
        else : 
            Canevas.move(TirAlien[k],0,10)
    fen.after(10,MouvTirAlien)

def DestructionLaser():
    global Laser,TirAlien,Aliens,Ilots,Vaisseau,VerifLaser,Score,Morts
    #on cherche les éléments qui ont la même position que le laser
    x1Laser=Canevas.coords(Laser)[0]
    y1Laser=Canevas.coords(Laser)[1]
    x2Laser=x1Laser+20
    y2Laser=y1Laser+20
    Impact1=Canevas.find_overlapping(x1Laser,y1Laser,x2Laser,y2Laser)
    #retourne la liste des éléments touchés
    #suppression des éléments qui sont entrés en collision
    for i in Impact1:
        for i3 in Aliens:
            for j in i3:
                if  i==j:
                    Canevas.delete(j)
                    Canevas.delete(Laser)
                    Score+=50
                    Morts+=1
                    if Morts==18:
                        Canevas.create_image(0,0,anchor=NW,image=Victoire)
                    return 



def DestructionTirAlien():
    global Laser,TirAlien,Aliens,Ilots,Vaisseau,VerifLaser,Vies
    Collision=False
    #on cherche les éléments qui ont la même position que les tirs des aliens
    if len(TirAlien)!=0:
        for j in TirAlien:
            n=Canevas.coords(j)
            x1TirAlien=Canevas.coords(j)[0]
            y1TirAlien=Canevas.coords(j)[1]
            x2TirAlien=x1TirAlien+20
            y2TirAlien=x2TirAlien+20
            Impact2=Canevas.find_overlapping(x1TirAlien,y1TirAlien,x2TirAlien,y2TirAlien) #retourne la liste des éléments touchés
            #suppression des éléments qui sont entrés en collision
            for k in Impact2:
                if k==Vaisseau:
                    Vies-=1
                    Collision=True
                if Collision:
                    Canevas.delete(j)
                    TirAlien.pop(TirAlien.index(j))
                    if Vies==0:
                        Canevas.delete(k)
                        Canevas.create_image(0,0,anchor=NW,image=Defaite)
    fen.after(10,DestructionTirAlien)


fen=Tk()
fen.title('Space invaders')
photo = PhotoImage(file="space_invaders_wallpaper.gif")


Largeur = 1800
Hauteur = 800
Canevas = Canvas(fen,width = Largeur, height =Hauteur)
# vesseau = Canevas.create_polygon(vx1,vy1,vx2,vy1,vx3,vy,width=5,outline='black',fill='yellow')
item = Canevas.create_image(0,0,anchor=NW, image=photo)

start = Button(fen, text='Nouvelle Partie')
start.pack(anchor=N, padx=5, pady=5)

# Création d'un widget Button (bouton quitter)
Quitter = Button(fen, text ='Quitter',command=fen.destroy)
Quitter.pack(anchor=NE, padx = 5, pady = 5)

#Afichage score
x=StringVar()
score = Label(fen, textvariable=x , fg="black")

score.pack(anchor=NW, padx = 5, pady = 5)
Canevas.pack()

Life=[PhotoImage(file='life-1.gif'),PhotoImage(file='life-2.gif'),PhotoImage(file='life-3.gif')]
Dab=PhotoImage(file='player.gif')
Arc=PhotoImage(file='laser.gif')
bombe=PhotoImage(file='egg.gif')
Defaite=PhotoImage(file='game_over.gif')
Victoire=PhotoImage(file='Win.gif')

Vies=3
Morts=0
Score=0
vie=Canevas.create_image(0,0,anchor=NW,image=Life[Vies-1])
Canevas.pack()

#Création vaisseau
PosX=450
PosY=750
Vaisseau=Canevas.create_image(PosX,PosY,image=Dab)
Canevas.focus_set()
Canevas.bind('d',Clavier)
Canevas.bind('q',Clavier)
Canevas.bind('l',Clavier)
Canevas.pack()

#Création aliens
al=PhotoImage(file='enemy.gif')
def CreationAliens(X,Y):
    Alien=Canevas.create_image(X,Y,anchor=NW,image=al)
    return Alien

TirAlien=[]
Aliens=[[],[],[]]
X=200
Y=0
for i in range (0,3):
    for j in range (2,8):
        Aliens[i].append(CreationAliens(j*100,i*100))
#direction initiale
dX=3
dY=0
for i in range (0,3):
    for j in range (0,6):
        Canevas.move(Aliens[i][j],dX,dY)

YLaser=750

deplacementAl()
CreationTirAlien()
MouvTirAlien()


# #Affichage vies
# y=StringVar()
# y.set("Vies restantes: "+str(Vies))
# LabelVies=Label(fen,textvariable=y,fg='black',bg='white')


fen.mainloop()


#Canevas.coords(Vaisseau,X-rayon,Y-rayon,X+rayon,Y+rayon)
#fen.after(20,deplacementAl)

