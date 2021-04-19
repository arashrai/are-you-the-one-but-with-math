from PossiblePairing import PossiblePairing
from itertools import permutations

class AreYouTheOne:
    name_to_id = {}
    id_to_name = {}
    all_possible_pairings = {}
    couple_odds = {}

    def __init__(self, guys, girls):
        self.name_to_id = {}
        self.id_to_name = {}

        guy_ids = []
        girl_ids = []
        id = 1
        
        for g in guys:
            self.name_to_id[g] = id
            self.id_to_name[id] = g
            guy_ids.append(id)
            id += 1
        
        for g in girls:
            self.name_to_id[g] = id
            self.id_to_name[id] = g
            girl_ids.append(id)
            id += 1

        self.all_possible_pairings = []
        
        possible_permutations = permutations(girl_ids)

        for p in possible_permutations:
            self.all_possible_pairings.append(PossiblePairing(guy_ids, p, self.id_to_name))

    def truth_booth(self, guy, girl, is_match):
        """
        Eliminates impossible pairings.
        """
        print("Running truth_booth with " + guy + " and " + girl + " with match: " + str(is_match))

        new_possible_pairings = []

        pair = (self.name_to_id[guy], self.name_to_id[girl])

        for test_pairing in self.all_possible_pairings:
            if is_match and pair in test_pairing.pairs:
                new_possible_pairings.append(test_pairing)
            elif not is_match and pair not in test_pairing.pairs:
                new_possible_pairings.append(test_pairing)
    
        self.all_possible_pairings = new_possible_pairings
        self.calculate_odds_for_all_couples()

    def lights(self, guys, girls, num_lights):
        """
        Eliminates impossible pairings.
        """
        print("Running lights with " + str(num_lights) + " lights")
        print("Guys: ", guys)
        print("Girls: ", girls)

        # guys and girls are arrays of names, now converting to ids then constructing 
        #   PossiblePairing from it
        new_guys = []
        new_girls = []

        for guy in guys:
            new_guys.append(self.name_to_id[guy])
        for girl in girls:
            new_girls.append(self.name_to_id[girl])

        pairing = PossiblePairing(new_guys, new_girls, self.id_to_name)

        # Eliminating pairs that would have made the lighting impossible
        new_possible_pairings = []

        for test_pairing in self.all_possible_pairings:
            count_of_lights = 0
            for pair in test_pairing.pairs:
                if pair in pairing.pairs:
                    count_of_lights += 1
        
            if count_of_lights == num_lights:
                new_possible_pairings.append(test_pairing)
        
        self.all_possible_pairings = new_possible_pairings
        self.calculate_odds_for_all_couples()

    def calculate_odds_for_all_couples(self):
        n = len(self.all_possible_pairings)

        # Maps couples to how many possible pairings they appear
        couple_counts = {}

        for pairing in self.all_possible_pairings:
            for pair in pairing.pairs:
                if pair not in couple_counts:
                    couple_counts[pair] = 0
                couple_counts[pair] += 1
        
        # Maps couples to a percentage chance of them being together
        couple_odds = {}

        for k,v in couple_counts.items():
            couple_odds[k] = v/n * 100
        
        self.couple_odds = couple_odds

    def get_odds_for_couple(self, guy, girl):
        pair = (self.name_to_id[guy], self.name_to_id[girl])
        return self.couple_odds.get(pair, 0)

    def pretty_print_odds(self):
        odds_array = []
        for k, v in self.couple_odds.items():
            odds_array.append( (v, k) )
        
        odds_array.sort(reverse=True)

        print()
        print("Odds for all couples:")
        print()
        for percent, couple in odds_array:
            print(self.id_to_name[couple[0]] + " <-> " + self.id_to_name[couple[1]] + ": " + str(percent) + "%")
        print()

    def print_most_likely_pairing(self):
        best_prob = 0
        best_pairing = None

        for pairing in self.all_possible_pairings:
            prob = 1
            for guy, girl in pairing.pairs:
                prob *= self.get_odds_for_couple(self.id_to_name[guy], self.id_to_name[girl])/100

            if prob > best_prob:
                best_prob = prob
                best_pairing = pairing
        
        print()
        print("The following pairing has a", str(best_prob*100) + "%", "of being correct.")
        print(best_pairing)