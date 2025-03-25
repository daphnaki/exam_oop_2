import statistics
from typing import override
from number_array_handler import NumberArrayHandler


class CalculateStd(NumberArrayHandler):

    @override
    def handle(self, number_array):
        std_choice = input("Calculate standard deviation? (yes/no): ").strip().lower()
        if std_choice == "yes":
            if len(number_array.numbers) > 1:
                calculated_std = statistics.stdev(number_array.numbers)
                number_array.std_deviation = calculated_std
                print(f"Standard deviation: {number_array.std_deviation}")
            else:
                print("Cannot calculate standard deviation with less than 2 numbers")
        if self.next:
            self.next.handle(number_array)