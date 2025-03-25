class PizzaCalculator:
    def __init__(self):
        self.SLICES_PER_PIZZA = 8
        self.SLICES_PER_PERSON = 3
    def calculate_pizzas_needed(self, num_people):

        """Calculate how many pizzas are needed for a party."""
        if not isinstance(num_people, (int, float)) or num_people < 0:
            raise ValueError("Number of people must be a positive number!")

        total_slices_needed = num_people * self.SLICES_PER_PERSON

        pizzas_needed = total_slices_needed / self.SLICES_PER_PIZZA

        return round(pizzas_needed + 0.5) # round up to ensure enough pizza!

    def is_enough_pizza(self, num_pizzas, num_people):

        """Check if we have enough pizza for everyone"""

        pizzas_needed = self.calculate_pizzas_needed(num_people)
        return num_pizzas >= pizzas_needed