from PossiblePairing import PossiblePairing
from itertools import permutations

class AreYouTheOne:
    name_to_id = {}
    all_possible_pairings = {}

    def __init__(self, guys, girls):
        self.name_to_id = {}
        
        guy_ids = []
        girl_ids = []
        id = 1
        
        for g in guys:
            self.name_to_id[g] = id
            guy_ids.append(id)
            id += 1
        
        for g in girls:
            self.name_to_id[g] = id
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

    # def lights(self, pairing, num_lights):
    #     """
    #     Eliminates impossible pairings.
    #     """
    #     # I'm given a set of pairs and a number of lights implying the number of 
    #     # correct pairs. I will compare each `all_possible_pairings` with `pairing`
    #     # and if `num_lights + 1` or more number of pairs are the same, then remove this `pairing`

    #     new_possible_pairings = []
    #     for test_pairing in self.all_possible_pairings:
    #         count_of_matches = 0
    #         for pair in test_pairing: 
    #             if pair in pairing.pairs:
    #                 count_of_matches += 1
            
    #         if count_of_matches <= num_lights:
    #             new_possible_pairings.append(test_pairing)
        
    #     self.all_possible_pairings = new_possible_pairings

    def lights(self, pairing, num_lights):
        """
        Eliminates impossible pairings.
        """
        new_possible_pairings = []
        
        for test_pairing in self.all_possible_pairings:
            count_of_lights = 0
            for pair in test_pairing:
                if pair in pairing.pairs:
                    count_of_lights += 1
        
            if count_of_lights == num_lights:
                new_possible_pairings.append(test_pairing)
        
        self.all_possible_pairings = new_possible_pairings
