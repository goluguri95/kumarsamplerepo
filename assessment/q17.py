class circle:
    def __init__(self, radius):
        self.radius=float(radius)
    def getarea(self):
        return(3.14*(self.radius*self.radius))

r=raw_input()
j=circle(float(r))
p=j.getarea()
print(p)
