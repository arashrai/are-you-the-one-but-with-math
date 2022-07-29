from AreYouTheOne import AreYouTheOne
from PossiblePairing import PossiblePairing

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

solution = [
    ("Adam", "Amber"),
    ("Dre", "Ashleigh"),
    ("Scali", "Brittany"),
]

show = AreYouTheOne(guys, girls, solution)

# print(show.run_truth_both("Adam", "Amber"))
# print(show.run_truth_both("Adam", "Brittany"))
# print(show.run_lights(("Adam", "Dre", "Scali"), ("Amber", "Ashleigh", "Brittany")))
# print(show.run_lights(("Adam", "Dre", "Scali"), ("Amber", "Brittany", "Ashleigh")))

# show.truth_booth("Adam", "Amber", True)
# show.pretty_print_odds()
# show.print_most_likely_solution()
# print(show.get_most_likely_couple())
# print(show.get_most_likely_solution())

n = 1
while not show.is_show_over():
    print("Week", n)
    print()
    guy, girl = show.get_most_likely_couple()
    show.truth_booth(guy, girl, show.run_truth_both(guy, girl))

    guys, girls = show.get_most_likely_solution()
    show.lights(guys, girls, show.run_lights(guys, girls))
    show.pretty_print_odds()
    n += 1
    print()