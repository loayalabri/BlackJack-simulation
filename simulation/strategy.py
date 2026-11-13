


from abc import ABC,  abstractmethod

from overrides import override
from hand import Hand, DealerHand



class Strategy(ABC):
    """
    Abstract base class for different blackjack strategies.
    """
    @abstractmethod
    def get_action(self, player_hand: Hand, dealer_hand: DealerHand):
        """
        Get the recommended action based on the player's hand value and dealer's upcard value.
        Prerequisites: neither hand is busted, nor blackjack.
        """
        pass

    def update_count(self, card):
        pass

    def get_bet(self):
        return 1.0

    def reset_count(self):
        pass
    

class HitTill17Strategy(Strategy):
    def get_action(self, player_hand, dealer_hand):
        if player_hand.get_value() < 17 or (player_hand.isSoft() and player_hand.get_value() == 17):
            return 'Hit' 
        else:
            return 'Stand'

class BasicStrategy(Strategy):
    """
    ○ Total of 11 or less, hit.
    ○ Total of 12 and dealer upcard 4-6, stand; otherwise hit.
    ○ Total of 13-16 and dealer upcard 2-6, stand; otherwise hit.
    ○ Total of hard 17 or higher, stand.
    ○ Total of Soft 17 or less, hit.
    ○ Total of Soft 18, hit if dealer has (9, 10, Ace); stand otherwise.
    ○ Total of Soft 19 or higher, stand
    """
    def get_action(self, player_hand, dealer_hand):       
        player_value = player_hand.get_value()
        dealer_upcard = dealer_hand.get_uppercard().get_value()
        if player_hand.isSoft():
            if player_value <= 17:
                return 'Hit'
            elif player_value == 18:
                if dealer_upcard in [9, 10, 11]:
                    return 'Hit'
                else:
                    return 'Stand'
            else:
                return 'Stand'
        else:
            if player_value <= 11:
                return 'Hit'
            elif player_value == 12:
                if dealer_upcard in [4, 5, 6]:
                    return 'Stand'
                else:
                    return 'Hit'
            elif 13 <= player_value <= 16:
                if dealer_upcard in [2, 3, 4, 5, 6]:
                    return 'Stand'
                else:
                    return 'Hit'
            else:
                return 'Stand'  
        

class HighLowStrategy(BasicStrategy):
    """
    follows basic strategy while keeping a count
    (+1 for cards 2-6, -1 for cards 10-Ace, and 0 for all other cards).
    Then, bet $0.50 if the count is at or below +1 and $1.50 if the 
    count is above +1.
    """
    def __init__(self):
        super().__init__()
        self.count = 0
        
    def update_count(self, card):
        self.count += card.get_count_value()

    @override
    def get_bet(self):
        if self.count > 1:
            return 1.5
        else:
            return 0.5

    def reset_count(self):
        self.count = 0
        