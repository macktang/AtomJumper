import random
from enemy import Enemy
import __main__ as main

class Spawner():


    def __init__(self,player,rows,enemyPerRow):
        self.enemies = [] #init empty array
        self.rows = rows
        self.enemyPerRow = enemyPerRow
        self.player = player
        self.spawn()


    def spawn(self):
        intervaly = self.player.height/self.rows

        for row in range(1, self.rows + 1):
            for x in range(0, self.enemyPerRow):

                newy = (intervaly*row) - (intervaly/2)
                newx = random.randint(10,self.player.width)
                self.enemies.append(Enemy(self.player.width,self.player.height,newx,newy))
        main.g.all_sprites.add(self.enemies)

    def purge(self):
        main.g.all_sprites.remove(self.enemies)
        self.enemies = [] # purges enemy sprites from primary array, and resets class' own array

    def reset(self):
        self.purge()
        self.spawn()


    import random




