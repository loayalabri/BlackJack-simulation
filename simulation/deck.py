from random import shuffle
from card import Card
class Shoe():
    """
    Can be initialized with multiple decks.
    Cards are shuffled upon initialization.
    """
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    def __init__(self, num_decks=1):
        self.num_decks = num_decks
        self.cards = []
        self.reset()
        assert len(self.cards) == 52 * num_decks, "Incorrect number of cards in the deck"

    def deal_card(self):
        if len(self.cards) == 0:
            raise ValueError("No cards left in the deck")
        return self.cards.pop()

    def penetration(self):
        return 1 - len(self.cards) / (self.num_decks * 52)

    def need_reshuffle(self, threshold: float = 0.75):
        print(self.penetration())
        return self.penetration() >= threshold

    def reset(self):
        print("Reshufling ...")
        self.cards = []
        for _ in range(self.num_decks):
            for rank in self.RANKS:
                for suit in self.SUITS:
                    self.cards.append(Card(rank, suit))
        self.shuffle()

    def shuffle(self):
            shuffle(self.cards)

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        return f"{self.num_decks} deck(s), total cards: {len(self.cards)}"

    def print_cards(self):
        [print(card) for card in self.cards]