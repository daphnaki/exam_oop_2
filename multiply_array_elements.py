from typing import override
from number_array_handler import NumberArrayHandler


class MultiplyArrayElements(NumberArrayHandler):

    @override
    def handle(self, number_array):
        multiply_choice = input("Multiply array elements by a number? (yes/no): ").strip().lower()
        if multiply_choice == "yes":
            factor = int(input("Enter the multiplication factor: "))
            multiplied_numbers = [num * factor for num in number_array.numbers]
            number_array.numbers = multiplied_numbers
            print(f"Array after multiplication: {number_array.numbers}")
        if self.next:
            self.next.handle(number_array)