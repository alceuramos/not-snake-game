import random
class Food():
    def __init__(self,screen_size):
        self.screen_size = screen_size
        self.color = (0,0,0)
        self.coordinate =  (random.randint(0,screen_size[0]),random.randint(0,screen_size[1]))
        self.coordinate_variation = 2
        self.radius_medium = 5
        self.radius = 5
        self.radius_variation = 2
    def update(self):
        self.radius = random.randint(self.radius_medium-self.radius_variation,self.radius_medium+self.radius_variation)
        c = random.randint(0,255)
        self.color = (c,c,c)
        self.coordinate = ((self.coordinate[0]+random.randint(-self.coordinate_variation,self.coordinate_variation))% self.screen_size[0],
        (self.coordinate[1]+random.randint(-self.coordinate_variation,self.coordinate_variation))%self.screen_size[1])