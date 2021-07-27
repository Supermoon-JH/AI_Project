class Box:
    def __init__(self, width, depth, height):
        self.width = width
        self.depth = depth
        self.height = height
    def set_width(self, width):
        self.width = width
    def set_depth(self, depth):
        self.depth = depth
    def set_height(self, height):
        self.height = height
    def cal_volume(self):
        return self.width * self.depth * self.height

box = Box(50, 50, 50)

print("box의 부피: %d" % box.cal_volume())
