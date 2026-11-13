from card import Card
from deck import Shoe
from hand import Hand, DealerHand
from strategy import HitTill17Strategy, BasicStrategy, HighLowStrategy
 
class BlackjackGame:
    def __init__(self, num_decks=1, hit_on_soft_17=True, strategy="Basic"):
        assert strategy in ["HitTill17", "Basic", "Counting"], f"Invalid strategy. {strategy}"
        self.num_decks = num_decks
        self.shoe = Shoe(num_decks)
        self.dealer_behaviour = "HitOnSoft17" if hit_on_soft_17 else "StandOnSoft17"
        self.strategy_name = strategy   
        self.player_hand = Hand()
        self.dealer_hand = DealerHand(hit_on_soft_17)
        if strategy == "HitTill17":
            self.strategy = HitTill17Strategy()
        elif strategy == "Basic":
            self.strategy = BasicStrategy()
        else:
            self.strategy = HighLowStrategy()
        self.bet = 0
        self.net_outcome = 0

    def deal_init_cards(self):
        self.player_hand.clear()
        self.dealer_hand.clear()
        self.bet = self.strategy.get_bet()
        self.net_outcome = 0
        
        self.deal_to_hand(self.player_hand)
        self.deal_to_hand(self.dealer_hand)
        self.deal_to_hand(self.player_hand)
        self.deal_to_hand(self.dealer_hand, visible=False)

    def deal_to_hand(self, hand: Hand, visible=True):
        card = self.shoe.deal_card()
        hand.add_card(card)
        if visible:
            self.strategy.update_count(card)


    def play_turn(self):
        if self.player_hand.is_blackjack() and self.dealer_hand.is_blackjack():
            print("Tie! BlackJack!")
            print(f"PLAYER HAND: {self.player_hand}")
            print(f"DEALER HAND: {self.dealer_hand}")
            return self.get_results("Tie")
        
        elif self.player_hand.is_blackjack():
            self.net_outcome = 1.5 * self.bet
            print("Player wins with blackjack!")
            print(f"PLAYER HAND: {self.player_hand}")
            print(f"DEALER HAND: {self.dealer_hand}")
            return self.get_results("Win")
        
        elif self.dealer_hand.is_blackjack():
            self.net_outcome = - self.bet
            print("Dealer wins with blackjack!")
            print(f"PLAYER HAND: {self.player_hand}")
            print(f"DEALER HAND: {self.dealer_hand}")
            return self.get_results("Loss")

        while self.strategy.get_action(self.player_hand, self.dealer_hand) == 'Hit':
            self.deal_to_hand(self.player_hand)
            if self.player_hand.is_busted():
                self.net_outcome =  - self.bet
                print("Player Busted!")
                print(f"PLAYER HAND: {self.player_hand}")
                print(f"DEALER HAND: {self.dealer_hand}")
                return self.get_results("Loss")
            
        self.strategy.update_count(self.dealer_hand.get_cards()[1])
        while self.dealer_hand.should_hit():
            self.deal_to_hand(self.dealer_hand)
            if self.dealer_hand.is_busted():
                self.net_outcome = self.bet
                print("Dealer busted, player wins!")
                print(f"PLAYER HAND: {self.player_hand}")
                print(f"DEALER HAND: {self.dealer_hand}")
                return self.get_results("Win")

        if self.player_hand.get_value() > self.dealer_hand.get_value():
            self.net_outcome = self.bet
            print("Player Wins with value!")
            print(f"PLAYER HAND: {self.player_hand}")
            print(f"DEALER HAND: {self.dealer_hand}")
            return self.get_results("Win")
        
        elif self.player_hand.get_value() == self.dealer_hand.get_value():
            self.net_outcome = 0
            print("Tie")
            print(f"PLAYER HAND: {self.player_hand}")
            print(f"DEALER HAND: {self.dealer_hand}")
            return self.get_results("Tie")
        
        else:
            self.net_outcome = - self.bet
            print("Player Losses with value!!")
            print(f"PLAYER HAND: {self.player_hand}")
            print(f"DEALER HAND: {self.dealer_hand}")
            return self.get_results("Loss")

    def get_results(self, outcome):
        return {
                "num_decks": self.num_decks,
                "strategy": self.strategy_name,
                "dealer_bahaviour": self. dealer_behaviour,
                "bet": self.bet,
                "net_outcome": self.net_outcome,
                "outcome": outcome
                }

    def set_shoe(self, shoe: Shoe):
        self.num_decks = shoe.num_decks
        self.shoe = shoe

    def set_strategy(self, strategy):
        assert strategy in ["HitTill17", "Basic", "Counting"], f"Invalid strategy. {strategy}"

        self.strategy_name = strategy
        if strategy == "HitTill17":
            self.strategy = HitTill17Strategy()
        elif strategy == "Basic":
            self.strategy = BasicStrategy()
        else:
            self.strategy = HighLowStrategy()

    def set_player_hand(self, hand: Hand):
        self.player_hand = hand

    def set_dealer_hand(self, hand: DealerHand):
        self.dealer_hand = hand





    