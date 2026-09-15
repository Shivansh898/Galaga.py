import pgzrun
import random
WIDTH = 800
HEIGHT = 525
Galaga = Actor("galaga")
Bug = Actor("bug")
BulletList = []
Galaga.x = 400
Galaga.y = 475

def draw():
    screen.fill("blue")
    Galaga.draw()
    for b in BulletList:
        b.draw()
def update():
    if keyboard.left:
        Galaga.x -= 5
        if Galaga.x < 50:
            Galaga.x = 50
    if keyboard.right:
        Galaga.x += 5
        if Galaga.x > 750:
            Galaga.x = 750
    for i in BulletList:
        i.y -= 5

def on_key_down(key):
    if key == keys.SPACE:
        Bullet = Actor("bullet")
        BulletList.append(Bullet)
        Bullet.x = Galaga.x
        Bullet.y = Galaga.y -35

pgzrun.go()