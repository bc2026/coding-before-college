class animal:

    def __init__ (self, common_name, species, mammality):
        self.common_name = common_name
        self.species = species
        self.mammality = mammality

    def get_common_name(self):
        return self.common_name
    def isMammal(self):
        if(self.mammality == True):
            return "is"
        else:
            return "is not"

    def get_species(self):
        return self.species

a = animal("dog", "canine", True)

print(f"{'Common Name' :<20}{'Species' : ^40}{'Mammality': >20}")
print("{:<20}".format(a.get_common_name()), "{:^22}".format(a.get_species()),"{:>20}".format(a.isMammal()))
