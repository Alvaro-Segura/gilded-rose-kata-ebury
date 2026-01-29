from gilded_rose import GildedRose, Item


def test_foo():
    item = Item("foo", 0, 0)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.name == "foo"


def test_quality_greater_than_zero():
    item = Item("foo", 0, 1)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.name == "foo"


def test_sell_in_greater_than_zero():
    item = Item("foo", 1, 1)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.name == "foo"


def test_backstage_quality_increases():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 40)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.quality == 43


def test_sell_in_less_than_zero():
    item = Item("foo", -1, 2)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.quality == 0


def test_backstage_sell_in_less_than_zero():
    item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 1)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.quality == 0


def test_aged_brie_sell_in_less_than_zero():
    item = Item("Aged Brie", -1, 1)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.quality == 3


def test_conjured_item_sell_in_greater_than_zero():
    item = Item("Conjured", 2, 10)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == 1
    assert item.quality == 8


def test_conjured_item_sell_in_less_than_zero():
    item = Item("Conjured", -1, 10)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == -2
    assert item.quality == 6


def test_multiple_items():
    aged_brie = Item("Aged Brie", -1, 1)
    backstage_pass = Item("Backstage passes to a TAFKAL80ETC concert", -1, 1)
    sulfuras = Item("Sulfuras, Hand of Ragnaros", 5, 60)
    conjured_item = Item("Conjured", -1, 10)
    foo_item = Item("foo", 0, 0)

    gilded_rose = GildedRose([aged_brie, backstage_pass, sulfuras, conjured_item, foo_item])
    gilded_rose.update_quality()

    assert aged_brie.quality == 3
    assert backstage_pass.quality == 0
    assert sulfuras.quality == 80
    assert conjured_item.quality == 6
    assert foo_item.quality == 0


def test_representation_item():
    item = Item("foo", -1, 2)
    assert str(item) == "foo, -1, 2"
