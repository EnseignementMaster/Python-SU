__author__ = 'lantos'

import unittest

from Chap_8_Objets.Chap_8_Objets_Point import *


class TestPoint(unittest.TestCase):

    def setUp(self):
        self.nullPoint = Point(0.0, 0.0)
        self.minusOnePoint = Point(-1.0, -1.0)

    def test_initialization(self):
        self.assertAlmostEqual(self.nullPoint.x, 0.0, delta=1e-15)
        self.assertAlmostEqual(self.nullPoint.y, 0.0, delta=1e-15)

    def test_translate(self):
        p = self.nullPoint
        p.translate(-1.0, -1.0)
        self.assertAlmostEqual(p.x, 0.0, delta=1e-15)
        self.assertAlmostEqual(p.y, 0.0, delta=1e-15)

    def test_Positivity(self):
        p = self.minusOnePoint
        self.assertAlmostEqual(p.x, 0.0, delta=1e-15)
        self.assertAlmostEqual(p.y, 0.0, delta=1e-15)

    def test_Type(self):
        p = self.minusOnePoint
        self.assertEqual(type(p), Point)

    def test_NonZero(self):
        p = self.minusOnePoint
        self.assertTrue(p)


if __name__ == '__main__':
    unittest.main()
