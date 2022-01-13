"""
Code realisé par Perrichet Théotime et Tuzio Lorenzo
le 16/12/2021

"""

from tkinter import *

# def creation_tir():
#     global PosX,PosY,Laser,VerifLaser
#     XLaser=PosX
#     YLaser1=PosY
#     Laser=Canevas.create_image(XLaser,YLaser1,image=Arc)

    
# def mouv_tir():
#     global touche,YLaser,Laser,VerifLaser
#     if verif_laser:
#         if Canevas.coords(Laser)[1]<=100:
#             Canevas.bind('s',Clavier)
#             Canevas.delete(Laser)
#             VerifLaser=True
#         else :
#             Canevas.move(Laser,0,-10)
#             fen.after(10,mouv_tir)

#Création aliens
# al=PhotoImage(file='enemy.gif')
# def CreationAliens(X,Y):
#     Alien=Canevas.create_image(X,Y,anchor=NW,image=al)
#     return Alien
# Aliens=""
# TirAlien=[]

class Vaisseau:
    def __init__(self, Canevas):
        self.PosX=450
        self.PosY=750
        self.Laser=True
        self.joueur=PhotoImage(file='player.gif')
        self.Canevas = Canevas
        self.image = self.Canevas.create_image(self.PosX,self.PosY,image=self.joueur)

    # def VerificationLaser(self):
    #     if self.VerifLaser:
    #         SpaceInvaders.fen.after(50,self.VerificationLaser)
        
class Tir :
    def __init__(self,PosX,PosY,Canevas):
        self.XLaser = PosX
        self.YLaser = PosY
        self.tir=PhotoImage(file='laser.gif')
        self.Laser=self.Canevas.create_image(self.XLaser,self.YLaser,image=self.tir)
        self.Canevas = Canevas
        self.Canevas.pack()
        self.fen.mainloop()



class Alien:
    def __init__(self, Canevas):
        self.X=200
        self.Y=0
        self.alien=PhotoImage(file='enemy.gif')
        self.Canevas = Canevas
        self.image = self.Canevas.create_image(self.X,self.Y,image=self.alien)
    


verif_laser=True
YLaser=750

class SpaceInvaders:
    def __init__(self):
        self.fen=Tk()
        self.fen.title('Space invaders')
        self.Largeur = 1700
        self.Hauteur = 800
        self.nbal = 18
        self.aliens = []
        self.Canevas = Canvas(self.fen,width = self.Largeur, height = self.Hauteur)
        self.photo = PhotoImage(file="space_invaders_wallpaper.gif")
        self.item = self.Canevas.create_image(0,0,anchor=NW, image=self.photo)
        self.laser=PhotoImage(file='laser.gif')
        self.Canevas.focus_set()
        self.Canevas.bind('d', self.deplacer)  # déplacement à droite
        self.Canevas.bind('q', self.deplacer)  # déplacement à gauche
        self.vaisseau = Vaisseau(self.Canevas)
        for i in range (self.nbal):
            self.aliens.append(Alien(self.Canevas))
        self.Canevas.pack()
        self.fen.mainloop()

    def deplacer(self, event):
        touche=event.keysym
        #déplacement vers la droite
        if touche == 'd' :
            if self.vaisseau.PosX < 1650:
                self.vaisseau.PosX +=10
        #déplacement vers la gauche
        if touche =='q' :
            if self.vaisseau.PosX>50:
                self.vaisseau.PosX-=10
        if touche=='l':
            self.tir = Tir(self.Canevas)
            self.MouvTir(self.tir)
            #on dessine le vaisseau à sa nouvelle place
        self.Canevas.coords(self.vaisseau.image,self.vaisseau.PosX,self.vaisseau.PosY)
    
    def mouv_tir(self):
        if self.VerifLaser:
            if self.Canevas.coords(self.Laser)[1]<=0:
                self.Canevas.delete(self.Laser)
                self.VerifLaser=True
            else :
                self.Canevas.move(self.Laser,0,-10)
                SpaceInvaders.fen.after(10,self.MouvTir)

jeu = SpaceInvaders()