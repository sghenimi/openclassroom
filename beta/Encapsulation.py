class Coffee:
    TANK_LEVEL = 100

    def _start_machine(self):
        if self.TANK_LEVEL>20:
            return True
        else:
            print("please aadd water")
            return False

    def __boil_water(self):
        return "Boilling ..."

    def make_coffe(self):
        if self._start_machine():
            self.TANK_LEVEL -= 20
            print(self.__boil_water())
            print("Take you coffee")

cafe = Coffee()

print("### Public method : ", cafe.make_coffe())
print("### Protected method : ", cafe._start_machine())

print("### Private method Access : ", cafe._Coffee__boil_water())
print("### Private method : ", cafe.__boil_water())