


from abc import ABC,  abstractmethod
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
    

class HitTill17Strategy(Strategy):
    def get_action(self, player_hand, dealer_hand):
        if player_hand.get_value() < 17:
            return 'Hit' 
        else:
            return 'Stand'

class BasicStrategy(Strategy):
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
        
        


class HighLowStrategy(Strategy):
    def __init__(self):
        self.count = 0
        
    pass 
        