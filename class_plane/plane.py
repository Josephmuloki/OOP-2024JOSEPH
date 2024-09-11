class Plane:
    def __init__(self, airline, model, capacity):
        self.airline = airline
        self.model = model
        self.capacity = capacity

    def take_off(self):
        return f"The {self.airline} {self.model} is taking off."

    def land(self):
        return f"The {self.airline} {self.model} is landing."

# Example usage
plane = Plane("Delta", "Boeing 747", 416)
print(plane.take_off())  
print(plane.land())      
