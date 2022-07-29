class PossiblePairing:
    pairs = set()
    guys = []
    girls = []
    id_to_name = {}

    # guys are the first tuple value in the pairs set 
    pairs = set()

    def __init__(self, guys, girls, id_to_name):
        self.pairs = set()
        self.guys = guys
        self.girls = girls
        self.id_to_name = id_to_name

        for ind, val in enumerate(guys):
            self.pairs.add( (guys[ind], girls[ind]) )

    def __repr__(self):
        repr_string = ""

        for guy, girl in self.pairs:
            repr_string += self.id_to_name[guy] + " <-> " + self.id_to_name[girl] + "\n"

        repr_string += "\n"

        return repr_string

    def contains(self, guy_id, girl_id):
        return (guy_id, girl_id) in self.pairs

    def get_couples(self):
        guy_names = []
        girl_names = []

        for guy, girl in self.pairs:
            guy_names.append(self.id_to_name[guy])
            girl_names.append(self.id_to_name[girl])
        
        return guy_names, girl_names