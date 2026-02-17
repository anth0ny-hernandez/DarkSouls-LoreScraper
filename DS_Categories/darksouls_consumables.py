from darksouls_class import DarkSouls

# ds1 = DarkSouls("http://darksouls.wikidot.com/consumables", "class", "wiki-content-table")
ds2 = DarkSouls("http://darksouls.wikidot.com/multiplayer-items", "class", "wiki-content-table")
# ds3 = DarkSouls("http://darksouls.wikidot.com/covenants", "class", "wiki-content-table")

# print(ds1.url)
# ds1.get_all_urls("class", "wiki-content-table")
ds2.run()