# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_quality_default(self):
        items = [
            Item('foo', 5, 5),
            Item('foo', 0, 5),
            Item('foo', 5, 0),
            Item('foo', 0, 0),
            Item('foo', 5, 52),
            ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].quality)
        self.assertEqual(3, items[1].quality)
        self.assertEqual(0, items[2].quality)
        self.assertEqual(0, items[3].quality)
        return

        
if __name__ == '__main__':
    unittest.main()
