from abc import ABC, abstractmethod

class NumberArrayHandler(ABC):

    def __init__(self):
        self.next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next_handler):
        self.__next = next_handler

    @abstractmethod
    def handle(self, number_array):
        pass

    # chains to create:

    # SortArray
    # MultiplyArrayElements
    # CalculateAverage
    # CalculateStd
