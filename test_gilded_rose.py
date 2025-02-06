# -*- coding: utf-8 -*-
import unittest
from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    # Logical Error 1: Normal items' quality should never be negative
    def test_normal_item_quality_never_negative(self):
        items = [Item("Normal Item", sell_in=3, quality=0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].quality)  # Quality should not be negative

    # Logical Error 2: Expired items' quality should decrease twice as fast
    def test_expired_item_quality_decreases_twice_as_fast(self):
        items = [Item("Normal Item", sell_in=0, quality=6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(5, items[0].quality)  # Quality should decrease by 2, not 1

    # Logical Error 3: "Backstage passes" should drop to zero quality after the concert
    def test_backstage_passes_quality_drops_to_zero_after_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=25)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(25, items[0].quality)  # Quality should be 0 after expiration

    # Syntax Error: Calling a non-existent method should raise an AttributeError
    def test_calling_nonexistent_method_should_fail(self):
        items = [Item("Elixir of the Mongoose", sell_in=5, quality=7)]
        gilded_rose = GildedRose(items)
        with self.assertRaises(AttributeError):  
            gilded_rose.get_item()  # This method does not exist and should raise an error

if __name__ == '__main__':
    unittest.main()


