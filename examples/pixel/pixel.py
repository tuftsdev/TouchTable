import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)
sys.path.insert(0,parentdir) 

import pytouch
import random

class Bullet():
    def __init__(self, x, y):
        self.obj = pytouch.Image("bullet.png", x, y, z_index = 1)
        self.obj.update = self.update
        self.active = True

    def update(self, obj):
        obj.move(obj.x, obj.y - 5)

class Ship():

    def __init__(self):
        self.obj = pytouch.Image("ship.png", 375, 500, z_index = 1)
        self.obj.dragHandler = self.shipDragHandler
        self.obj.update = self.update

        self.hp = 100
        self.hit = False
        self.hpbar = pytouch.Rect(780, 0, 20, 600, color='red', z_index = 1)

        self.counter = 0
        self.bullets = []

    def shipDragHandler(self, obj, touch, extra=None):
        # Can't use self because it still thinks it is the ship that
        # you are referring to
        if touch.xpos + obj.width/2 > 780:
            x = 730
        elif touch.xpos < 25:
            x = 0
        else:
            x = touch.xpos - obj.width/2

        if touch.ypos + obj.height/2 > 600:
            y = 550
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
            self.hpbar.move(self.hpbar.x, self.hpbar.y + 60)

    def shoot(self):
        self.bullets.append(Bullet(self.obj.x + 20, self.obj.y))

class Enemy():
    def __init__(self, x):
        self.obj = pytouch.Image("enemy.png", x, -50, z_index = 1)
        self.obj.update = self.update

    def update(self, obj):
        obj.move(obj.x, obj.y + 2)

def bgupdate(obj):
    if obj.y == 590:
        obj.y = -590
    else:
        obj.move(0, obj.y + 1)

if __name__ == "__main__":
    random.seed()
    pytouch = pytouch.init()

    background1 = pytouch.Image("background.png", 0, 0, z_index = 0)
    background2 = pytouch.Image("background.png", 0, -pytouch.screen_h, z_index = 0)
    background1.update = bgupdate
    background2.update = bgupdate

    gameover = pytouch.Text(0, 0, "GAME OVER", 60, z_index = 3)
    gameover.setVisible(False)
    gameover.move(400 - gameover.rect.width/2, 300 - gameover.rect.height/2)

    title = pytouch.Text(0,0, "PIXEL SHOOTER", 60, z_index = 3)
    title.setVisible(False)
    title.move(400 - title.rect.width/2, 300 - title.rect.height/2)

    ship = None
    enemies = []

    score = 0
    scoretext = pytouch.Text(0, 0, "Score: " + str(score), 30, z_index = 1)

    # Title Screen
    background1.z_index = 2
    background2.z_index = 2
    title.setVisible(True)
    while True:
        t = pytouch.touchTracker.update()
        if t != None and t.status == "clicked":
            background1.z_index = 0
            background2.z_index = 0
            title.setVisible(False)
            ship = Ship()
            break
        else:
            pytouch.update()
    while True:
        pytouch.update()

        # Attempt to spawn an enemy
        if random.randint(0,100) > 95:
            spawn = True
            newEnemy = Enemy(random.randint(0,730))
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
            if enemy.obj.y > 650:
                enemy.obj.remove()
                enemies.pop(i)
                i -= 1
            i += 1

        if ship.hp <= 0:
            gameover.setVisible(True)
            background1.z_index = 2
            background2.z_index = 2
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
                t = pytouch.touchTracker.update()
                if t != None and t.status == "clicked":
                    score = 0
                    scoretext.changeText("Score: " + str(score))
                    scoretext.z_index = 0
                    ship = Ship()
                    background1.z_index = 0
                    background2.z_index = 0
                    gameover.setVisible(False)
                    break
                else:
                    pytouch.update()
