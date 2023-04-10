import pyxel
import salles
import rush
import pygame
from machine_sous import Machine_a_Sous
from des import Des
from menu import Menu

pygame.init()
pygame.mixer.music.load("assets/Musiques/Nouveau_projet.mp3")
#pygame.mixer.music.play(-1)
class casino:
    def __init__(self):
        pyxel.init(1350, 680, title= "ChasinOwO")
        pyxel.mouse(True)
        self.salle = salles.Debut()
        self.perso = rush.Rush(650,425)
        self.jeu = Menu()
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.jeu == None:
            self.perso.mouv(self.salle.mur)
            if len(self.salle.porte_bas)==3:
                if self.perso.x >= self.salle.porte_bas[0] and self.perso.x <= self.salle.porte_bas[1] and self.perso.y == self.salle.porte_bas[2] and pyxel.btnp(pyxel.KEY_E):
                    self.salle = self.salle.changer_bas()
                    self.perso.x = (self.salle.porte_haut[0] + self.salle.porte_haut[1])//2
                    self.perso.y = self.salle.mur[0][1]+5
            if len(self.salle.porte_haut)==3:
                if self.perso.x >= self.salle.porte_haut[0] and self.perso.x <= self.salle.porte_haut[1] and self.perso.y == self.salle.porte_haut[2] and pyxel.btnp(pyxel.KEY_E):
                    self.salle = self.salle.changer_haut()
                    self.perso.x = (self.salle.porte_bas[0] + self.salle.porte_bas[1])//2
                    self.perso.y = self.salle.mur[0][3]-5
            if len(self.salle.porte_droit)==3:
                if self.perso.y >= self.salle.porte_droit[1] and self.perso.y <= self.salle.porte_droit[2] and self.perso.x == self.salle.porte_droit[0] and pyxel.btnp(pyxel.KEY_E):
                    self.salle = self.salle.changer_droit()
                    self.perso.x = self.salle.porte_gauche[0]+5
                    self.perso.y = (self.salle.porte_gauche[1] + self.salle.porte_gauche[2])//2
            if len(self.salle.porte_gauche)==3:
                if self.perso.y >= self.salle.porte_gauche[1] and self.perso.y <= self.salle.porte_gauche[2] and self.perso.x == self.salle.porte_gauche[0] and pyxel.btnp(pyxel.KEY_E):
                    self.salle = self.salle.changer_gauche()
                    self.perso.x = self.salle.porte_droit[0] - 5
                    self.perso.y = (self.salle.porte_droit[1] + self.salle.porte_droit[2]) // 2
            if pyxel.btnp(pyxel.KEY_E):
                if len(self.salle.jeu)==2:
                    if self.perso.x >= self.salle.jeu[0] and self.perso.x <= self.salle.jeu[0]+75 and self.perso.y >= self.salle.jeu[1] and self.perso.y <= self.salle.jeu[1]+75:
                        self.jeu = self.salle.jouer()
            if pyxel.btnp(pyxel.KEY_K):
                print(self.perso.x,self.perso.y)
        else:
            self.jeu.update()
            if self.jeu.jouer == False:
                self.jeu = None

    def draw(self):
        if self.jeu == None:
            self.salle.dess()
            self.perso.dess()
        else:
            self.jeu.draw()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    casino()