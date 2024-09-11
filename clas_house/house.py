class House:
    def __init__(self, address, num_rooms, price):
        self.address = address
        self.num_rooms = num_rooms
        self.price = price

    def show_address(self):
        return f"The house is located at {self.address}."

    def show_details(self):
        return f"The house has {self.num_rooms} rooms and costs ${self.price}."

# Example usage
house = House("123 Main St", 4, 350000)
print(house.show_address()) 
print(house.show_details())  
