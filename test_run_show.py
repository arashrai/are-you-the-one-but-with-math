from AreYouTheOne import AreYouTheOne

guys = [
    "Adam",
    "Dre",
    "Scali",
]

girls = [
    "Amber",
    "Ashleigh",
    "Brittany",
]

show = AreYouTheOne(guys, girls)

show.truth_booth("Adam", "Amber", True)
show.pretty_print_odds()
