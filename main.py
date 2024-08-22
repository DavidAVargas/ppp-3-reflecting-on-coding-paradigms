# functional prompt 

def flatten_and_sort(array):
    flatten = [item for sublist in array for item in sublist]
    return sorted(flatten)

# object oriented prompt

class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    # Define a repair() method that will update the condition of the podracer to "repaired".
    def repair(self):
        self.condition = "repaired"

# Define a new class, AnakinsPod, that inherits from Podracer and has a boost method.
class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def boost(self):
        self.max_speed *= 2

# Define another class, SebulbasPod, that inherits from Podracer and has a flame_jet method.
class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def flame_jet(self, other):
        other.condition = "trashed"