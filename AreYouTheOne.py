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
            self.all_possible_pairings.append(PossiblePairing(guy_ids, p))

    def truth_booth(self, guy, girl, is_match):
        """
        Eliminates impossible pairings.
        """

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
        # guys and girls are arrays of names, now converting to ids then constructing 
        #   PossiblePairing from it
        print(guys)
        for ind, guy in enumerate(guys): 
            guys[ind] = self.name_to_id[guy]
        for ind, girl in enumerate(girls):
            girls[ind] = self.name_to_id[girl]
        print(guys)
            
        pairing = PossiblePairing(guys, girls)

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
        
