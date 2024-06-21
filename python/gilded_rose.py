# -*- coding: utf-8 -*-
from __future__ import annotations
from enum import Enum

class Special(Enum):
    BRIE = 'Aged Brie'
    BACKSTAGE = 'Backstage passes to a TAFKAL80ETC concert'
    SULFURAS = 'Sulfuras, Hand of Ragnaros'
    CONJURED = 'Conjured Mana Cake'


class GildedRose(object):

    def __init__(self, items):
        self.items: list[Item] = items

    def update_quality(self):
        for item in self.items:
            if Special.SULFURAS.value in item.name:
                continue
            # Handles sell-in drop
            item.sell_in = item.sell_in - 1

            # Handles quality drop
            if Special.BACKSTAGE.value in item.name:
                if item.sell_in < 0:
                    item.quality = 0
                    continue
                elif item.sell_in < 6:
                    qualityChange = 3
                elif item.sell_in < 11:
                    qualityChange = 2
                else:
                    qualityChange = 1
            elif Special.BRIE.value in item.name:
                qualityChange = 2 if item.sell_in < 0 else 1
            elif Special.CONJURED.value in item.name:
                qualityChange = -4 if item.sell_in < 0 else -2
            else:
                qualityChange = -2 if item.sell_in < 0 else -1

            self._QualityChanger(item, qualityChange)
            

    def _QualityChanger(self, item: Item, change: int) ->None:
        item.quality = max(0, min(50, item.quality + change))
        return

class Item:
    def __init__(self, name, sell_in, quality):
        self.name: str = name
        self.sell_in: int = sell_in
        self.quality: int = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
