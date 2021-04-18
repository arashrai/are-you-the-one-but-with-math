from PossiblePairing import PossiblePairing
from itertools import permutations

class AreYouTheOne:
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


    def truth_booth(self, p1, p2, is_match):
        """
        Eliminates impossible pairings.
        """
        pass

    def lights(self, pairing, num_lights):
        """
        Eliminates impossible pairings.
        """
        pass