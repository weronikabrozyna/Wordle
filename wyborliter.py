import pygame
import time
import sys
import random

pygame.init()

#okno w którym można wybrać liczbę liter
oknoMenu = pygame.display.set_mode((800,650),0,32)
tlo = (0,0,0)
pygame.display.set_caption('WORDLE')

oknoMenu.fill((186, 201, 217))

czarny=(0,0,0)

czcionka = pygame.font.SysFont("arial", 70)
tekst = czcionka.render("Jaką długość słowa wybierasz?", True, czarny)
pozycja = tekst.get_rect(center=(400, 125))
oknoMenu.blit(tekst, pozycja)

color = (255,255,255)

color_light = (170,170,170)

color_dark = (100,100,100)

width = oknoMenu.get_width()

height = oknoMenu.get_height()

smallfont = pygame.font.SysFont('arial',60)

przycisk4 = smallfont.render('4' , True , color)
przycisk5 = smallfont.render('5' , True , color)
przycisk6 = smallfont.render('6' , True, color)
while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            if 200 <= mouse[0] <= 250 and 350 <= mouse[1] <= 410:
                wyborhasla == "4"
            if 400 <= mouse[0] <= 450 and 350 <= mouse[1] <= 410:
                wyborhasla == "5"
            if 550 <= mouse[0] <= 600 and 350 <= mouse[1] <= 410:
                wyborhasla == "6"

    mouse = pygame.mouse.get_pos()

    if 200 <= mouse[0] <= 250 and 350 <= mouse[1] <= 410:
        pygame.draw.rect(oknoMenu,color_light,[200,350,60,60])

    else:
        pygame.draw.rect(oknoMenu,color_dark,[200,350,60,60])

    if 375 <= mouse[0] <= 425 and 350 <= mouse[1] <= 410:
        pygame.draw.rect(oknoMenu,color_light,[375,350,60,60])

    else:
        pygame.draw.rect(oknoMenu,color_dark,[375,350,60,60])

    if 550 <= mouse[0] <= 600 and 350 <= mouse[1] <= 410:
        pygame.draw.rect(oknoMenu,color_light,[550,350,60,60])

    else:
        pygame.draw.rect(oknoMenu,color_dark,[550,350,60,60])

    oknoMenu.blit(przycisk4 , (213,345))
    oknoMenu.blit(przycisk5 , (388,345))
    oknoMenu.blit(przycisk6 , (563,345))

    pygame.display.update()
    
    
  # funkcja - losowanie hasła
  def losuj_haslo(ile):
    if wyborhasla == "4":
        ile = random.choice(open('4litery.txt', 'r').readlines()).strip()
    elif wyborhasla == "5":
        ile =  random.choice(open('5liter.txt', 'r').readlines()).strip()
    elif wyborhasla == "6":
        ile = random.choice(open('6liter.txt', 'r').readlines()).strip()

