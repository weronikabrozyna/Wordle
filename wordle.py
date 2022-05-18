import pygame
import time
import pygame.locals
import random

pygame.init()

okno = pygame.display.set_mode((800,650),0,32)
tlo = (0,0,0)
pygame.display.set_caption('WORDLE')

kafelek_tlo = pygame.Surface([50,50])
litera = pygame.font.SysFont('arial',20,True,False)
kafelek_tlo.fill((100,100,100))
alf = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
kafelki = []

def rysuj_haslo(ile,proby):
    for i in range(proby):
        for j in range(ile):
            pygame.draw.rect(okno,(255,255,255),pygame.Rect((280+j*50,10+i*50),(50,50)),1)
            pygame.display.update()

def rysuj_klawiature():
    for i in range(10):
        kafelek_tlo = pygame.Surface([50, 50])
        kafelek_tlo.fill((100, 100, 100))
        kafelek = litera.render(alf[i], True, (255, 255, 255), None)
        kafelki.append(kafelek_tlo)
        kafelki[i].blit(kafelek,(15,10))
        okno.blit(kafelki[i], (140+5*i + (i * 50),465))
        del kafelek_tlo
    for i in range(9):
        kafelek_tlo = pygame.Surface([50, 50])
        kafelek_tlo.fill((100, 100, 100))
        kafelek = litera.render(alf[10+i], True, (255, 255, 255), None)
        kafelki.append(kafelek_tlo)
        kafelki[10+i].blit(kafelek, (15, 10))
        okno.blit(kafelki[10+i], (170 + 5 * i + (i * 50), 520))
        del kafelek_tlo
    for i in range(7):
        kafelek_tlo = pygame.Surface([50, 50])
        kafelek_tlo.fill((100, 100, 100))
        kafelek = litera.render(alf[19+i], True, (255, 255, 255), None)
        kafelki.append(kafelek_tlo)
        kafelki[19+i].blit(kafelek, (15, 10))
        okno.blit(kafelki[19+i], (200 + 5 * i + (i * 50), 575))
        del kafelek_tlo

okno.fill(tlo)
pygame.display.update()
rysuj_haslo(5,9)
rysuj_klawiature()
pygame.display.update()
#time.sleep(5)

