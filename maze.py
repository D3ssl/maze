from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, img,player_x, player_y,player_speed):
        self.image = transform.scale(image.load(img),(65,65))
        self.speed = player_speed 
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= 10

        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= 10

        if keys_pressed[K_s] and self.rect.y < 430:
            self.rect.y += 10

        if keys_pressed[K_d] and self.rect.x < 630:
            self.rect.x += 10
class Enemy(GameSprite):
    def update(self):
        if self.rect.x >= 600:
            self.direction = 'left'
            
        if self.rect.x <= 470:
            self.direction = 'right'

        if self.direction == 'left':
            self.rect.x -= self.speed
            
        if self.direction == 'right':
            self.rect.x += self.speed
class Wall(sprite.Sprite):
    def __init__(self,c_1,c_2,c_3, wall_w,wall_h,wall_x,wall_y):
        super().__init__()
        self.color_1 = c_1
        self.color_2 = c_2
        self.color_3 = c_3
        self.width = wall_w
        self.height = wall_h
        self.image = Surface((self.width,self.height))
        self.image.fill((self.color_1,self.color_2,self.color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

window = display.set_mode((700,500))
display.set_caption('Лабиринт')
#задай фон сцены
bg = transform.scale(image.load('background.jpg'),(700,500))
final = False
game = True
clock = time.Clock()
FPS = 60
#музыка
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
kick = mixer.Sound('kick.ogg')
jp = mixer.Sound('money.ogg')
font.init()
font = font.SysFont('Arial',70)
win = font.render('YOU WIN!', True,(0,255,0))
lose = font.render('YOU LOSE!',True,(255,0,0))
#создание спрайтов
hero = Player('hero.png',50,330,4)
enemy = Enemy('cyborg.png', 600,250,3)
money = GameSprite('treasure.png',600,435,0)
w1 = Wall(153,255,153,10,250,110,75)

w2 = Wall(153,255,153,10,65,110,405)
w3 = Wall(153,255,153,350,10,110,460)
w4 = Wall(153,255,153,400,10,110,75)
w5 = Wall(153,255,153,10,275,210,185)
w6 = Wall(153,255,153,10,285,310,75)
w7 = Wall(153,255,153,10,280,450,185)
w8 = Wall(153,255,153,100,10,405,180)

finish = False
while game:
#обработай событие «клик по кнопке "Закрыть окно"»
    for e in event.get():
        if e.type == QUIT:
            game = False 
    if finish != True:
        window.blit(bg,(0,0))
        hero.reset()
        enemy.reset()
        money.reset()
        hero.update()
        enemy.update()
        w1.draw_wall()

        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()

        if sprite.collide_rect(hero,money):
            window.blit(win,(200,200))
            finish = True
            jp.play()

        if sprite.collide_rect(hero,enemy):
            window.blit(lose,(200,200))
            finish = True
            kick.play()

        if sprite.collide_rect(hero,w1):
            finish = True
            window.blit(lose,(200,200))
            kick.play()

        if sprite.collide_rect(hero,w2):
            window.blit(lose,(200,200))
            finish = True
            kick.play()
        
        if sprite.collide_rect(hero,w3):
            window.blit(lose,(200,200))
            finish = True
            kick.play()
        
        if sprite.collide_rect(hero,w4):
            window.blit(lose,(200,200))
            finish = True
            kick.play()

        if sprite.collide_rect(hero,w5):
            window.blit(lose,(200,200))
            finish = True
            kick.play()
        
        if sprite.collide_rect(hero,w6):
            window.blit(lose,(200,200))
            finish = True
            kick.play()
        
        if sprite.collide_rect(hero,w7):
            window.blit(lose,(200,200))
            finish = True
            kick.play()

        if sprite.collide_rect(hero,w8):
            window.blit(lose,(200,200))
            finish = True
            kick.play()

        if sprite.collide_rect(hero,w3):
            window.blit(lose,(200,200))
            finish = True
            kick.play()
    clock.tick(FPS)
    display.update()