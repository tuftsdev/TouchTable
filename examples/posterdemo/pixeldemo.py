"""
    Pixel Shooter Application for TouchTable poster demo
"""
import os, sys, inspect
CUR_DIR = os.path.dirname(os.path.abspath(
                                    inspect.getfile(inspect.currentframe())))
PAR_DIR = os.path.dirname(CUR_DIR)
PAR_DIR = os.path.dirname(PAR_DIR)
sys.path.insert(0, PAR_DIR)

#import pytouch
import random

pytouch = None

STAR_SPAWN_Y = -4
STAR_WIDTH = 4
STAR_HEIGHT = 4
STAR_SPEED = 1

class Star():
    def __init__(self, x, y=STAR_SPAWN_Y):
        self.obj = pytouch.Rect(x, y, STAR_WIDTH, STAR_HEIGHT, color='white', alpha=random.randint(50,255))
        self.obj.update = self.update
        self.active = True

    def update(self, obj):
        obj.move(obj.x, obj.y + STAR_SPEED)

STAR_POPULATE_CHANCE = 99
STAR_SPAWN_CHANCE = 75
STAR_POPULATE_SPACING = 8
class Starfield():
    def __init__(self):
        self.stars = []
        self.populate()

    def populate(self):
        i = 0
        while i < pytouch.screen_h:
            j = 0
            while j < pytouch.screen_w:
                if random.randint(0,100) > STAR_POPULATE_CHANCE:
                    newStar = Star(j, i)
                    self.stars.append(newStar)
                j += STAR_POPULATE_SPACING
            i += STAR_POPULATE_SPACING

    def update(self):
    # Attempt to spawn a star
        if random.randint(0,100) > STAR_SPAWN_CHANCE:
            spawn = True
            newStar = Star(random.randint(0, pytouch.screen_w-4))
            for star in self.stars: # TODO DON'T NEED THIS
                if star.obj.collide(newStar.obj):
                    spawn = False
                    break
            if spawn:
                self.stars.append(newStar)
            else:
                newStar.obj.remove()
        i = 0
        for star in self.stars:
            if star.obj.y > pytouch.screen_h + 4:
                star.obj.remove()
                self.stars.pop(i)
                i -= 1
            i += 1
            
    def clean(self):
        for star in self.stars:
            star.obj.remove()
        self.stars = []

BULLET_SPEED = 5

class Bullet():
    def __init__(self, x, y):
        self.obj = pytouch.Image("bullet.png", x, y, z_index=1)
        self.obj.update = self.update
        self.active = True

    def update(self, obj):
        obj.move(obj.x, obj.y - BULLET_SPEED)

HPBAR_WIDTH = 20
SHIP_FIRE_SPEED = 5
SHIP_GUN_OFFSET = 20

class Ship():
    def __init__(self):
        self.obj = pytouch.Image("ship.png", pytouch.screen_w/2 - 25, pytouch.screen_h - 100, z_index=1)
        self.obj.dragHandler = self.shipDragHandler
        self.obj.update = self.update
        self.hp = 100
        self.hit = False
        self.hpbar = pytouch.Rect(pytouch.screen_w-HPBAR_WIDTH, 0, HPBAR_WIDTH, pytouch.screen_h, color="red", alpha=None, z_index=1)
        self.counter = 0
        self.bullets = []

    def shipDragHandler(self, obj, touch, extra=None):
    # Determine x coordinate from touch
        if touch.xpos + obj.width/2 > pytouch.screen_w - HPBAR_WIDTH: # Right side of screen
            x = pytouch.screen_w - HPBAR_WIDTH - self.obj.width
        elif touch.xpos < self.obj.width/2: # Left side of screen
            x = 0
        else:
            x = touch.xpos - obj.width/2
    # Determine y coordinate from touch
        if touch.ypos + obj.height/2 > pytouch.screen_h: # Right side of screen
            y = pytouch.screen_h - self.obj.height
        elif touch.ypos < self.obj.height/2: # Left side of screen
            y = 0
        else:
            y = touch.ypos - obj.height/2
    # Move ship
        obj.move(x, y)

    def update(self, obj):
    # Determine if the ship is going to shoot during this frame
        if self.counter >=  SHIP_FIRE_SPEED:
            self.shoot()
            self.counter = 0
        else:
            self.counter += 1
    # Determine if the oldest fired bullet is off the screen
        if len(self.bullets) > 0:
            if self.bullets[0].obj.y < 0:
                self.bullets[0].active = False
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
            self.hpbar.move(self.hpbar.x, self.hpbar.y + pytouch.screen_h/10)

    def shoot(self):
        self.bullets.append(Bullet(self.obj.x + SHIP_GUN_OFFSET, self.obj.y))

    def clean(self):
        self.hpbar.remove()
        for bullet in self.bullets:
            bullet.obj.remove()
        self.bullets = []
        self.obj.remove()

ENEMY_SPAWN_CHANCE = 95
ENEMY_SPAWN_Y = -50
ENEMY_SPEED = 2
class Enemy():
    def __init__(self, x):
        self.obj = pytouch.Image("enemy.png", x, ENEMY_SPAWN_Y, z_index=1)
        self.obj.update = self.update

    def update(self, obj):
        obj.move(obj.x, obj.y + ENEMY_SPEED)

class PixelApp():
    def __init__(self):
        self.gameover = None
        self.title = None
        self.title2 = None
        self.ship = None
        self.enemies = None
        self.starfield = None

        self.score = 0
        self.scoretext = None

        self.quit = None
        self.running = False

    def quitHandler(self, obj, touch):
        self.running = False

    def initgame(self):
        self.title = pytouch.Text(0,0,"PIXEL SHOOTER", 60, z_index=3)
        self.title.setVisible(False)
        self.title.move(pytouch.screen_w/2 - self.title.rect.width/2, pytouch.screen_h/2 - self.title.rect.height/2)

        self.title2 = pytouch.Text(0,0,"Tap to Begin", 15, z_index=3)
        self.title2.setVisible(False)
        self.title2.move(pytouch.screen_w/2 - self.title2.rect.width/2, 50 + pytouch.screen_h/2 - self.title2.rect.height/2)

        self.gameover = pytouch.Text(0, 0, "GAME OVER", 60, z_index = 3)
        self.gameover.setVisible(False)
        self.gameover.move(pytouch.screen_w/2 - self.gameover.rect.width/2, pytouch.screen_h/2 - self.gameover.rect.height/2)

        self.score = 0
        self.scoretext = pytouch.Text(0, 0, "Score: " + str(self.score), 30, z_index=1)
        self.scoretext.setVisible(False)

        self.quit = pytouch.Text(0, 0, "QUIT", 30, z_index=3)
        self.quit.touchUpInsideHandler = self.quitHandler
        self.quit.move(pytouch.screen_w - HPBAR_WIDTH - self.quit.rect.width, 0)

        self.enemies = []
        self.starfield = Starfield()

    def spawnEnemy(self):
        if random.randint(0,100) > ENEMY_SPAWN_CHANCE:
            spawn = True
            newEnemy = Enemy(random.randint(0,pytouch.screen_w-HPBAR_WIDTH-50))
            for enemy in self.enemies:
                if enemy.obj.collide(newEnemy.obj):
                    spawn = False
                    break
            if spawn:
                self.enemies.append(newEnemy)
            else:
                newEnemy.obj.remove()
                newEnemy = None

    def run(self, p):
        random.seed()
        global pytouch
        pytouch = p
        self.running = True

        self.initgame()
        t = pytouch.touchTracker.update()
        while self.running:
            self.titlescreen()
            self.gamescreen()
            self.gameoverscreen()
        self.clean()

    def titlescreen(self):
        onTitleScreen = True
        self.title.setVisible(True)
        self.title2.setVisible(True)
        while onTitleScreen:
            t = pytouch.touchTracker.update()
            self.starfield.update()
            if not self.running:
                break
            if t != None and t.status == "clicked":
                onTitleScreen = False
            else:
                pytouch.update()
        self.title.setVisible(False)
        self.title2.setVisible(False)

    def gamescreen(self):
        onGameScreen = True
        self.ship = Ship()
        self.score = 0
        self.scoretext.changeText("Score: " + str(self.score))
        self.scoretext.setVisible(True)
        while onGameScreen:
            if not self.running:
                break
            pytouch.update()
            self.starfield.update()
            self.spawnEnemy()
            i = 0
            # Collision detection: Ship Bullet - Enemy
            for bullet in self.ship.bullets:
                j = 0
                for enemy in self.enemies:
                    if bullet.obj.collide(enemy.obj):
                        bullet.obj.remove()
                        self.ship.bullets.pop(i)
                        i -= 1
                        enemy.obj.remove()
                        self.enemies.pop(j)
                        j -= 1

                        self.score += 10
                        self.scoretext.changeText("Score: " + str(self.score))
                        break
                    j += 1
                i += 1
            # Collision detection: Ship - Enemy
            i = 0
            for enemy in self.enemies:
                if enemy.obj.collide(self.ship.obj):
                    self.ship.hit = True
                    enemy.obj.remove()
                    self.enemies.pop(i)
                    i -= 1
                if enemy.obj.y > pytouch.screen_h + 50:
                    enemy.obj.remove()
                    self.enemies.pop(i)
                    i -= 1
                i += 1
            # Check if ship is dead
            if self.ship.hp <= 0:
                onGameScreen = False
        self.ship.clean()
        self.ship = None
        for enemy in self.enemies:
            enemy.obj.remove()
            enemies = []

    def gameoverscreen(self):
        onGameOverScreen = True
        self.gameover.setVisible(True)
        while onGameOverScreen:
            if not self.running:
                break
            t = pytouch.touchTracker.update()
            self.starfield.update()
            if t != None and t.status == "clicked":
                onGameOverScreen = False
            else:
                pytouch.update()
        self.gameover.setVisible(False)
        self.scoretext.setVisible(False)

    def clean(self):
        self.gameover.remove()
        self.title.remove()
        self.title2.remove()
        if self.ship != None:
            self.ship.clean()
            self.ship = None
        for enemy in self.enemies:
            enemy.obj.remove()
        self.enemies = None
        self.starfield.clean()
        self.starfield = None

        self.score = 0
        self.scoretext.remove()
        self.scoretext = None

        self.quit.remove()
        self.quit = None

        self.running = False
