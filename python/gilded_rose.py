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
            # Handles quality drop
            if item.name != BRIE and item.name != BACKSTAGE:
                if item.quality > 0:
                    if item.name != SULFURAS:
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == BACKSTAGE:
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1

            # Handles sell-in drop
            if item.name != SULFURAS:
                item.sell_in = item.sell_in - 1

            # Handles expiry quality drop
            if item.sell_in < 0:
                if item.name != BRIE:
                    if item.name != BACKSTAGE:
                        if item.quality > 0:
                            if item.name != SULFURAS:
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1

    def _QualityChanger(self, item: Item, change: int) ->None:
        item.quality = item.quality + change
        return

class Item:
    def __init__(self, name, sell_in, quality):
        self.name: str = name
        self.sell_in: int = sell_in
        self.quality: int = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
