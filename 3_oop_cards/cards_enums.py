from enum import Enum

class CardSuit(Enum):
    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3
    SPADES = 4

    def __eq__(self, other) -> bool:
        if isinstance(other,CardSuit):
           return self.value == other.value
        return NotImplemented

    def __lt__(self, other) -> bool:
        if isinstance(other,CardSuit):
            return self.value < other.value
        return NotImplemented

    def __gt__(self, other) -> bool:
        return not self.__lt__(other)

    def __hash__(self):
        return hash(self.value)

class CardRank(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

    def __eq__(self, other) -> bool:
        if isinstance(other,CardRank):
           return self.value == other.value
        return NotImplemented

    def __lt__(self, other) -> bool:
        if isinstance(other,CardRank):
            return self.value < other.value
        return NotImplemented

    def __gt__(self, other) -> bool:
        return not self.__lt__(other)

    def __hash__(self):
        return hash(self.value)