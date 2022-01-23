"""
Code realisé par Perrichet Théotime et Tuzio Lorenzo
le 16/12/2021
"""

from tkinter import Tk,PhotoImage,N,NE,NW,Canvas,Label,Button,StringVar,Text
from random import randint
from typing import Text


class HP: #classe pour la vie du joueur

	def __init__(self):
		self.life = [1,2,3]

	def regeneration(self, valeur): 
		self.life.append(valeur)

	def hurt(self):
		if self.life:
			return self.life.pop()

	def dead(self):
		return self.life == []

class Vaisseau:
    def __init__(self, Canevas):
        self.PosX=450
        self.PosY=850
        self.joueur=PhotoImage(file='player.gif')
        self.Canevas = Canevas
        self.image = self.Canevas.create_image(self.PosX,self.PosY,image=self.joueur)

        
class Tir :
    def __init__(self,PosX,PosY,Canevas):
        self.xLaser = PosX
        self.yLaser = PosY
        self.tir=PhotoImage(file='laser.gif')
        self.Canevas = Canevas
        self.Laser=self.Canevas.create_image(self.xLaser,self.yLaser,image=self.tir)

class TirAl: #classe tir aliens
    def __init__(self):
        self.tiral=PhotoImage(file='laser.gif')


class Alien:
    def __init__(self,Canevas):
        self.alien=PhotoImage(file='enemy.gif')
        self.Canevas = Canevas
    def CreationAliens(self,x,y):
        self.image=self.Canevas.create_image(x,y,anchor=NW,image=self.alien)
        return self.image

class Ilots:
    def __init__(self,Canevas):
        self.bloc=PhotoImage(file='mur.gif')
        self.Canevas = Canevas
    def CreationIlots(self,X,Y):
        Ilot=self.Canevas.create_image(X,Y,anchor=NW,image=self.bloc)
        return Ilot
        

class SpaceInvaders: #classe principale
    def __init__(self):
        self.fen=Tk()
        self.fen.title('Space invaders')

        self.Largeur = 1700
        self.Hauteur = 1000
        self.nbal_large = 8
        self.nbal_hauteur = 2
        self.scorenb = 0
        self.morts = 0
        self.vies =HP()

        self.aliens = [[],[],[]] #implementation liste
        self.life=[PhotoImage(file='life-1.gif'),PhotoImage(file='life-2.gif'),PhotoImage(file='life-3.gif')]

        self.Canevas = Canvas(self.fen,width = self.Largeur, height = self.Hauteur)
        self.photo = PhotoImage(file="space_invaders_wallpaper.gif")
        self.item = self.Canevas.create_image(0,0,anchor=NW, image=self.photo)

        self.laser=PhotoImage(file='laser.gif')
        self.victoire=PhotoImage(file='win.gif')
        self.defaite=PhotoImage(file='gameover.gif')

        self.Canevas.focus_set()
        self.Canevas.bind('d', self.deplacer)  # déplacement à droite
        self.Canevas.bind('q', self.deplacer)  # déplacement à gauche
        self.Canevas.bind('l', self.tirer)  #tirer

        self.vaisseau = Vaisseau(self.Canevas)
        self.enemi= Alien(self.Canevas)
        self.tiral=TirAl()
        self.bloc=Ilots(self.Canevas)

        #création d'ilots
        self.ilots=[]
        self.xilot=45
        self.yilot=600
        for i in range (0,101):
            self.ilots.append(self.bloc.CreationIlots(self.xilot,self.yilot))
            if self.xilot==195 or self.xilot==510 or self.xilot==825 or self.xilot==1140 or self.xilot==1455:
                self.xilot+=135
            if self.xilot>=1685:
                self.xilot=45
                self.yilot+=30
            else :
                self.xilot+=30

        #création d'aliens
        self.x = 200
        self.y = 0
        self.dx = 3
        self.dy = 0
        for i in range (0,3):
            for j in range (2,8):
                self.aliens[i].append(self.enemi.CreationAliens(j*100,i*100))
        
        for i in range (0,3):
            for j in range (0,6):
                self.Canevas.move(self.aliens[i][j],self.dx,self.dy)
            
        # Création d'un bouton nouvelle partie
        self.start = Button(self.fen, text='Nouvelle Partie')
        self.start.pack(anchor=N, padx=5, pady=5)
        # Création d'un widget Button (bouton quitter)
        self.quitter = Button(self.fen, text ='Quitter',command=self.fen.destroy)
        self.quitter.pack(anchor=NE, padx = 5, pady = 5)

        # Création d'un score
        self.score1 = Label(self.fen, text='Score:', fg="black")
        self.score1.pack(anchor=NW, padx = 5, pady = 5)

        self.Canevas.pack()

        self.tir = []
        self.fen.after(10, self.mouv_tir)

        self.deplacement_al()
        self.creation_tir_alien()
        self.mouv_tir_alien()

        self.fen.mainloop()

    def deplacer(self, event): #déplacement du joueur
        touche=event.keysym
        #déplacement vers la droite
        if touche == 'd' :
            if self.vaisseau.PosX < 1650:
                self.vaisseau.PosX +=10
        #déplacement vers la gauche
        if touche =='q' :
            if self.vaisseau.PosX>50:
                self.vaisseau.PosX-=10
        #on dessine le vaisseau à sa nouvelle place
        self.Canevas.coords(self.vaisseau.image,self.vaisseau.PosX,self.vaisseau.PosY)
    
    def tirer(self,event): #tir du joueur
        touche=event.keysym
        if touche=='l': 
            self.tir.append(Tir(self.vaisseau.PosX,self.vaisseau.PosY,self.Canevas))
        self.destruction_Laser()
    

    
    def deplacement_al(self): #déplacement des aliens
        self.TailleAl=50
        self.xp=self.Canevas.coords(self.aliens[0][0])[0]
        self.xd=self.Canevas.coords(self.aliens[0][-1])[0]
        #rebond à gauche
        if self.xp+self.dx<0:
            self.x=0
            self.dx = -self.dx
            self.y += self.TailleAl
        #rebond à droite
        if self.xd + self.TailleAl + self.dx > self.Largeur:
            self.x = self.Largeur - self.TailleAl-500
            self.dx = -self.dx
            self.y += self.TailleAl
        #nouvelle direction
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        #affichage
        for i in range(len(self.aliens)):
            for j in range(len(self.aliens[i])):
                self.Canevas.coords(self.aliens[i][j],self.x+j*100,self.y+i*100)
        #déplacement
        self.fen.after(40,self.deplacement_al)

    def mouv_tir(self): #deplacement du tir du joueur
        tir_to_delete = [] #implementation file
        for tir in self.tir:
            if self.Canevas.coords(tir.Laser)[1]<=0:
                tir_to_delete.append(tir)
            else :
                self.Canevas.move(tir.Laser,0,-3)

        for tir in tir_to_delete:
            self.Canevas.delete(tir.Laser)
            self.tir.remove(tir)

        self.fen.after(10, self.mouv_tir)

    def creation_tir_alien(self):
        self.tiralien=[]
        i=randint(0,len(self.aliens)-1)
        j=randint(0,len(self.aliens[i])-1)
        XAlien=self.Canevas.coords(self.aliens[i][j])[0]
        YAlien=self.Canevas.coords(self.aliens[i][j])[1]
        self.tiralien.append(self.Canevas.create_image(XAlien,YAlien,image=self.laser)) 
        self.destruction_tir_alien()
        self.fen.after(1000,self.creation_tir_alien)


    def mouv_tir_alien(self):
        for k in range(len(self.tiralien)-1):
            if self.Canevas.coords(self.tiralien[k].Laser)[1]==900:
                self.Canevas.delete(self.tiralien[k].Laser)
                self.tiralien.pop(k)
            else : 
                self.Canevas.move(self.tiralien[k].Laser,0,10)
        self.fen.after(10,self.mouv_tir_alien)


    def destruction_Laser(self): #destruction des éléments touchés par le laser du joueur
    #on cherche les éléments qui ont la même position que le laser
        self.x1Laser=self.Canevas.coords(self.tir)[0]
        self.y1Laser=self.Canevas.coords(self.tir)[1]
        self.x2Laser=self.x1Laser+20
        self.y2Laser=self.y1Laser+20
        self.impact1=self.Canevas.find_overlapping(self.x1Laser,self.y1Laser,self.x2Laser,self.y2Laser)
    #suppression des éléments qui sont entrés en collision
        for i in self.impact1:
            for i1 in self.aliens:
                for j in i1:
                    if i==j:
                        self.Canevas.delete(j)
                        self.Canevas.delete(self.tir)   
                        self.scorenb+=50
                        self.morts+=1
                        if self.morts==18:
                            self.Canevas.create_image(0,0,anchor=NW,image=self.victoire)
                        return 
            for i2 in self.ilots:
                if i==i2:
                    self.Canevas.delete(i2)
    
    def destruction_tir_alien(self):
    #on cherche les éléments qui ont la même position que les tirs des aliens
        if len(self.tiralien)!=0:
            for j in self.tiralien:
                self.n=self.Canevas.coords(j)
                self.x1TirAlien=self.Canevas.coords(j)[0]
                self.y1TirAlien=self.Canevas.coords(j)[1]
                self.x2TirAlien=self.x1TirAlien+20
                self.y2TirAlien=self.x2TirAlien+20
                self.Impact2=self.Canevas.find_overlapping(self.x1TirAlien,self.y1TirAlien,self.x2TirAlien,self.y2TirAlien) #retourne la liste des éléments touchés
                #suppression des éléments qui sont entrés en collision
                for k in self.Impact2:
                    if k==Vaisseau:
                        self.vies.hurt()
                        self.Canevas.delete(j)
                        self.tiralien.pop(self.tiralien.index(j))
                        if self.vies.dead:
                            self.Canevas.delete(k)
                            self.Canevas.create_image(0,0,anchor=NW,image=self.defaite)
        self.fen.after(10,self.destruction_tir_alien)

jeu = SpaceInvaders()