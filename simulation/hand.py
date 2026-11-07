from card import Card

class Hand:
    """
    A class representing a hand of cards in blackJack.
    """

    def __init__(self):
        self.cards = []
        self.value = 0

    def add_card(self, card: Card):
        self.cards.append(card)
        self.value += card.value

    def get_value(self):
        return self.value

    def isSoft(self):
        return any(card.rank == "A" for card in self.cards) and self.value <= 21

