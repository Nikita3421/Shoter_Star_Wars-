#Спросить про кнопку F
#Cпросить про той как зделать текст на передний план
#Снять видео про проэкт(печалька)
from pygame import *
from random import randint 
#Игровая сцена:
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Шутер")
background = transform.scale(image.load("galaxy.jpg"), (win_width, win_height))

game = True
finish = False
clock = time.Clock()
FPS = 60
font.init()
font1=font.SysFont("Arial",80)
Win1 = font1.render('YOU WIN!', True,(255, 255, 255))
Lose = font1.render('YOU LOSE!', True,(180, 0, 0))
Restart = font1.render('TO RESTART ', True,(180, 220, 100))
Restart1 = font1.render('PRESS BUTTON ', True,(180, 200, 100))
Restart2 = font1.render('[R]', True,(180, 200, 50))

font2=font.SysFont("Arial",36)



#Музыка на фоне
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
mixer.music.set_volume(0.5)
#класс-родитель для спрайтов 
class GameSprite(sprite.Sprite):
    #конструктор класса
    def __init__(self, player_image, player_x, player_y, width,height,player_speed):
        super().__init__()
 
        # каждый спрайт должен хранить свойство image - изображение

        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.width=width
        self.height=height
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#класс-наследник для спрайта-игрока (управляется стрелками)
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed  
             

    def fier(self):
        bullet = Bullet("bullet.png",self.rect.centerx-10,self.rect.top,20,15,16)
        bullets.add(bullet)

class Enemy(GameSprite):
    def update(self):
        global Lost 
        self.rect.y+=self.speed
        if self.rect.y > 485:
            self.rect.x=randint(50,650)
            self.rect.y = 0 
            Lost+=1 
        if finish == True:
            self.kill()     

class Enemy1(GameSprite):
    def update(self):
        global Lost 
        self.rect.y+=self.speed
        if self.rect.y > 485:
            self.rect.x=randint(50,650)
            self.rect.y = 0  
        if finish == True:
            self.kill()               


class Bullet(GameSprite):
    def update(self):
        self.rect.y-=self.speed
        if self.rect.y < 0:
            self.kill()
        if finish == True:
            self.kill()



bullets = sprite.Group()    



ship = Player("ship.png",350,400,80,100,10)



monsters=sprite.Group()
monsters1=sprite.Group()
monsters2=sprite.Group()
monsters3=sprite.Group()
monsters4=sprite.Group()

Asteroids=sprite.Group()

#счётчик пропусков
Lost=0 
#счётчик попаданий
Score=0
#счётчик побед
Won = 0
#счётчик проигрышей
Loser = 0
for i in range (1):
    monster=Enemy("ufo.png",randint(50,650),0,80,50,randint(1,6))  
    monsters.add(monster)
    monster1=Enemy("ufo1.png",randint(50,650),0,80,50,randint(1,6))  
    monsters1.add(monster1)
    monster2=Enemy("ufo2.png",randint(50,650),0,80,50,randint(1,6))  
    monsters2.add(monster2)
    monster3=Enemy("ufo3.png",randint(50,650),0,80,50,randint(1,6))  
    monsters3.add(monster3)
    monster4=Enemy("ufo4.png",randint(50,650),0,80,50,randint(1,6))  
    monsters4.add(monster4)

for i in range (1):
    Asteroid =Enemy1("Asteroid.png",randint(50,650),0,80,70,3)  
    Asteroids.add(Asteroid)


F = mixer.Sound("fire.ogg")

Win31 = mixer.Sound("Win31.ogg")
Over1 = mixer.Sound("Over.ogg")  
Man1 = mixer.Sound("Man.ogg")

Over1.set_volume(0.2)
Man1.set_volume(0.6)
Win31.set_volume(0.5)
F.set_volume(0.3)


while game:
    for e in event.get():
        if e.type == QUIT: 
            game=False
        elif e.type == KEYDOWN:
            if e.key == K_q:
                if finish == False:    
                    finish = True
                    mixer.music.stop()
            
            if e.key == K_f:
                if finish == True:
                        finish = False
                        Win31.stop()
                        Man1.stop()
                        Over1.stop()
                        mixer.music.play()     
                        monsters.add(monster)
                        monsters1.add(monster1)
                        monsters2.add(monster2)
                        monsters3.add(monster3)
                        monsters4.add(monster4)
                        Asteroid.add(Asteroids)

            if e.key == K_SPACE and finish != True:
                ship.fier() 
                F.play()           
            if e.key == K_r:  
                    if finish == True:
                        monsters.update()
                        monsters1.update()
                        monsters2.update()
                        monsters3.update()
                        monsters4.update()
                        Asteroids.update()
                        finish = False
                        Win31.stop()
                        Man1.stop()
                        Over1.stop()
                        mixer.music.play()
                        Lost -= Lost
                        Score -= Score 
                        monster=Enemy("ufo.png",randint(50,650),0,80,50,randint(1,6))  
                        monsters.add(monster)
                        monster1=Enemy("ufo1.png",randint(50,650),0,80,50,randint(1,6))  
                        monsters1.add(monster1)
                        monster2=Enemy("ufo2.png",randint(50,650),0,80,50,randint(1,6))  
                        monsters2.add(monster2)
                        monster3=Enemy("ufo3.png",randint(50,650),0,80,50,randint(1,6))  
                        monsters3.add(monster3)
                        monster4=Enemy("ufo4.png",randint(50,650),0,80,50,randint(1,6))  
                        monsters4.add(monster4)    
                        monsters.add(monster)
                        monsters1.add(monster1)
                        monsters2.add(monster2)
                        monsters3.add(monster3)
                        monsters4.add(monster4)
                        Asteroid=Enemy1("Asteroid.png",randint(50,650),0,80,70,3)  
                        Asteroid.add(Asteroids)   
                                   

        
                   
            

    if finish != True:
        window.blit(background,(0,0))
        ship.reset()
        ship.update()
        text=font2.render("Счёт:" +str(Score),True,(250,25,200))
        window.blit(text,(20,20))
        text1=font2.render("Пропущено:" +str(Lost),True,(25,255,255))
        window.blit(text1,(20,50)) 
        text2=font2.render("Побед:" +str(Won),True,(0,255,155))
        window.blit(text2,(20,80))   
        text3=font2.render("Проигрышей:" +str(Loser),True,(250,25,200))
        window.blit(text3,(20,110))  
        text4=font2.render("Q for stop:" +str(),True,(25,255,255))
        window.blit(text4,(480,20))  
        text5=font2.render("F for return:" +str(),True,(25,255,255))
        window.blit(text5,(480,50))
        monsters.update() 
        monsters.draw(window)
        monsters1.update() 
        monsters1.draw(window)
        monsters2.update() 
        monsters2.draw(window)
        monsters3.update() 
        monsters3.draw(window)
        monsters4.update() 
        monsters4.draw(window)
        bullets.draw(window)
        bullets.update()
        Asteroids.update() 
        Asteroids.draw(window)
        
        collidess = sprite.groupcollide(monsters, Asteroids, True, False)
        collides1s = sprite.groupcollide(monsters1, Asteroids, True, False)
        collides2s = sprite.groupcollide(monsters2, Asteroids, True, False)
        collides3s = sprite.groupcollide(monsters3, Asteroids, True, False)
        collides4s = sprite.groupcollide(monsters4, Asteroids, True, False)  
        for m in collidess:
            monster=Enemy("ufo.png",randint(50,650),0,80,50,randint(2,5)) 
            monsters.add(monster)
        for m in collides1s:
            monster1=Enemy("ufo1.png",randint(50,650),0,80,50,randint(2,5)) 
            monsters1.add(monster1)
        for m in collides2s:
            monster2=Enemy("ufo2.png",randint(50,650),0,80,50,randint(2,5)) 
            monsters2.add(monster2)
        for m in collides3s:
            monster3=Enemy("ufo3.png",randint(50,650),0,80,50,randint(2,5)) 
            monsters3.add(monster3)
        for m in collides4s:
            monster4=Enemy("ufo4.png",randint(50,650),0,80,50,randint(2,5)) 
            monsters4.add(monster4)       

        sprites_collidess = sprite.spritecollide(ship,Asteroids,False)           
        if sprites_collidess:
            finish = True
            mixer.music.stop()
            F.stop()
            Over1.play()  
            Man1.play()
            window.blit(Lose, (180, 200))
            window.blit(Restart, (120, 260))
            window.blit(Restart1, (70, 320))
            window.blit(Restart2, (300, 380))
            monsters.update()
            monsters1.update()
            monsters2.update()
            monsters3.update()
            monsters4.update()
            Asteroids.update() 
            Loser+=1

        collides = sprite.groupcollide(monsters, bullets, True, True)
        collides1 = sprite.groupcollide(monsters1, bullets, True, True)
        collides2 = sprite.groupcollide(monsters2, bullets, True, True)
        collides3 = sprite.groupcollide(monsters3, bullets, True, True)
        collides4 = sprite.groupcollide(monsters4, bullets, True, True)         
        for m in collides:
            Score+=1
            monster=Enemy("ufo.png",randint(50,650),0,80,50,randint(2,5)) 
            monsters.add(monster)
        for m in collides1: 
            Score+=1   
            monster1=Enemy("ufo1.png",randint(50,650),0,80,50,randint(2,5))  
            monsters1.add(monster1)
        for m in collides2:
            Score+=1        
            monster2=Enemy("ufo2.png",randint(50,650),0,80,50,randint(2,5))  
            monsters2.add(monster2)
        for m in collides3: 
            Score+=1       
            monster3=Enemy("ufo3.png",randint(50,650),0,80,50,randint(2,5))  
            monsters3.add(monster3) 
        for m in collides4: 
            Score+=1       
            monster4=Enemy("ufo4.png",randint(50,650),0,80,50,randint(2,5))  
            monsters4.add(monster4) 
    
        sprites_collides = sprite.spritecollide(ship,monsters,False)
        sprites_collides1 = sprite.spritecollide(ship,monsters1,False)
        sprites_collides2 = sprite.spritecollide(ship,monsters2,False)
        sprites_collides3 = sprite.spritecollide(ship,monsters3,False)
        sprites_collides4 = sprite.spritecollide(ship,monsters4,False)
        if sprites_collides:
            finish = True
            mixer.music.stop()
            F.stop()
            Over1.play()  
            Man1.play()
            window.blit(Lose, (200, 200))
            window.blit(Restart, (120, 260))
            window.blit(Restart1, (70, 320))
            window.blit(Restart2, (300, 380))
            monsters.update()
            monsters1.update()
            monsters2.update()
            monsters3.update()
            monsters4.update()
            Asteroids.update()
            Loser+=1
        
        if sprites_collides1:
            finish = True
            mixer.music.stop()
            F.stop()
            Over1.play()  
            Man1.play()
            window.blit(Lose, (180, 200)) 
            window.blit(Restart, (120, 260))
            window.blit(Restart1, (70, 320))
            window.blit(Restart2, (300, 380))
            monsters.update()
            monsters1.update()
            monsters2.update()
            monsters3.update()
            monsters4.update()
            Asteroids.update() 
            Loser+=1

        if sprites_collides2:
            finish = True
            mixer.music.stop()
            F.stop()
            Over1.play()  
            Man1.play()
            window.blit(Lose, (180, 200)) 
            window.blit(Restart, (120, 260))
            window.blit(Restart1, (70, 320))
            window.blit(Restart2, (300, 380))
            monsters.update()
            monsters1.update()
            monsters2.update()
            monsters3.update()
            monsters4.update()
            Asteroids.update()
            Loser+=1       

        if sprites_collides3:
            finish = True
            mixer.music.stop()
            F.stop()
            Over1.play()  
            Man1.play()
            window.blit(Lose, (180, 200)) 
            window.blit(Restart, (120, 260))
            window.blit(Restart1, (70, 320))
            window.blit(Restart2, (300, 380))
            monsters.update()
            monsters1.update()
            monsters2.update()
            monsters3.update()
            monsters4.update()
            Asteroids.update()
            Loser+=1

        if sprites_collides4:
            finish = True
            mixer.music.stop()
            F.stop()
            Over1.play()  
            Man1.play()
            window.blit(Lose, (180, 200)) 
            window.blit(Restart, (120, 260))
            window.blit(Restart1, (70, 320))
            window.blit(Restart2, (300, 380))
            monsters.update()
            monsters1.update()
            monsters2.update()
            monsters3.update()
            monsters4.update()
            Asteroids.update()
            Loser+=1

        if Lost >= 16:   
            finish = True
            mixer.music.stop()
            F.stop()
            Over1.play()
            Man1.play()
            window.blit(Lose, (180, 200)) 
            window.blit(Restart, (120, 260))
            window.blit(Restart1, (70, 320))
            window.blit(Restart2, (300, 380))
            monsters.update()
            monsters1.update()
            monsters2.update()
            monsters3.update()
            monsters4.update()
            Asteroids.update()
            Loser+=1


        if Score >= 26:  
            finish = True
            mixer.music.stop()
            F.stop()
            Win31.play()
            window.blit(Win1, (180, 200))
            window.blit(Restart, (120, 260))
            window.blit(Restart1, (70, 320))
            window.blit(Restart2, (300, 380))
            monsters.update()
            monsters1.update()
            monsters2.update()
            monsters3.update()
            monsters4.update()
            Asteroids.update()  
            Won+=1 
    
              
      

    display.update()
    clock.tick(FPS)  