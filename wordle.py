import pygame
import time
import pygame.locals
import random

pygame.init()

#tworzenie okna gry o wymiarach 800x650, ustalenie koloru, nazwy okna
okno = pygame.display.set_mode((800,650),0,32)
tlo = (0,0,0)
pygame.display.set_caption('WORDLE')

#ustawienia kafelka klawiatury - rozmiar, kolor

kafelek_tlo = pygame.Surface([50,50])
kafelek_tlo.fill((100,100,100))

#ustawienia czcionki liter na kafelkach, lista alfabetu w kolejności qwerty, która pomoże stworzyć klawiaturę
litera = pygame.font.SysFont('arial',20,True,False)
alf = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']

#w liście kafelki będą zapisane kolejne kafelki klawiatury
kafelki = []


#funkcja, która rysuje miejsce na wpisywanie hasła, zależne od 2 danych dłguość hasła = ile; liczba prób = proby
def rysuj_haslo(ile,proby):
    for i in range(proby):
        for j in range(ile):
            pygame.draw.rect(okno,(255,255,255),pygame.Rect((280+j*50,10+i*50),(50,50)),1)
            pygame.display.update()

#funkcja rysuje klawiaturę 'QWERTY', za pomocą której gracz będzie wpisywać hasło
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
    #trzeba dodać kafelek usuwania ostatniej wpisanej literki
    #trzeba dodać kafelek potwierdzający wpisanie hasła i wywołania sprawdzenia czy jest ono poprawne
        
def losuj_haslo(ile):
    wyborhasla = int(input("Jaką długość słów wybierasz? "))
    if wyborhasla == 4:
        print(random.choice(open('4litery.txt', 'r').readlines()).strip())
    elif wyborhasla == 5:
        print(random.choice(open('5liter.txt', 'r').readlines()).strip())
    elif wyborhasla == 6:
        print(random.choice(open('6liter.txt', 'r').readlines()).strip())
    else:
        print("Niestety nie mamy do wyboru słów o wybranej przez ciebie długości :(")
    #jeśli robimy dodatek: w zależności od liczby liter (ile) będziemy wyierać hasło z różnych zbiórów słow (różnica polega na różnej długości)
    #funkcja powinna zwracać wybrane hasło, chyba najlepiej w stringu
    
def wpisz_haslo(ile,proby):
    #tutaj będzie trzeba użyć funkcji z pygame (get_event itp.)
    #zasada działania: po kliknięciu kafelka z odpowiednią literką, literka jest wpisywana w pierwszym wolnym miejscu na wpisanie hasła

okno.fill(tlo)
rysuj_haslo(5,9)
rysuj_klawiature()
pygame.display.update()
time.sleep(5) #tymczasowe, żeby zobaczyć jak wygląda plansza/okno gry
