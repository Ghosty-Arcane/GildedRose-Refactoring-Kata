# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_quality_default(self):
        items = [
            Item('foo', 5, 5),
            Item('foo', 0, 5),
            Item('foo', 5, 0),
            Item('foo', 0, 0)
            ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].quality)
        self.assertEqual(3, items[1].quality)
        self.assertEqual(0, items[2].quality)
        self.assertEqual(0, items[3].quality)
        return
    
    def test_quality_sulfuras(self):
        items = [
            Item('Sulfuras, Hand of Ragnaros', 5, 80),
            Item('Sulfuras, Hand of Ragnaros', 0, 80)
            ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)
        self.assertEqual(80, items[1].quality)
        return
    
    def test_quality_brie(self):
        items = [
            Item('Aged Brie', 5, 0),
            Item('Aged Brie', 1, 0),
            Item('Aged Brie', 0, 0),
            Item('Aged Brie', 5, 50),
            Item('Aged Brie', 0, 49)
            ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].quality)
        self.assertEqual(1, items[1].quality)
        self.assertEqual(2, items[2].quality)
        self.assertEqual(50, items[3].quality)
        self.assertEqual(50, items[4].quality)
        return
    
    def test_quality_backstage(self):
        items = [
            Item('Backstage passes to a TAFKAL80ETC concert', 15, 0),
            Item('Backstage passes to a TAFKAL80ETC concert', 9, 0),
            Item('Backstage passes to a TAFKAL80ETC concert', 4, 0),
            Item('Backstage passes to a TAFKAL80ETC concert', 0, 40),
            Item('Backstage passes to a TAFKAL80ETC concert', 15, 50)
            ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].quality)
        self.assertEqual(2, items[1].quality)
        self.assertEqual(3, items[2].quality)
        self.assertEqual(0, items[3].quality)
        self.assertEqual(50, items[4].quality)
        return

        
if __name__ == '__main__':
    unittest.main()
