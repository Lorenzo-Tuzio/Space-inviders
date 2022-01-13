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
        self.PosY=850
        self.Laser=True
        self.joueur=PhotoImage(file='player.gif')
        self.Canevas = Canevas
        self.image = self.Canevas.create_image(self.PosX,self.PosY,image=self.joueur)
        
class Tir :
    def __init__(self,PosX,PosY,Canevas):
        self.XLaser = PosX
        self.YLaser = PosY
        self.tir=PhotoImage(file='laser.gif')
        self.Canevas = Canevas
        self.Laser=self.Canevas.create_image(self.XLaser,self.YLaser,image=self.tir)


class Alien:
    def __init__(self,x,y,Canevas):
        self.x=x
        self.y=y
        self.alien=PhotoImage(file='enemy.gif')
        self.Canevas = Canevas
        self.image = self.Canevas.create_image(self.x,self.y,image=self.alien)

class SpaceInvaders:
    def __init__(self):
        self.fen=Tk()
        self.fen.title('Space invaders')
        self.Largeur = 1700
        self.Hauteur = 1000
        self.nbal_large = 6
        self.nbal_hauteur = 3
        self.aliens = [[],[],[]]
        # self.life=[PhotoImage(file='life-1.gif'),PhotoImage(file='life-2.gif'),PhotoImage(file='life-3.gif')]
        # self.defaite=PhotoImage(file='game_over.gif')
        # self.victoire=PhotoImage(file='Win.gif')
        self.Canevas = Canvas(self.fen,width = self.Largeur, height = self.Hauteur)
        self.photo = PhotoImage(file="space_invaders_wallpaper.gif")
        self.item = self.Canevas.create_image(0,0,anchor=NW, image=self.photo)
        self.laser=PhotoImage(file='laser.gif')
        self.Canevas.focus_set()
        self.Canevas.bind('d', self.deplacer)  # déplacement à droite
        self.Canevas.bind('q', self.deplacer)  # déplacement à gauche
        self.Canevas.bind('l', self.deplacer)  
        self.vaisseau = Vaisseau(self.Canevas)
        for i in range (self.nbal_large):
            for j in range (self.nbal_hauteur):
                self.aliens[j].append(Alien(i*100+50,j*50+50,self.Canevas))
        self.start = Button(self.fen, text='Nouvelle Partie')
        self.start.pack(anchor=N, padx=5, pady=5)
        self.quitter = Button(self.fen, text ='Quitter',command=self.fen.destroy)
        self.quitter.pack(anchor=NE, padx = 5, pady = 5)
        self.lol=StringVar()
        self.score = Label(self.fen, textvariable=self.lol , fg="black")
        self.score.pack(anchor=NW, padx = 5, pady = 5)
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
            self.veriflaser = True
            self.tir = Tir(self.vaisseau.PosX,self.vaisseau.PosY,self.Canevas)
            self.MouvTir(self,self.veriflaser)
            #on dessine le vaisseau à sa nouvelle place
        self.Canevas.coords(self.vaisseau.image,self.vaisseau.PosX,self.vaisseau.PosY)
    
    def deplacement_al(self):
        self.TailleAl=50
        self.x = 200
        self.y = 0
        self.dx = 3
        self.dy = 0
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

    def mouv_tir(self,veriflaser):
        if veriflaser:
            if self.Canevas.coords(self.laser)[1]<=0:
                self.Canevas.delete(self.laser)
                self.VerifLaser=True
            else :
                self.Canevas.move(self.laser,0,-10)
                SpaceInvaders.fen.after(10,self.mouv_tir)

jeu = SpaceInvaders()