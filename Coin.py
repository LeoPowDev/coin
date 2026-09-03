import random
# Imports Python's random module so we can randomly flip the coin.

# General parent class for all coins
class Coin:

    # Constructor method - runs when a Coin object is created
    def __init__(self, rare=False, clean=True, heads=True, **kwargs):

        # Loops through any extra keyword arguments passed in
        # and creates attributes from them automatically.
        for key, value in kwargs.items():
            setattr(self, key, value)

        # Stores whether the coin is rare
        self.is_rare = rare

        # Stores whether the coin is clean
        self.is_clean = clean

        # Stores whether the coin is currently heads-up
        self.heads = heads

        # If the coin is rare, increase its value by 25%
        if self.is_rare:
            self.value = self.original_value * 1.25
        else:
            # Otherwise use its normal value
            self.value = self.original_value

        # Set the coin's colour based on whether it is clean
        if self.is_clean:
            self.colour = self.clean_colour
        else:
            self.colour = self.rusty_colour

    # Makes the coin rusty
    def rust(self):
        self.colour = self.rusty_colour

    # Cleans the coin
    def clean(self):
        self.colour = self.clean_colour

    # Destructor method
    def __del__(self):
        print("Coin spent!")

    # Simulates flipping the coin
    def flip(self):
        heads_options = [True, False]
        self.heads = random.choice(heads_options)

    # String representation of the coin
    def __str__(self):
        if self.original_value >= 1.00:
            return "£{} coin".format(int(self.original_value))
        else:
            return "{}p Coin".format(int(self.original_value * 100))



# Pound coin class that inherits from Coin
class Pound(Coin):

    def __init__(self):

        data = {
            "original_value": 1.00,
            "clean_colour": "gold",
            "rusty_colour": "greenish",
            "num_edges": 1,
            "diameter": 22.5,
            "thiccness": 3.15,
            "mass": 9.5
        }

        super().__init__(**data)



class OnePence(Coin):

    def __init__(self):

        data = {
            "original_value": 0.01,
            "clean_colour": "copper",
            "rusty_colour": "brown",
            "num_edges": 1,
            "diameter": 20.3,
            "thiccness": 1.52,
            "mass": 3.56
        }

        super().__init__(**data)



class TwoPence(Coin):

    def __init__(self):

        data = {
            "original_value": 0.02,
            "clean_colour": "copper",
            "rusty_colour": "brown",
            "num_edges": 1,
            "diameter": 25.9,
            "thiccness": 2.03,
            "mass": 7.12
        }

        super().__init__(**data)



class FivePence(Coin):

    def __init__(self):

        data = {
            "original_value": 0.05,
            "clean_colour": "silver",
            "rusty_colour": "silver",
            "num_edges": 1,
            "diameter": 18.0,
            "thiccness": 1.89,
            "mass": 3.25
        }

        super().__init__(**data)

    def rust(self):
        self.colour = self.clean_colour

    def clean(self):
        self.colour = self.clean_colour



class TenPence(Coin):

    def __init__(self):

        data = {
            "original_value": 0.10,
            "clean_colour": "silver",
            "rusty_colour": "silver",
            "num_edges": 1,
            "diameter": 24.5,
            "thiccness": 1.85,
            "mass": 6.50
        }

        super().__init__(**data)



class TwentyPence(Coin):

    def __init__(self):

        data = {
            "original_value": 0.20,
            "clean_colour": "silver",
            "rusty_colour": "silver",
            "num_edges": 7,
            "diameter": 21.4,
            "thiccness": 1.7,
            "mass": 5.0
        }

        super().__init__(**data)



class FiftyPence(Coin):

    def __init__(self):

        data = {
            "original_value": 0.50,
            "clean_colour": "silver",
            "rusty_colour": "silver",
            "num_edges": 7,
            "diameter": 27.3,
            "thiccness": 1.78,
            "mass": 8.0
        }

        super().__init__(**data)



class TwoPound(Coin):

    def __init__(self):

        data = {
            "original_value": 2.00,
            "clean_colour": "gold and silver",
            "rusty_colour": "gold and silver",
            "num_edges": 1,
            "diameter": 28.4,
            "thiccness": 2.50,
            "mass": 12.0
        }

        super().__init__(**data)



# List of all the coins
coins = [
    OnePence(), TwoPence(), FivePence(), TenPence(),
    TwentyPence(), FiftyPence(), Pound(), TwoPound()
]

# Ask user what details they want to see
print("\nWhat details do you want to display for each coin?")
print("Options: colour, value, diameter, edges, mass, thiccness, all")

choice = input("Enter your choice: ").lower()

print("\n--- Coin Details ---\n")

for coin in coins:

    if choice == "colour":
        print("{} - Colour: {}".format(coin, coin.colour))

    elif choice == "value":
        print("{} - Value: {}".format(coin, coin.value))

    elif choice == "diameter":
        print("{} - Diameter(mm): {}".format(coin, coin.diameter))

    elif choice == "edges":
        print("{} - Number of edges: {}".format(coin, coin.num_edges))

    elif choice == "mass":
        print("{} - Mass(grams): {}".format(coin, coin.mass))

    elif choice == "thiccness":
        print("{} - Thiccness(mm): {}".format(coin, coin.thiccness))

    elif choice == "all":
        print("{} - Colour: {}, value:{}, diameter(mm):{}, number of edges:{}, mass(grams):{}, thiccness(mm):{}".format(
            coin,
            coin.colour,
            coin.value,
            coin.diameter,
            coin.num_edges,
            coin.mass,
            coin.thiccness
        ))

    else:
        print("Invalid choice.")
        break
