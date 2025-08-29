class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin

    def introduce(self):
        return f"I am {self.name}, born of {self.origin}, wielding the power of {self.power}!"

    def use_power(self):
        return f"{self.name} uses {self.power} to save the day!"
class TechHero(Superhero):
    def __init__(self, name, power, origin, gadget):
        super().__init__(name, power, origin)
        self.gadget = gadget

    def use_power(self):
        return f"{self.name} activates {self.gadget} and unleashes {self.power} with precision!"

    def upgrade_gadget(self, new_gadget):
        self.gadget = new_gadget
        return f"{self.name} upgraded to {self.gadget}!"
