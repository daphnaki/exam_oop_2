from cards_enums import *

class Card:
    def __init__(self,suit: CardSuit,rank: CardRank,face_up = True):
        self._suit: CardSuit = suit
        self._rank : CardRank = rank
        self._face_up = face_up

    @property
    def suit(self):
        return self._suit

    @property
    def rank(self):
        return self._rank

    @property
    def face_up(self):
        return self._face_up

    def flip(self) -> bool:

        if self.face_up:
            self._face_up = False
        else:
            self._face_up = True
        return self._face_up

    def get_display_name(self) -> str:
        return f"{self._rank.name} of {self._suit.name}"

    def __eq__(self, other) -> bool:
        if isinstance(other,Card):
            return self._rank.value == other._rank.value and self._suit.value == other._suit.value


    def __lt__(self, other) -> bool:
        if isinstance(other,Card):
            if self._rank.value != other._rank.value:
                return self._rank.value < other._rank.value
            return self._suit.value < other._suit.value
        return NotImplemented


    def __gt__(self, other) -> bool:
        return not self.__lt__(other)

    def __hash__(self):
        return hash((self._suit.value,self._rank.value))

    def __str__(self):
        if not self._face_up:
            return "?"
        return self.get_display_name()

    def __repr__(self):
        return f"Card({self._rank},{self._suit},{self._face_up})"
