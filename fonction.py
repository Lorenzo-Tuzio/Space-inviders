from tkinter import*

def deplacement():
    global x,y,dx,dy,rayon,Largeur,Hauteur

    #rebond a droite
    if x+rayon+dx > Largeur:
        x = 2*(Largeur-rayon)-x
        dx= -dx
    #rebond a gauche
    if x+rayon+dx > Largeur:
        x = 2*(Largeur-rayon)-x
        dx= -dx
    
    x=x+dx
def dep_vaisseau(event):
    global vaisseau
    touche= event.keysym

    if touche == 'q':
        vaisseau.move()
    if touche == 'd':
        vx1 += 5
        vx2 += 5
        vx3 += 5
