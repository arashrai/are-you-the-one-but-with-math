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

show = AreYouTheOne(guys, girls)

# Week 1
print("Week 1!")
show.truth_booth("Chris T", "Shanley", False)
show.pretty_print_odds()
show.print_most_likely_pairing()
show.lights(guys, ["Brittany", "Ashleigh", "Jessica", "Colyesia", "Jacy", "Shanley", "Paige", "Simone", "Amber", "Kayla"], 2)
show.pretty_print_odds()
show.print_most_likely_pairing()

# Week 2
print("Week 2!")
show.truth_booth("Ethan", "Jessica", False)
show.pretty_print_odds()
show.print_most_likely_pairing()
show.lights(guys, ["Shanley", "Simone", "Paige", "Jessica", "Ashleigh", "Amber", "Brittany", "Jacy", "Kayla", "Colyesia"], 4)
show.pretty_print_odds()
show.print_most_likely_pairing()

# Week 3
print("Week 3!")
show.truth_booth("John", "Simone", False)
show.pretty_print_odds()
show.print_most_likely_pairing()
show.lights(guys, ["Brittany", "Paige", "Simone", "Colyesia", "Ashleigh", "Amber", "Shanley", "Jessica", "Kayla", "Jacy"], 2)
show.pretty_print_odds()
show.print_most_likely_pairing()

# Week 4
print("Week 4!")
show.truth_booth("Dillan", "Jessica", False)
show.pretty_print_odds()
show.print_most_likely_pairing()
show.lights(guys, ["Amber", "Paige", "Ashleigh", "Colyesia", "Simone", "Kayla", "Jacy", "Shanley", "Brittany", "Jessica"], 2)
show.pretty_print_odds()
show.print_most_likely_pairing()

# Week 5
print("Week 5!")
show.truth_booth("Dre", "Ashleigh", False)
show.pretty_print_odds()
show.print_most_likely_pairing()
show.truth_booth("Dillan", "Colyesia", True)
show.pretty_print_odds()
show.print_most_likely_pairing()
show.lights(guys, ["Shanley", "Simone", "Paige", "Colyesia", "Brittany", "Amber", "Jessica", "Jacy", "Ashleigh", "Kayla"], 5)
show.pretty_print_odds()
show.print_most_likely_pairing()

# Week 6
print("Week 6!")
show.truth_booth("Chris T", "Paige", True)
show.pretty_print_odds()
show.print_most_likely_pairing()
show.lights(guys, ["Ashleigh", "Brittany", "Paige", "Colyesia", "Shanley", "Amber", "Simone", "Jacy", "Jessica", "Kayla"], 5)
show.pretty_print_odds()
show.print_most_likely_pairing()

# Week 7
print("Week 7!")
show.truth_booth("Ryan", "Kayla", False)
show.pretty_print_odds()
show.print_most_likely_pairing()
show.lights(guys, ["Shanley", "Jacy", "Paige", "Colyesia", "Simone", "Amber", "Jessica", "Brittany", "Ashleigh", "Kayla"], 7)
show.pretty_print_odds()
show.print_most_likely_pairing()


# WOOO Only took 7 weeks, the __contestants__ took 9
# Update: Only takes 6 weeks with most_likely_pairing approach
