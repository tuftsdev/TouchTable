import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)
sys.path.insert(0,parentdir) 

import pytouch
import random

SCREEN_W = 0
SCREEN_H = 0
pyt = pytouch.init()

class Star():
    def __init__(self, x, y=-4):
        self.WIDTH = 4
        self.HEIGHT = 4
        self.obj = pyt.Rect(x, y, self.WIDTH, self.HEIGHT, color='white', alpha=random.randint(50, 255))
        self.obj.update = self.update
        self.active = True

    def update(self, obj):
        obj.move(obj.x, obj.y + 1)

class Bullet():
    def __init__(self, x, y):
        self.obj = pyt.Image(os.path.join(os.path.dirname(__file__),"bullet.png"), x, y, z_index = 1)
        self.obj.update = self.update
        self.active = True

    def update(self, obj):
        obj.move(obj.x, obj.y - 5)

class Ship():
    def __init__(self):
        self.obj = pyt.Image(os.path.join(os.path.dirname(__file__),"ship.png"), SCREEN_W/2-25, SCREEN_H - 100, z_index = 1)
        self.obj.dragHandler = self.shipDragHandler
        self.obj.update = self.update
        self.hp = 100
        self.hit = False
        self.hpbar = pyt.Rect(SCREEN_W-20, 0, 20, SCREEN_H, color='red', alpha=None, z_index = 1)
        self.counter = 0
        self.bullets = []

    def shipDragHandler(self, obj, touch, extra=None):
        # Can't use self because it still thinks it is the ship that
        # you are referring to
        if touch.xpos + obj.width/2 > SCREEN_W-20:
            x = SCREEN_W-20-self.obj.width
        elif touch.xpos < 25:
            x = 0
        else:
            x = touch.xpos - obj.width/2

        if touch.ypos + obj.height/2 > SCREEN_H:
            y = SCREEN_H-self.obj.height
        elif touch.ypos < 25:
            y = 0
        else:
            y = touch.ypos - obj.height/2

        obj.move(x, y)


    # Self refers to SHIP class, obj refers to PYOBJECT class
    def update(self, obj):
        if self.counter >= 5:
            self.shoot()
            self.counter = 0
        else:
            self.counter += 1
        if len(self.bullets) > 0:
            # Must refer to object x and y if using custom class
            if self.bullets[0].obj.y < 0:
                self.bullets[0].obj.remove()
                self.bullets.pop(0)
        i = 0
        for bullet in self.bullets:
            if not bullet.active:
                bullet.obj.setVisible(False)
                bullet.obj.remove()
                self.bullets.pop(i)
                i -= 1 # Prevent skipping of objects during check
            i += 1

        if self.hit:
            self.hit = False
            self.hp -= 10
            self.hpbar.move(self.hpbar.x, self.hpbar.y + SCREEN_H/10)

    def shoot(self):
        self.bullets.append(Bullet(self.obj.x + 20, self.obj.y))

class Enemy():
    def __init__(self, x):
        self.obj = pyt.Image(os.path.join(os.path.dirname(__file__),"enemy.png"), x, -50, z_index = 1)
        self.obj.update = self.update

    def update(self, obj):
        obj.move(obj.x, obj.y + 2)

def star_populate(stars):
    i = -16
    j = 0
    while i < SCREEN_H:
        j = 0
        while j < SCREEN_W:
            if random.randint(0, 100) > 99:
                newStar = Star(j, i)
                stars.append(newStar)
            j += 8
        i += 8
    return stars

def star_update(stars):
    # Attempt to spawn a star
    if random.randint(0,100) > 75:
        spawn = True
        newStar = Star(random.randint(0, SCREEN_W-4))
        for star in stars:
            if star.obj.collide(newStar.obj):
                spawn = False
                break
        if spawn:
            stars.append(newStar)
        else:
            newStar.obj.remove()

    # Remove old stars
    i = 0
    for star in stars:
        if star.obj.y > SCREEN_H + 4:
            star.obj.remove()
            stars.pop(i)
            i -= 1
        i += 1
    return stars

def run():
    global SCREEN_W, SCREEN_H
    random.seed()

    SCREEN_W = pyt.screen_w
    SCREEN_H = pyt.screen_h

    '''
    background1 = pyt.Image("background.png", 0, 0, z_index = 0)
    background1.resize(SCREEN_W, SCREEN_H)
    background2 = pyt.Image("background.png", 0, -SCREEN_H, z_index = 0)
    background2.resize(SCREEN_W, SCREEN_H)
    background1.update = bgupdate
    background2.update = bgupdate
    background1.setVisible(False)
    background2.setVisible(False)
    '''

    gameover = pyt.Text(0, 0, "GAME OVER", 60, z_index = 3)
    gameover.setVisible(False)
    gameover.move(SCREEN_W/2 - gameover.rect.width/2, SCREEN_H/2 - gameover.rect.height/2)

    title = pyt.Text(0,0, "PIXEL SHOOTER", 60, z_index = 3)
    title.setVisible(False)
    title.move(SCREEN_W/2 - title.rect.width/2, SCREEN_H/2 - title.rect.height/2)

    title2 = pyt.Text(0,0, "Tap to Begin", 15, z_index = 3)
    title2.setVisible(False)
    title2.move(SCREEN_W/2 - title2.rect.width/2, SCREEN_H/2 + 50 - title.rect.height/2)

    ship = None
    enemies = []
    stars = []
    stars = star_populate(stars)

    score = 0
    scoretext = pyt.Text(0, 0, "Score: " + str(score), 30, z_index = 1)

    # Title Screen
    #background1.z_index = 2
    #background2.z_index = 2
    title.setVisible(True)
    title2.setVisible(True)
    while True:
        t = pyt.touchTracker.update()
        stars = star_update(stars)
        if t != None and t.status == "clicked":
            #background1.z_index = 0
            #background2.z_index = 0
            title.setVisible(False)
            title2.setVisible(False)
            ship = Ship()
            break
        else:
            pyt.update()
    while True:
        pyt.update()
        stars = star_update(stars)
        # Attempt to spawn an enemy
        if random.randint(0,100) > 95:
            spawn = True
            newEnemy = Enemy(random.randint(0,SCREEN_W-20-50))
            for enemy in enemies:
                if enemy.obj.collide(newEnemy.obj):
                    spawn = False
                    break
            if spawn:
                enemies.append(newEnemy)
            else:
                newEnemy.obj.remove()

        # Collision detection: Ship Bullet - Enemy
        i = 0
        for bullet in ship.bullets:
            j = 0
            for enemy in enemies:
                if bullet.obj.collide(enemy.obj):
                    bullet.obj.remove()
                    ship.bullets.pop(i)
                    i -= 1
                    enemy.obj.remove()
                    enemies.pop(j)
                    j -= 1

                    score += 10
                    scoretext.changeText("Score: " + str(score))
                    break
                j += 1
            i += 1

        # Collision detection: Ship - Enemy
        i = 0
        for enemy in enemies:
            if enemy.obj.collide(ship.obj):
                ship.hit = True
                enemy.obj.remove()
                enemies.pop(i)
                i -= 1
            if enemy.obj.y > SCREEN_H + 50 :
                enemy.obj.remove()
                enemies.pop(i)
                i -= 1
            i += 1

        if ship.hp <= 0:
            gameover.setVisible(True)
            #background1.z_index = 2
            #background2.z_index = 2
            #background1.setVisible(True)
            #background2.setVisible(True)
            scoretext.z_index = 3
            # Reset game
            for enemy in enemies:
                enemy.obj.remove()
            enemies = []
            for bullet in ship.bullets:
                bullet.obj.remove()
            ship.bullets = []
            ship.obj.remove()
            ship = None

            while True:
                # Hack to get touches TODO
                t = pyt.touchTracker.update()
                stars = star_update(stars)
                if t != None and t.status == "clicked":
                    score = 0
                    scoretext.changeText("Score: " + str(score))
                    scoretext.z_index = 1
                    #background1.z_index = 0
                    #background2.z_index = 0
                    #background1.setVisible(False)
                    #background2.setVisible(False)
                    gameover.setVisible(False)
                    break
                else:
                    pyt.update()
            scoretext.setVisible(False)
            # Title Screen
            #background1.z_index = 2
            #background2.z_index = 2
            #background1.setVisible(True)
            #background2.setVisible(True)
            title.setVisible(True)
            title2.setVisible(True)
            while True:
                t = pyt.touchTracker.update()
                stars = star_update(stars)
                if t != None and t.status == "clicked":
                    #background1.z_index = 0
                    #background2.z_index = 0
                    #background1.setVisible(False)
                    #background2.setVisible(False)
                    title.setVisible(False)
                    title2.setVisible(False)
                    scoretext.setVisible(True)
                    ship = Ship()
                    break
                else:
                    pyt.update()

if __name__ == "__main__":
    run()
