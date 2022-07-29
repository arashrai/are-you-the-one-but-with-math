from PossiblePairing import PossiblePairing
from itertools import permutations

class AreYouTheOne:
    name_to_id = {}
    id_to_name = {}
    all_possible_pairings = {}
    couple_odds = {}
    solution = {}
    most_likely_couple = None
    most_likely_solution = None

    def __init__(self, guys, girls, solution=None):
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
        
        if solution:
            guy_ids = []
            girl_ids = []
            for guy, girl in solution:
                guy_ids.append(self.name_to_id[guy])
                girl_ids.append(self.name_to_id[girl])
            self.solution = PossiblePairing(guy_ids, girl_ids, self.id_to_name)
            print(self.solution)

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
        # self.calculate_odds_for_all_couples()

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
        # self.calculate_odds_for_all_couples()

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
        self.most_likely_couple = None
        best_odds = 0

        for k,v in couple_counts.items():
            couple_odds[k] = v/n * 100
            if v/n * 100 > best_odds and v/n < 1:
                best_odds = v/n * 100
                self.most_likely_couple = k
        
        self.couple_odds = couple_odds

    def calculate_most_likely_solution(self):
        best_prob = 0
        self.most_likely_solution = None

        for pairing in self.all_possible_pairings:
            prob = 1
            for guy, girl in pairing.pairs:
                prob *= self.get_odds_for_couple(self.id_to_name[guy], self.id_to_name[girl])/100

            if prob > best_prob:
                best_prob = prob
                self.most_likely_solution = pairing

    def get_odds_for_couple(self, guy, girl):
        pair = (self.name_to_id[guy], self.name_to_id[girl])
        return self.couple_odds.get(pair, 0)

    def pretty_print_odds(self):
        if len(self.couple_odds) == 0:
            self.calculate_odds_for_all_couples()

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

    def print_most_likely_solution(self):
        if self.most_likely_solution == None:
            self.calculate_most_likely_solution()
        
        print()
        print("The following solution has the best likelihood of being correct:")
        print(self.most_likely_solution)

    def get_most_likely_solution(self):
        if self.most_likely_solution == None:
            self.calculate_most_likely_solution()
        return self.most_likely_solution.get_couples()

    def run_truth_both(self, guy, girl):
        return self.solution.contains(self.name_to_id[guy], self.name_to_id[girl])

    def run_lights(self, guys, girls):
        num_lights = 0
        for i in range(len(guys)):
            if self.run_truth_both(guys[i], girls[i]):
                num_lights += 1
        return num_lights

    def get_most_likely_couple(self):
        if self.most_likely_couple == None:
            self.calculate_odds_for_all_couples()
        return self.id_to_name[self.most_likely_couple[0]], self.id_to_name[self.most_likely_couple[1]]

    def is_show_over(self):
        return len(self.all_possible_pairings) == 1