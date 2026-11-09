from typing import override

from card import Card

class Hand:
    """
    A class representing a hand of cards in blackJack.
    """

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card: Card):
        self.cards.append(card)
        if card.rank == "A":
            self.aces += 1
        self.value += card.get_value()
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1


    def get_value(self):
        return self.value

    def get_cards(self):
        return self.cards.copy()

    def isSoft(self):
        return self.aces > 0

    def is_busted(self):
        return self.value > 21

    def is_blackjack(self):
        return len(self.cards) == 2 and self.value == 21

    def clear(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def __str__(self):
        return f"Hand value: {self.value}, Cards: {[str(card) for card in self.cards]}"

    

class DealerHand(Hand):
    def __init__(self, hit_on_soft_17=True):
        super().__init__()
        self.hit_on_soft_17 = hit_on_soft_17

    @override
    def add_card(self, card: Card):
        super().add_card(card)
        if len(self.cards) == 1:
            self.uppercard = card

    def get_uppercard(self):
        return self.cards[0] if self.cards else None

    def should_hit(self):
        total_value = self.get_value()
        if total_value < 17:
            return True
        elif total_value == 17 and self.isSoft():
            return self.hit_on_soft_17
        return False
    

    
