from typing import override
from number_array_handler import NumberArrayHandler


class CalculateAverage(NumberArrayHandler):

    @override
    def handle(self, number_array):
        average_choice = input("Calculate average? (yes/no): ").strip().lower()
        if average_choice == "yes":
            calculated_average = sum(number_array.numbers) / len(number_array.numbers)
            number_array.average = calculated_average
            print(f"Average of numbers: {number_array.average}")
        if self.next:
            self.next.handle(number_array)