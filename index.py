"""
Code realisé par Perrichet Théotime et Tuzio Lorenzo
le 16/12/2021

"""

from tkinter import *
import random as rd

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

class TirAl:
    def __init__(self):
        self.tiral=PhotoImage(file='laser.gif')


class Alien:
    def __init__(self,Canevas):
        self.alien=PhotoImage(file='enemy.gif')
        self.Canevas = Canevas
    def CreationAliens(self,x,y):
        self.image=self.Canevas.create_image(x,y,anchor=NW,image=self.alien)
        return self.image
        

class SpaceInvaders:
    def __init__(self):
        self.fen=Tk()
        self.fen.title('Space invaders')
        self.Largeur = 1700
        self.Hauteur = 1000
        self.nbal_large = 8
        self.nbal_hauteur = 2
        self.scorenb = 0
        self.mort = 0
        self.vies =3
        self.aliens = [[],[],[]]
        self.life=[PhotoImage(file='life-1.gif'),PhotoImage(file='life-2.gif'),PhotoImage(file='life-3.gif')]
        # self.defaite=PhotoImage(file='game_over.gif')
        # self.victoire=PhotoImage(file='Win.gif')
        self.Canevas = Canvas(self.fen,width = self.Largeur, height = self.Hauteur)
        self.photo = PhotoImage(file="space_invaders_wallpaper.gif")
        self.item = self.Canevas.create_image(0,0,anchor=NW, image=self.photo)
        self.laser=PhotoImage(file='laser.gif')
        self.victoire=PhotoImage(file='victoire.gif')
        self.defaite=PhotoImage(file='defaite.gif')
        self.Canevas.focus_set()
        self.Canevas.bind('d', self.deplacer)  # déplacement à droite
        self.Canevas.bind('q', self.deplacer)  # déplacement à gauche
        self.Canevas.bind('l', self.tirer)  
        self.vaisseau = Vaisseau(self.Canevas)
        self.enemi= Alien(self.Canevas)

        self.x = 200
        self.y = 0
        self.dx = 3
        self.dy = 0
        for i in range (0,3):
            for j in range (2,8):
                self.aliens[i].append(self.enemi.CreationAliens(j*100,i*100))
        print(self.aliens)
        for i in range (0,3):
            for j in range (0,6):
                self.Canevas.move(self.aliens[i][j],self.dx,self.dy)
            
        self.deplacement_al(self.x,self.y,self.dx,self.dy)
            

        self.start = Button(self.fen, text='Nouvelle Partie')
        self.start.pack(anchor=N, padx=5, pady=5)
        self.quitter = Button(self.fen, text ='Quitter',command=self.fen.destroy)
        self.quitter.pack(anchor=NE, padx = 5, pady = 5)
        self.lol=StringVar()
        self.score = Label(self.fen, textvariable=self.lol , fg="black")
        self.score.pack(anchor=NW, padx = 5, pady = 5)
        self.Canevas.pack()
        self.tir = []
        self.fen.after(10, self.mouv_tir)
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
        #on dessine le vaisseau à sa nouvelle place
        self.Canevas.coords(self.vaisseau.image,self.vaisseau.PosX,self.vaisseau.PosY)
    
    def tirer(self,event):
        touche=event.keysym
        if touche=='l': 
            self.tir.append(Tir(self.vaisseau.PosX,self.vaisseau.PosY,self.Canevas))
            

    
    def deplacement_al(self,x,y,dx,dy):
        self.TailleAl=50
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
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

    def mouv_tir(self):
        tir_to_delete = []
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
        i=rd.randint(0,len(self.aliens)-1)
        j=rd.randint(0,len(self.aliens[i])-1)
        XAlien=self.Canevas.coords(self.aliens[i][j])[0]
        YAlien=self.Canevas.coords(self.aliens[i][j])[1]
        self.tiralien.append(self.Canevas.create_image(XAlien,YAlien,image=self.Arc)) #c'est quoi ARC?
        self.destruction_tir_alien()
        self.fen.after(1000,self.creation_tir_alien)
    
    def destruction_Laser(self):
    #on cherche les éléments qui ont la même position que le laser
    #self.collision=False
        self.x1Laser=self.Canevas.coords(self.Laser)[0]
        self.y1Laser=self.Canevas.coords(self.tir.Laser)[1]
        self.x2Laser=self.x1Laser+20
        self.y2Laser=self.y1Laser+20
        self.impact1=self.Canevas.find_overlapping(self.x1Laser,self.y1Laser,self.x2Laser,self.y2Laser)
    #suppression des éléments qui sont entrés en collision
        for i in self.impact1:
            for i3 in self.aliens:
                for j in i3:
                    if i==j:
                        self.Canevas.delete(j)
                        self.Canevas.delete(self.Laser)   
                        self.scorenb+=50
                        self.morts+=1
                        if self.morts==18:
                            self.Canevas.create_image(0,0,anchor=NW,image=self.victoire)
                        return 
    
    def destruction_tir_alien(self):
        self.Collision=False
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
                        self.vies-=1
                        Collision=True
                    if Collision:
                        self.Canevas.delete(j)
                        self.TirAlien.pop(self.TirAlien.index(j))
                        if self.vies==0:
                            self.Canevas.delete(k)
                            self.Canevas.create_image(0,0,anchor=NW,image=self.defaite)
        self.fen.after(10,self.destruction_tir_alien)

jeu = SpaceInvaders()