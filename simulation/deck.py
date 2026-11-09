from random import shuffle
from card import Card
class Shoe():
    """
    Can be initialized with multiple decks.
    Cards are shuffled upon initialization.
    """
    def __init__(self, num_decks=1):
        self.num_decks = num_decks
        self.cards = []
        for _ in range(num_decks):
            for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
                for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
                    self.cards.append(Card(rank, suit))
        self.shuffle()

        assert len(self.cards) == 52 * num_decks, "Incorrect number of cards in the deck"

    def shuffle(self):
        shuffle(self.cards)

    def deal_card(self):
        if len(self.cards) == 0:
            raise ValueError("No cards left in the deck")
        return self.cards.pop()

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        return f"{self.num_decks} deck(s), total cards: {len(self.cards)}"

    def print_cards(self):
        [print(card) for card in self.cards]