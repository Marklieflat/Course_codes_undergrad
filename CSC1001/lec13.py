class Rectangle:
    def __init__(self, width = 1, height = 2):
        self.width = width
        self.height = height
    def getArea(self):
        self.area = self.width * self.height
        return
    

rec = Rectangle(1,2)
rec.getArea()