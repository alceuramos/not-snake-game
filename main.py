from player import Player
from food import Food
from enemy import Enemy
from explosion import Explosion
import pygame, sys, random
class Game():
    def __init__(self,size):
        self.size = size
        self.displaysurf = pygame.display.set_mode(size)
        self.food = Food(size)
        self.player = Player(size)
        self.enemies = []
        self.explosions = []
    def draw(self):
        self.displaysurf.fill((0,0,255))
        i = 0
        pygame.draw.circle(self.displaysurf,self.food.color,self.food.coordinate,self.food.radius)
        for explosion in self.explosions:
            pygame.draw.circle(self.displaysurf,(0,255,255),explosion.coordinate,explosion.radius, 1) 
            explosion.expand()
        for coordinate in self.player.trail:
            i += 1
            try:
                pygame.draw.circle(self.displaysurf,(0,0,int((255*i)/255)),coordinate,int(self.player.trail_limit*i/self.player.trail_limit))
            except: print((0,0,int((255*i)/255)))
            # c -= int(255/self.player.trail_limit)
        # pygame.draw.circle(self.displaysurf,(0,0,0),self.player.coordinate,10)
        for enemy in self.enemies:
            for coordinate in enemy.trail:
                pygame.draw.circle(self.displaysurf,(0,255,0),coordinate,enemy.radius)
        self.displaysurf.blit(self.make_text('score:'+str(self.player.score)),(1,1))
    def make_text(self,text):
        font_obj = pygame.font.Font('freesansbold.ttf',12)
        return font_obj.render(text,True,(0,255,0))
    def colide(self,obj1,obj2):
        return (abs(obj1.coordinate[0] - obj2.coordinate[0]) <= max(obj1.radius,obj2.radius) and 
        abs(obj1.coordinate[1] - obj2.coordinate[1]) <= max(obj1.radius,obj2.radius))
    def explosion(self, coordinate):
        if coordinate != None:
            self.explosions.append(Explosion(coordinate,self.player.radius))
def main():
    pygame.init()
    pygame.display.set_caption('hehe')
    game = Game((800,600))
    clock = pygame.time.Clock()
    pressed_up = False
    pressed_down = False
    pressed_left = False
    pressed_right = False
    acelerate_factor = 2
    slow_down_factor = 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == ord('w'):
                    pressed_up = True
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    pressed_down = True
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    pressed_left = True
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    pressed_right = True
                if event.key == ord('r'):
                    game.enemies.append(Enemy(game.size))
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == ord('w'):
                    pressed_up = False
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    pressed_down = False
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    pressed_left = False
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    pressed_right = False
                if event.key == ord(' '):
                    game.explosion(game.player.explode())
        if pressed_up:
            game.player.acelerate((0,-acelerate_factor))
        if pressed_down:
            game.player.acelerate((0,acelerate_factor))
        if pressed_left:
            game.player.acelerate((-acelerate_factor,0))
        if pressed_right:
            game.player.acelerate((acelerate_factor,0))
        game.player.slow_down(slow_down_factor)
        game.player.move()
        for enemy in game.enemies:
            enemy.seek(game.player.coordinate)
            for explosion in game.explosions:
                if game.colide(explosion,enemy):
                    game.explosions.remove(explosion)
                    game.enemies.remove(enemy)
            if game.colide(game.player,enemy):
                game.enemies.remove(enemy)
                game.player.caught()
                
        if game.colide(game.player,game.food):
            del(game.food)
            game.food = Food(game.size)
            game.player.trail_limit += 1
            game.player.radius +=1
            game.player.score += 1
        game.food.update()
        pygame.display.update()
        game.draw()
        clock.tick(30)
if __name__ == "__main__":
    main()
    # diferença pego/explode
    # explosao
