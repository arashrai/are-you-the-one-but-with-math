from AreYouTheOne import AreYouTheOne

guys = [
    "Adam",
    "Dre",
    "Scali",
    "Chris",
    "Dillan",
    "Ethan",
    "Joey",
    "JJ",
    "Ryan",
    "Wes"
]

girls = [
    "Amber",
    "Ashleigh",
    "Brittany",
    "Colyesia",
    "Jacy",
    "Jessica",
    "Kayla",
    "Paige",
    "Shanley",
    "Simone"
]

show = AreYouTheOne(guys, girls)
show.truth_booth("Adam", "Amber", True)

print(show.couple_odds)
