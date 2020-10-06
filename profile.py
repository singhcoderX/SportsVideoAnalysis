from shapely.geometry import Point, Polygon
class Color:
    def __init__(self, red, green,blue):
        self.R = red
        self.G = green
        self.B = blue

class Person:
    distance_covered = 0
    def __init__(self,x,y,color,team):
        self.color = color
        self.x = float(x)
        self.y = float(y)
        self.team = team
    def add_distance(self,x,y):
        # if self.color.R == '0.667' and self.color.G == '0.0' and self.color.B == '1.0':
        #     x = float(x)
        #     y = float(y)
        #     dist = ((self.x - x) ** 2 + (self.y - y) ** 2) ** (1 / 2)
        #     self.distance_covered += dist
        #     print("Initial:", self.x, self.y,"Current:", x, y,"Initial Distance",self.distance_covered,"DistanceAdded:",dist)
        #     self.x = x
        #     self.y = y
        #     return
        x = float(x)
        y = float(y)
        self.distance_covered += ((self.x-x)**2 + (self.y-y)**2)**(1/2)
        self.x = x
        self.y = y
    def print(self):
        print(self.color.R,self.color.G,self.color.B,"Team:",self.team,"Total Distance Travelled:",self.distance_covered)

def getColorObj(r,g,b,colors):
    for x in colors:
        if x.R == r and x.G == g and x.B == b:
            return x

def dist(a,b,c,d):
    a = float(a)
    b = float(b)
    c = float(c)
    d = float(d)
    return (((a-c)**2)+(b-d)**2)**(1/2)
def getPerson(color,persons,a,b):
    for x in persons:
        if x.color == color and dist(a,b,x.x,x.y) < 10:
            return x
    return ""
file = open('myfile2.txt','r')
frames = []
frame = []
colors = []
colors_obj = []
persons = []
coords = [(1735,45), (0,45),(0,939),(1735,939)]
poly = Polygon(coords)
for each in file:
    if each == '\n':
        frames.append(frame)
        frame = []
    else:
        x, y, r, g, b, team = each[:-1].split(',')
        point = Point(float(x),float(y))
        if point.within(poly) == False:
            continue
        if (r, g, b) not in colors:
            colors.append((r, g, b))
            col = Color(r, g, b)
            colors_obj.append(col)
            person = Person(x, y, col,team)
        else:
            col = getColorObj(r, g, b, colors_obj)
            person = getPerson(col,persons,x,y)

            if person == '':
                continue
            persons.remove(person)
            person.add_distance(x,y)
        persons.append(person)
        frame.append(each)
if each != '\n':
    frames.append(frame)

print(len(persons))
for x in persons:
    x.print()