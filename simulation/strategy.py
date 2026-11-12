


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
    def __init__(self):
        super().__init__()
        self.count = 0
        
    def update_count(self, card):
        self.count += card.get_count_value()

    def get_action(self, player_hand, dealer_hand):
        pass

    def get_bet(self):
        if self.count > 1:
            return 1.5
        else:
            return 0.5

    def reset_count(self):
        self.count = 0
        