


from abc import ABC,  abstractmethod
from hand import Hand


class Strategy(ABC):
    """
    Abstract base class for different blackjack strategies.
    """
    @abstractmethod
    def get_action(self, player_hand: Hand, dealer_hand: Hand):
        """
        Get the recommended action based on the player's hand value and dealer's upcard value.
        """
        pass

    def get_bet(self, bet_amount: float):
        """
        Get the bet amount based on the minimum bet.
        """
        return bet_amount
    

class HitTill17Strategy(Strategy):
    def get_action(self, player_hand, dealer_hand):
        if player_hand.get_value() < 17:
            return 'Hit' 
        else:
            return 'Stand'

class BasicStrategy(Strategy):
    def get_action(self, player_hand, dealer_hand):
        player_value = player_hand.get_value()
        dealer_value = dealer_hand.get_value()
        if player_value <= 11:
            return 'Hit'
        if player_hand.isSoft():
            if player_value <= 17:
                return 'Hit'
            if player_value == 18:
                pass # hit if dealer has (9, 10, Ace); stand otherwise.
            if player_value >= 19:
                return 'Stand'


class HighLowStrategy(Strategy):
    pass 
        