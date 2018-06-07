# Object Oriented Concept.

class Robot:
    def __init__(self, givenname, givencolor, givenweight ):
        self.name = givenname
        self.color = givencolor
        self.weight = givenweight

    def intro_self(self):
        print("My Name is : ", self.name)
        print("My color is : ", self.color)
        print("My weight is : ", self.weight)

# r1 = Robot()
# r1.name = "First Robot"
# r1.color = "Blue"
# r1.weight = 100
# r1.style = "Simple"
#
# r2 = Robot()
# r2.name = "Second Robot"
# r2.color = "Red Giant"
# r2.weight = 500
# r2.cost = 10000

r1 = Robot("Vikas", "White", 70)
r2 = Robot("Mohit", "Grhite", 520)

r1.intro_self()
r2.intro_self()
