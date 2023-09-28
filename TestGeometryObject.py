import unittest
import math
import GeometryObject as go

class TestTriangle (unittest.TestCase):
    def setUp(self):
        self.triangle         = go.Triangle (3, 4, 5)
        self.nonRigntTriangle = go.Triangle (3, 3, 3)
      
    def test_Triangle_valid(self):
        self.assertEqual (self.triangle.CalculateSquare(), 6)

        self.assertTrue  (self.triangle.isRight())
        self.assertFalse (self.nonRigntTriangle.isRight())

    def test_Triangle_invalid(self):
        with self.assertRaises (go.InvalidGeometryObject): 
            go.Triangle (1, 5)
        with self.assertRaises (go.InvalidGeometryObject): 
            go.Triangle (1, 2, 3)
        with self.assertRaises (ValueError): 
            go.Triangle (-3, 3, 3)

class TestCircle (unittest.TestCase):
    def setUp(self):
        self.circle = go.Circle (5)
      
    def test_Circle_valid(self):
        self.assertEqual (self.circle.CalculateSquare(), 5**2 * math.pi)
        self.assertEqual (go.Circle().CalculateSquare(), 0)

    def test_Circle_invalid(self):
        with self.assertRaises (ValueError): 
            go.Circle (-3)

class TestGeometryObject (unittest.TestCase):
    def setUp(self):
        self.geometryObject = go.GeometryObject()

    def test_GeometryObject_valid(self):
        self.assertEqual (self.geometryObject.CalculateSquare (go.GeometryType.Triangle, 3, 4, 5),            6)
        self.assertEqual (self.geometryObject.CalculateSquare (go.GeometryType.Triangle, 3, 4, 5, 9, 10, 55), 6)
        self.assertEqual (self.geometryObject.CalculateSquare (go.GeometryType.Triangle, 3, 4, 5, -2),        6)

        self.assertEqual (self.geometryObject.CalculateSquare (go.GeometryType.Circle, 5),             5**2 * math.pi)
        self.assertEqual (self.geometryObject.CalculateSquare (go.GeometryType.Circle, 5, 2, 6, 7, 8), 5**2 * math.pi)
        self.assertEqual (self.geometryObject.CalculateSquare (go.GeometryType.Circle, 5, -2),         5**2 * math.pi)

    def test_GeometryObject_invalid(self):
        with self.assertRaises (IndexError): 
            self.geometryObject.CalculateSquare (go.GeometryType.Triangle, 3)
        with self.assertRaises (IndexError): 
            self.geometryObject.CalculateSquare (go.GeometryType.Circle)
        with self.assertRaises (TypeError): 
            self.geometryObject.CalculateSquare (0, 5)

if __name__ == "__main__":
    unittest.main()
