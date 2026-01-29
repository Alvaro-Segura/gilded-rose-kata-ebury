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


def test_representation_item():
    item = Item("foo", -1, 2)
    assert str(item) == "foo, -1, 2"
