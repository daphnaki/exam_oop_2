from abc import ABC,abstractmethod
from typing import List

from card import Card


class Ideck(ABC):

    @abstractmethod
    def cards(self):
        pass

    @abstractmethod
    def shuffle(self) -> List[Card]:
        pass

    @abstractmethod
    def draw(self) -> Card:
        pass

    @abstractmethod
    def add_card(self,card:Card):
        pass

