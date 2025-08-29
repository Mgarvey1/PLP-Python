# Base class
class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life  # in hours

    def call(self, number):
        print(f"Calling {number} from {self.model}...")

    def charge(self):
        print(f"{self.model} is charging... Battery life restored to {self.battery_life} hours.")


# Subclass - adds camera functionality
class CameraPhone(Smartphone):
    def __init__(self, brand, model, battery_life, camera_megapixels):
        super().__init__(brand, model, battery_life)
        self.camera_megapixels = camera_megapixels

    def take_photo(self):
        print(f"Taking a photo with {self.camera_megapixels} MP camera on {self.model}.")


# Create objects
phone1 = Smartphone("Samsung", "Galaxy S23", 30)
phone2 = CameraPhone("Apple", "iPhone 15", 25, 48)

# Test methods
phone1.call("123-456-7890")
phone2.take_photo()
phone2.charge()
