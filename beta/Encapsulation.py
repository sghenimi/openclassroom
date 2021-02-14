class Coffee:
    WATER_LEVEL = 100

    def start_machine(self):
        if self.TANK_LEVEL>20:
            return True
        else:
            print("please aadd water")
            return False

    def boil_coffee(self):
        return "Boilling ..."

    def make_coffe(self):
        if self.start_machine():
            self.TANK_LEVEL -= 20
            print(self.boil_coffee())
            print("Take you coffee")

cafe = Coffee()
cafe.make_coffe()