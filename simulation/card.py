class Card():
    def __init__(self, rank, suit):
        RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
             'J', 'Q', 'K', 'A']
        SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        if rank not in RANKS:
            raise ValueError(f"Invalid rank: {rank}")
        if suit not in SUITS:
            raise ValueError(f"Invalid suit: {suit}")
        
        self.rank = rank
        self.suit = suit
        self.value = (
            11 if self.rank == 'A' else 10 if self.rank in ['J', 'Q', 'K'] else int(self.rank)
            )
       
    def get_rank(self):
        return self.rank

    def get_suit(self):
        return self.suit

    def get_value(self):
        return self.value

    def get_count_value(self):
        if self.rank in ['2', '3', '4', '5', '6']:
            return 1
        elif self.rank in ['7', '8', '9']:
            return 0
        else:  # 10, J, Q, K, A
            return -1

    def __str__(self):
        return f"{self.rank} of {self.suit}"