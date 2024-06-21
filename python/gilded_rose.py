# -*- coding: utf-8 -*-
from __future__ import annotations

BRIE = 'Aged Brie'
BACKSTAGE = 'Backstage passes to a TAFKAL80ETC concert'
SULFURAS = 'Sulfuras, Hand of Ragnaros'
CONJURED = 'Conjured Mana Cake'

class GildedRose(object):

    def __init__(self, items):
        self.items: list[Item] = items

    def update_quality(self):
        for item in self.items:
            # Handles sell-in drop
            if item.name != SULFURAS:
                item.sell_in = item.sell_in - 1

            # Handles quality drop
            qualityChange = -1
            if item.sell_in < 0:
                qualityChange = qualityChange *2
            if item.name == BACKSTAGE:
                if item.sell_in < 0:
                    qualityChange = -item.quality
                elif item.sell_in < 6:
                    qualityChange = 3
                elif item.sell_in < 11:
                    qualityChange = 2
                else:
                    qualityChange = 1
            elif item.name == BRIE:
                qualityChange = -qualityChange
            elif item.name == CONJURED:
                qualityChange = qualityChange *2
            elif item.name == SULFURAS:
                return
            self._QualityChanger(item, qualityChange)
            

    def _QualityChanger(self, item: Item, change: int) ->None:
        if item.name == SULFURAS:
            return
        item.quality = max(0, min(50, item.quality + change))
        return

class Item:
    def __init__(self, name, sell_in, quality):
        self.name: str = name
        self.sell_in: int = sell_in
        self.quality: int = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
