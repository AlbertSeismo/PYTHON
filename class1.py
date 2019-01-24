from matplotlib.pyplot import *
import matplotlib.pyplot as plt 

class Circle(object):
    def __init__(self,radius =3,color ='blue'):
        self.radius =radius
        self.color = color
        
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0,0),radius = self.radius, fc= self.color))
        plt.axis('scaled')
        grid(True)
        plt.show()

redcirc = Circle(10, 'red')
print(redcirc.radius)
print(redcirc.color)

redcirc.drawCircle()




            


