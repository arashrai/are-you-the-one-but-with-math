from AreYouTheOne import AreYouTheOne

guys = [
    "Adam",
    "Chris S",
    "Chris T",
    "Dillan",
    "Dre",
    "Ethan",
    "Joey",
    "John",
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

solution = [
    ("Adam", "Shanley"),
    ("Chris S", "Jacy"),
    ("Chris T", "Paige"),
    ("Dillan", "Colyesia"),
    ("Dre", "Simone"),
    ("Ethan", "Amber"),
    ("Joey", "Brittany"),
    ("John", "Ashleigh"),
    ("Ryan", "Jessica"),
    ("Wes", "Kayla")
]

show = AreYouTheOne(guys, girls, solution)

n = 1
while not show.is_show_over():
    print("Week", n)
    print()
    guy, girl = show.get_most_likely_couple()
    show.truth_booth(guy, girl, show.run_truth_both(guy, girl))

    guys, girls = show.get_most_likely_solution()
    show.lights(guys, girls, show.run_lights(guys, girls))
    show.pretty_print_odds()
    show.print_most_likely_solution()
    n += 1
    print()
