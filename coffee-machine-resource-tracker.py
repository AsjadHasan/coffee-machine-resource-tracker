
class CoffeeMachine:
    """
    A coffee machine that tracks water, coffee, and milk resources.
    """

    def __init__(self, water, coffee, milk):
        """
        Initialize the coffee machine with available resources.
        """
        self.water = water
        self.coffee = coffee
        self.milk = milk

    def make_latte(self):
        """
        Check resources, prepare a latte, and update resources.
        """
        required_water = 200
        required_coffee = 20
        required_milk = 150

        if (
            self.water >= required_water
            and self.coffee >= required_coffee
            and self.milk >= required_milk
        ):
            self.water -= required_water
            self.coffee -= required_coffee
            self.milk -= required_milk

            print("\nLatte made!")
            print(f"Remaining - Water: {self.water}ml, "
                  f"Coffee: {self.coffee}g, "
                  f"Milk: {self.milk}ml")
        else:
            print("\nNot enough resources to make a latte.")


# Main program
print("===== Coffee Machine =====")

water = int(input("Enter available water (ml): "))
coffee = int(input("Enter available coffee (g): "))
milk = int(input("Enter available milk (ml): "))

machine = CoffeeMachine(water, coffee, milk)

while True:
    choice = input("\nDo you want to make a latte? (yes/no): ").lower()

    if choice == "yes":
        machine.make_latte()
    elif choice == "no":
        print("Thank you for using the Coffee Machine!")
        break
    else:
        print("Invalid choice! Please enter yes or no.")
