from pygame import *
import random
from time import sleep

class Sprite:
    def __init__(self, xpos, ypos, filename):
        self.x = xpos
        self.y = ypos
        self.bitmap = image.load(filename).convert_alpha()
        self.bitmap.set_colorkey((0,0,0))
    def set_position(self, xpos, ypos):
        self.x = xpos
        self.y = ypos
    def render(self):
        screen.blit(self.bitmap, (self.x, self.y))
def Intersect(s1_x, s1_y, s2_x, s2_y):
    if (s1_x > s2_x - 32) and (s1_x < s2_x + 32) and (s1_y > s2_y - 32) and (s1_y < s2_y + 32):
        return 1
    else:
        return 0


init()
screen = display.set_mode((1000,1000))
key.set_repeat(1,1)
display.set_caption('Kill All Aliens')
backdrop = image.load('space.png')
basicEnemies = pygame.sprite.Group()

enemies = []
bullet = []
x = 0

for count in range(18):
    basicEnemys.add(enemies.append(Sprite(50 * x + 50, 50, 'BlueBlaster.png')))
    basicEnemys.add(enemies.append(Sprite(50 * x + 50, 100, 'BlueBlaster.png')))
    basicEnemys.add(enemies.append(Sprite(50 * x + 50, 150, 'BlueBlaster.png')))
    x += 1

hero = Sprite(500, 900, 'player.png')
ourmissile = Sprite(0,900, 'bullet.png')
enemymissle = Sprite(0, 480, 'EnemyBullet.png')
StageClear = Sprite(500,500, 'StageClear.png')


quit = 0


while quit == 0:
    screen.blit(backdrop, (0, 0))
    for count in range(len(enemies)):
        enemies[count].x += 5
        enemies[count].render()
    for count in range(len(enemies)):
        enemies[count].x -= 5
        enemies[count].render()
    if ourmissile.y < 1000 and ourmissile.y > 0:
        ourmissile.render()
        ourmissile.y += -20

    if enemymissle.y >= 1000 and len(enemies)> 0:
        enemymissle.x = enemies[random.randint(0, len(enemies) - 1)].x
        enemymissle.y = enemies[0].y

    if Intersect(hero.x, hero.y, enemymissle.x, enemymissle.y):
        quit = 1

    for count in range(0, len(enemies)):
        if Intersect(ourmissile.x, ourmissile.y, enemies[count].x, enemies[count].y):
            del enemies[count]
            ourmissile.x = 1000
            break
    if len(enemies) == 0:
        for i in range(200):
            hero.y += 5
        while quit == 0:
            StageClear.render()
            

    for ourevent in event.get():
        if ourevent.type == QUIT:
            quit = 1
        if ourevent.type == KEYDOWN:
            if ourevent.key ==K_RIGHT and hero.x < 1000:
                hero.x += 5
            if ourevent.key ==K_LEFT and hero.x > 0:
                hero.x -= 5
            if ourevent.key ==K_SPACE:
                ourmissile.x = hero.x
                ourmissile.y = hero.y

    enemymissle.render()
    enemymissle.y += 20

    hero.render()

    display.update()
    time.delay(5)
