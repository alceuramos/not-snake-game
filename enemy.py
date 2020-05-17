import random
class Enemy():
    def __init__(self,screen_size):
        self.secreen_size = screen_size
        self.coordinate = (random.randint(0,screen_size[0]),random.randint(0,screen_size[1]))
        self.velocity = 3
        self.trail_size = 5
        self.trail = [self.coordinate]
        self.radius = 5
    def seek(self,player_coordinate):
        x = 0
        y = 0
        if (player_coordinate[0] - self.coordinate[0]) < 0:
            x = -self.velocity
        elif (player_coordinate[0] - self.coordinate[0]) > 0:
            x = self.velocity
        if (player_coordinate[1] - self.coordinate[1]) < 0:
            y = -self.velocity
        elif (player_coordinate[1] - self.coordinate[1]) > 0:
            y = self.velocity
        self.coordinate = ((self.coordinate[0]+x) % self.secreen_size[0],
                            (self.coordinate[1]+y) % self.secreen_size[1])
        self.trail.append(self.coordinate)
        if len(self.trail) > self.trail_size:
            self.trail.pop(0)
    