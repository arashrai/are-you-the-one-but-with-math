class PossiblePairing:

    guys = []
    girls = []

    # guys are the first tuple value in the pairs set 
    pairs = set()

    def __init__(self, guys, girls):
        self.guys = guys
        self.girls = girls
        for ind, val in enumerate(guys):
            self.pairs.add( (guys[ind], girls[ind]))
        print(self.pairs)


# PossiblePairing(["richy", "guy", "arash"], ["nat", "chelsea", "jess"])