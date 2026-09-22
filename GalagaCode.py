import pgzrun
import random
WIDTH = 800
HEIGHT = 525
Galaga = Actor("galaga")
BulletList = []
BugList = []
Galaga.x = 400
Galaga.y = 475
direction = 1 

for j in range(3):
    for i in range(6):
        Bug = Actor("bug")
        Bug.x =  25 + (50*i)
        Bug.y = 25 + (45*j)
        BugList.append(Bug)

def draw():
    
    screen.fill("blue")
    Galaga.draw()
    for b in BulletList:
        b.draw()
    for bug in BugList:
        bug.draw()
def update():
    global direction, Bug    
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
        for Bug in BugList:
            if Bug.colliderect(i):
                BugList.remove(Bug)
                BulletList.remove(i)
    if Bug in BugList:
        for Bug in BugList:
            Bug.x += 3*direction
        if BugList[-1].x == 800:
            direction = -1
            for Bug in BugList:
                Bug.y += 20
                
        elif BugList[0].x <= 10:
            direction = 1
            for Bug in BugList:
                Bug.y +=20
    elif Bug not in BugList:
        screen.fill("black")

def on_key_down(key):
    if key == keys.SPACE:
        Bullet = Actor("bullet")
        BulletList.append(Bullet)
        Bullet.x = Galaga.x
        Bullet.y = Galaga.y -35

pgzrun.go()