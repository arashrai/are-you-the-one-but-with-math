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

for k,v in show.name_to_id.items():
    print(k, v)