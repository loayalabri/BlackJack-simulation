class Card():
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = (
            int(self.rank) if self.rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10']
            else 10 if self.rank in ['J', 'Q', 'K'] else 11)
        assert self.rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'], "Invalid rank"
        assert self.suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades'], "Invalid suit"

    def get_rank(self):
        return self.rank

    def get_suit(self):
        return self.suit

    def get_value(self):
        return self.value

    def __str__(self):
        return f"{self.rank} of {self.suit}"