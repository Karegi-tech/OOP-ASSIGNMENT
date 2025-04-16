# QUESTION 1
class Smartphone:
    def __init__(self, brand, model, operating_system, storage_gb, ram_gb, battery_mah, screen_size_inches):
        self.brand = brand
        self.model = model
        self.operating_system = operating_system
        self.storage_gb = storage_gb
        self.ram_gb = ram_gb
        self.battery_mah = battery_mah
        self.screen_size_inches = screen_size_inches
        self.is_on = False
        self.current_app = None
        self._battery_level = 100.0
        
def introduce(self):
    print(f"Hello, I am a {self.brand} {self.model} smartphone running torage, {self.ram_gb}GB RAM, and a {self.screen_size_inches}-inch display.")    
class apple(Smartphone):
    def __init__(self, model, storage_gb, ram_gb, battery_mah, screen_size_inches):
        super().__init__("Apple", model, "iOS", storage_gb, ram_gb, battery_mah, screen_size_inches)
    def introduce(self):
        print(f"Hello, I am an Apple {self.model} smartphone running iOS, with {self.storage_gb}GB storage, {self.ram_gb}GB RAM, and a {self.screen_size_inches}-inch display.")
         #Example usage
iphone = apple("iPhone 14", 128, 6, 3279, 6.1)  
print(iphone.introduce())


class samsung(Smartphone):
    def __init__(self, model, storage_gb, ram_gb, battery_mah, screen_size_inches):
        super().__init__("Samsung", model, "Android", storage_gb, ram_gb, battery_mah, screen_size_inches)
    def introduce(self):
        print(f"Hello, I am a Samsung {self.model} smartphone running Android, with {self.storage_gb}GB storage, {self.ram_gb}GB RAM, and a {self.screen_size_inches}-inch display.")

#Example usage
galaxy = samsung("Galaxy S21", 256, 8, 4000, 6.2)
print(galaxy.introduce())

# QUESTION 2

class Animal:
    def move(self):
        return "moves in some way"

class Dog(Animal):
       def move(self):
        return("runs on four legs")


class Bird(Animal):
    def move(self):
        return(" flies with wings")

class Fish(Animal):
    def move(self):
        return("swims with fins")
for Animals in [Dog(), Bird(), Fish()]:
        print(f"This animal {Animals.move()}")