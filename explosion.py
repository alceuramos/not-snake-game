class Explosion():
    def __init__(self, coordinate, radius):
        self.coordinate = coordinate
        self.radius = radius
    def expand(self):
        self.radius += 1