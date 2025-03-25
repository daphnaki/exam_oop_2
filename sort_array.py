from typing import override
from number_array_handler import NumberArrayHandler


class SortArray(NumberArrayHandler):

    @override
    def handle(self, number_array):
        sort_choice = input("Sort the array? (yes/no): ").strip().lower()
        if sort_choice == "yes":
            sorted_numbers = sorted(number_array.numbers)
            number_array.numbers = sorted_numbers
            print(f"Sorted array: {number_array.numbers}")
        if self.next:
            self.next.handle(number_array)


