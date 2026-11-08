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

    def get_cards(self):
        return self.cards

    def isSoft(self):
        return any(card.rank == "A" for card in self.cards) and self.value <= 21

class DealerHand(Hand):

    def __init__(self):
        super().__init__()
        self.uppercard = None

    def add_card(self, card: Card):
        super().add_card(card)
        if len(self.cards) == 1:
            self.uppercard = card

    def get_uppercard(self):
        return self.uppercard

