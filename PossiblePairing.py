class PossiblePairing:

    guys = []
    girls = []

    # guys are the first tuple value in the pairs set 
    pairs = set()

    def __init__(self, guys, girls):
        self.pairs = set()
        self.guys = guys
        self.girls = girls
    
        for ind, val in enumerate(guys):
            self.pairs.add( (guys[ind], girls[ind]) )

    def __repr__(self):
        repr_string = "Pairings:\n"

        for guy, girl in self.pairs:
            repr_string += str(guy) + " <-> " + str(girl) + "\n"

        return repr_string
