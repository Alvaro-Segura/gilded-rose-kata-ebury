# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            match item.name:
                case "Aged Brie":
                    update_aged_brie(item)
                case "Backstage passes to a TAFKAL80ETC concert":
                    update_backstage_pass(item)
                case "Conjured":
                    update_conjured(item)
                case _:
                    update_general(item)

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

def update_aged_brie(item):
    item.quality = min(item.quality + 1, 50)
    item.sell_in -= 1
    if item.sell_in < 0 :
        item.quality = min(item.quality + 1, 50)

def update_general(item):
    if item.sell_in > 0:
        item.quality = max(item.quality - 1, 0)
    else:
        item.quality = max(item.quality - 2, 0)
    item.sell_in -= 1

def update_backstage_pass(item):
    item.quality += 1
    if item.sell_in <= 5:
        item.quality += 1
    if item.sell_in <= 10:
        item.quality += 1

    if item.sell_in < 0:
        item.quality = 0

def update_conjured(item):
    if item.sell_in > 0:
        item.quality = max(item.quality - 2, 0)
    else:
        item.quality = max(item.quality - 4, 0)
    item.sell_in -= 1