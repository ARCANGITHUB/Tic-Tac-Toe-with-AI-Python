# our class Ship
class Ship:
    def __init__(self, name):
        self.country = None
        self.name = name

        # self.cargo = 0

    # the old sail method that you need to rewrite
    def sail(self, country):
        self.country = country
        return "The {} has sailed for {}!".format(self.name, self.country)


black_pearl = Ship("Black Pearl")
print(black_pearl.sail(input()))
