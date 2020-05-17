class Player():
    def __init__(self,secreen_size):
        self.coordinate = (int(secreen_size[0]/2),int(secreen_size[1]/2))
        self.velocity = (0,0)
        self.lim_velocity = 10
        self.trail = []
        self.trail_limit = 10
        self.radius = self.trail_limit
        self.score = 0
    def move(self):
        self.coordinate = ((self.velocity[0] + self.coordinate[0]) % 800,(self.velocity[1] + self.coordinate[1]) % 600)
        self.trail.append(self.coordinate)
        if len(self.trail) > self.trail_limit:
            self.trail.pop(0)
    def acelerate(self, force):
        if abs(self.velocity[0] + force[0]) > self.lim_velocity:
            force = (0,force[1])
        if abs(self.velocity[1] + force[1]) > self.lim_velocity:
            force = (force[0],0)
        self.velocity = (self.velocity[0] + force[0],self.velocity[1] + force[1])
    def slow_down(self,factor):
        if self.velocity[0] > 0: self.acelerate((-factor,0))
        elif self.velocity[0] < 0: self.acelerate((factor,0))
        if self.velocity[1] > 0: self.acelerate((0,-factor))
        elif self.velocity[1] < 0: self.acelerate((0,factor))
    def decrease(self):
            self.trail_limit -= 5
            self.radius -= 5 
            self.trail = self.trail[len(self.trail)-5:]
    def caught(self):
        if self.trail_limit >= 10: self.decrease()
        else : self.die()
    def explode(self):
        if self.trail_limit >= 10: 
            self.decrease()
            return self.coordinate
    def die(self):
        print('DEATH REPORT')

            

