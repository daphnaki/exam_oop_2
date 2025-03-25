import random
from sort_array import SortArray
from multiply_array_elements import MultiplyArrayElements
from calculate_average import CalculateAverage
from calculate_std import CalculateStd


class NumberArray():
    def __init__(self, size):
        # Initialize array with random numbers
        self._numbers = [random.randint(1, 100) for _ in range(size)]
        self._average = None
        self._std_deviation = None

    # Getters
    @property
    def numbers(self):
        return self._numbers

    @property
    def average(self):
        return self._average

    @property
    def std_deviation(self):
        return self._std_deviation

    # Setters
    @numbers.setter
    def numbers(self, new_numbers):
        self._numbers = new_numbers

    @average.setter
    def average(self, value):
        self._average = value

    @std_deviation.setter
    def std_deviation(self, value):
        self._std_deviation = value


def main():
    # Create the number array
    size = int(input("Enter the size of the array: "))
    number_array = NumberArray(size)

    print(f"Original array: {number_array.numbers}")

    chain_sort = SortArray()
    chain_multiply = MultiplyArrayElements()
    chain_avg = CalculateAverage()
    chain_std = CalculateStd()

    chain_sort.next = chain_multiply
    chain_multiply.next = chain_avg
    chain_avg.next = chain_std
    chain_std.next = None

    chain_sort.handle(number_array)

    print(f"Final array: {number_array.numbers}")

    # Display stored statistics
    print("\nStored Statistics:")
    if number_array.average is not None:
        print(f"Average: {number_array.average}")
    if number_array.std_deviation is not None:
        print(f"Standard Deviation: {number_array.std_deviation}")

if __name__ == "__main__":
    main()