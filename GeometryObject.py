import math
import enum

@enum.unique
class GeometryType (enum.Enum):
    Triangle = 1
    Circle   = 2

class InvalidGeometryObject (Exception):
    "Geometry Object with specified parameters can't being exist"
    pass

class GeometryObject:
    def CalculateSquare (self, type: GeometryType, *args):
        if type == GeometryType.Triangle:
            aTriangle = Triangle (args[0], args[1], args[2])
            return aTriangle.CalculateSquare()
        elif type == GeometryType.Circle:
            aCircle = Circle (args[0])
            return aCircle.CalculateSquare()
        else:
            raise TypeError ("Type of figure is undefinded") 
    
class Triangle (GeometryObject):
    def __init__ (self, a = 0, b = 0 , c = 0):
        if a >= 0 and b >= 0 and c >= 0:
            if (a + b > c) and (a + c > b) and (c + b > a): 
                self.a = a
                self.b = b
                self.c = c
            else:
                raise InvalidGeometryObject
        else:
            raise ValueError ("Parameters can't being negative")   

    def CalculateSquare(self):
        p = (self.a + self.b + self.c) / 2
        s = math.sqrt ((p * (p - self.a) * (p - self.b) * (p - self.c)))
        return s
    
    def isRight(self) -> bool:
        return self.a**2 + self.b**2 == self.c**2 
    
class Circle (GeometryObject):
    def __init__ (self, r = 0):
        if r >= 0:
            self.r = r
        else:
            raise ValueError ("Radius can't being negative")        

    def CalculateSquare(self):
        s = math.pi * self.r**2
        return s

'''
Unfortunately, it was not completely clear what is meant by "Вычисление площади фигуры без знания типа фигуры"

I initially thought that here talking about a figure with an indefinite geometric shape. For example,
given by parametric curves (e.g. [Bézier curve](https://en.wikipedia.org/wiki/B%C3%A9zier_curve)).
After thinking about it, I assumed that most likely this is not the case. But just in case, I will tell you the concept of this approach below.

Let's say there is some curve defined by control points and their weights. Then, with the help of these points, you can restore the equation of the figure,
compute an integral and find the figure's square


from scipy import integrate

class Pole:
    def __init__ (x, y, weight):
        ...
        pass

class Curve (GeometryObject):
    def func (*args):
        # return a curve's function
        pass
    
    def CalculateSquare (self, start, end, *args: Pole):
        # Calculate square something like this
        s = integrate.quad (self.func (args), start, end) 
'''
