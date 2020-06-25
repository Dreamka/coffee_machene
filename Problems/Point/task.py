class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def dist(self, point):
        return (((self.x - point.x) ** 2) + ((self.y - point.y) ** 2)) ** .5
