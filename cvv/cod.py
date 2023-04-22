import pygame 
import time 
import random

pygame.init() 
pygame.font.init()

pygame.mixer.music.load('potok.mp3')
pygame.mixer.music.play(-1)


 
class img: 
 
    def __init__(self, file_name, x, y, width, height): 
        self.image = pygame.image.load(file_name) 
        self.newimage = pygame.transform.scale(self.image, (width, height)) 
 
    def draw(self, x, y): 
        sc.blit(self.newimage, (x, y)) 
 
    def collidepoint(self, x, y): 
        return self.rect.collidepoint(x, y)
        
bg = img("bg.png", 0,0,800,600)
car = img("car.png", 0,0,400,150)
car2 = img("carpovorot.png", 0,0,400,150)
kamen = img("kamen.png", 300,350,200,150)
car3 = img("car2.png", 0,0,400,350)
car4 = img("carpovorot2.png", 0,0,400,350)

carga = random.randint(1,2)


carx = 800
cary = 400

car1x = -400
car1y = 400

bgx = 0
bgy = 0


sc = pygame.display.set_mode((800, 600)) 
clk = pygame.time.Clock()
clk.tick(60)
game = True 
while game:
    for i in pygame.event.get(): 
        if i.type == pygame.QUIT: 
            game = False

    bg.draw(bgx,bgy)
    bg.draw(bgx-800,bgy)
    bg.draw(bgx+800,bgy)

    if bgx <= -800:
        bgx = 0
    if bgx >= 800:
        bgx = 0

    
    if carga == 1:
        carx -=10
        print(carx)
        if carx <= -400:
            car = img("car.png", 0,0,400,150)
            cary = 400
            carx = 900
            carga = random.randint(1,2)


    if carga == 2:
        car1x +=10
        print(car1x)
        if car1x >= 800:
            car2 = img("carpovorot.png", 0,0,400,150)
            car1y = 400
            car1x = -500
            carga = random.randint(1,2)

    #-80
    if carx == 480:
        pygame.mixer.music.load('pp.mp3')
        pygame.mixer.music.play()
        car = car3
        cary -= 100
        
    if carx <= 480:
        if carx >= 420:
            bgy +=10
            bg.draw(bgx,bgy)
            bg.draw(bgx-800,bgy)
            bg.draw(bgx+800,bgy)
            kamen.draw(300,435)
            car.draw(carx,cary)
            pygame.display.update()
            bgy -=10
            kamen.draw(300,425)
            bg.draw(bgx,bgy)
            bg.draw(bgx-800,bgy)
            bg.draw(bgx+800,bgy)
        cary -= 10
        bgx += 10


    if car1x == -80:
        pygame.mixer.music.load('pp.mp3')
        pygame.mixer.music.play()
        car2 = car4
        car1y -= 100
        
    if car1x >= -80:
        if car1x <= -20:
            bgy +=10
            bg.draw(bgx,bgy)
            bg.draw(bgx-800,bgy)
            bg.draw(bgx+800,bgy)
            kamen.draw(300,435)
            car2.draw(car1x,car1y)
            pygame.display.update()
            bgy -=10
            kamen.draw(300,425)
            bg.draw(bgx,bgy)
            bg.draw(bgx-800,bgy)
            bg.draw(bgx+800,bgy)
        car1y -= 10
        bgx -= 10


    car.draw(carx,cary)
    car2.draw(car1x,car1y)

    kamen.draw(300,425)
    clk.tick(60)
    pygame.display.update()
    #480

pygame.QUIT