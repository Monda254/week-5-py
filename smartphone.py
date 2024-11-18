class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: ${self.price}")

    def make_call(self, number):
        print(f"Calling {number}...")

    def send_text(self, number, message):
        print(f"Sending text to {number}: {message}")

# Inheriting the Smartphone class
class Smartwatch(Smartphone):
    def __init__(self, brand, model, price, screen_size):
        super().__init__(brand, model, price)  # Inherit from Smartphone
        self.screen_size = screen_size

    def display_info(self):
        super().display_info()  # Call the base class method
        print(f"Screen Size: {self.screen_size} inches")

    def track_heart_rate(self):
        print("Tracking heart rate...")


phone = Smartphone("Apple", "iPhone 14", 999)
watch = Smartwatch("Apple", "Apple Watch Series 8", 399, 1.9)


phone.display_info()
phone.make_call("123-456-7890")
phone.send_text("123-456-7890", "Hello, how are you?")

print("\n--- Smartwatch Info ---")
watch.display_info()
watch.track_heart_rate()
