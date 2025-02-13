# -*- coding: utf-8 -*-

class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class ItemUpdater:
    def update(self, item):
        pass

class NormalItemUpdater(ItemUpdater):
    def update(self, item):
        if item.quality > 0:
            item.quality -= 1
        item.sell_in -= 1
        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 1

class AgedBrieUpdater(ItemUpdater):
    def update(self, item):
        if item.quality < 50:
            item.quality += 1
        item.sell_in -= 1
        if item.sell_in < 0 and item.quality < 50:
            item.quality += 1

class BackstagePassUpdater(ItemUpdater):
    def update(self, item):
        if item.sell_in > 0:
            if item.quality < 50:
                item.quality += 1
                if item.sell_in < 11:
                    item.quality += 1
                if item.sell_in < 6:
                    item.quality += 1
        else:
            item.quality = 0
        item.sell_in -= 1

class SulfurasUpdater(ItemUpdater):
    def update(self, item):
        pass

class GildedRose:
    def __init__(self, items):
        self.items = items
        self.updaters = {
            "Aged Brie": AgedBrieUpdater(),
            "Backstage passes to a TAFKAL80ETC concert": BackstagePassUpdater(),
            "Sulfuras, Hand of Ragnaros": SulfurasUpdater()
        }

    def update_quality(self):
        for item in self.items:
            self.get_updater(item).update(item)

    def get_updater(self, item):
        return self.updaters.get(item.name, NormalItemUpdater())

