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

# for k,v in show.name_to_id.items():
#     print(k, v)

for p in show.all_possible_pairings:
    print(p)


show.truth_booth("Adam", "Amber", False)

for p in show.all_possible_pairings:
    print(p)

print(show.get_odds_for_couple("Adam", "Amber"))