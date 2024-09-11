class Phone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life

    def make_call(self, number):
        return f"Calling {number} from {self.brand} {self.model}."

    def send_message(self, number, message):
        return f"Sending message to {number}: {message}"

# Example usage
phone = Phone("Apple", "iPhone 13", "20 hours")
print(phone.make_call("123-456-7890"))  
print(phone.send_message("123-456-7890", "Hello!"))
