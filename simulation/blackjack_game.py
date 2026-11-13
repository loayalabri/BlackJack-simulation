from card import Card
from deck import Shoe
from hand import Hand, DealerHand
from strategy import HitTill17Strategy, BasicStrategy, HighLowStrategy
 
class BlackjackGame:
    def __init__(self, num_decks=1, hit_on_soft_17=True, strategy="Basic"):
        assert strategy in ["HitTill17", "Basic", "HighLow"], f"Invalid strategy. {strategy}"
        self.shoe = Shoe(num_decks)   
        self.player_hand = Hand()
        self.dealer_hand = DealerHand(hit_on_soft_17)
        if strategy == "HitTill17":
            self.strategy = HitTill17Strategy()
        elif strategy == "Basic":
            self.strategy = BasicStrategy()
        else:
            self.strategy = HighLowStrategy()
        self.bet = 0
        self.profit = 0


    def play_turn(self):
        self.player_hand.clear()
        self.dealer_hand.clear()
        self.bet = 10 # initial bet

        self.player_hand.add_card(self.shoe.deal_card())
        self.dealer_hand.add_card(self.shoe.deal_card())
        self.player_hand.add_card(self.shoe.deal_card())
        self.dealer_hand.add_card(self.shoe.deal_card())
        print(f"Initial Player hand: {self.player_hand}")
        if self.player_hand.is_blackjack():
            if self.dealer_hand.is_blackjack():
                self.profit == 0
                print("Tie! BlackJack!")
                print(f"PLAYER HAND: {self.player_hand}")
                print(f"DEALER HAND: {self.dealer_hand}")
                return self.profit  
            else:
                self.profit += self.bet + 1.5 * self.bet
                print("Player wins with blackjack!")
                print(f"PLAYER HAND: {self.player_hand}")
                print(f"DEALER HAND: {self.dealer_hand}")
                return self.profit
            

        while self.strategy.get_action(self.player_hand, self.dealer_hand) == 'Hit':
            self.player_hand.add_card(self.shoe.deal_card())
            self.bet += self.strategy.get_bet()
            if self.player_hand.is_busted():
                self.profit -= self.bet
                print("Player Busted!")
                print(f"PLAYER HAND: {self.player_hand}")
                print(f"DEALER HAND: {self.dealer_hand}")
                return self.profit

        while self.dealer_hand.should_hit():
            self.dealer_hand.add_card(self.shoe.deal_card())
            if self.dealer_hand.is_busted():
                self.profit += 2 * self.bet
                print("Dealer busted, player wins!")
                print(f"PLAYER HAND: {self.player_hand}")
                print(f"DEALER HAND: {self.dealer_hand}")
                return self.profit

        if self.player_hand.get_value() < self.dealer_hand.get_value():
            self.profit += 2 * self.bet
            print("Player Wins with value!")
            print(f"PLAYER HAND: {self.player_hand}")
            print(f"DEALER HAND: {self.dealer_hand}")
            return self.profit
        elif self.player_hand.get_value() == self.dealer_hand.get_value():
            self.profit == 0
            print("Tie")
            print(f"PLAYER HAND: {self.player_hand}")
            print(f"DEALER HAND: {self.dealer_hand}")
            return self.profit
        else:
            self.profit -= self.bet
            print("Player Losses with value!!")
            print(f"PLAYER HAND: {self.player_hand}")
            print(f"DEALER HAND: {self.dealer_hand}")
            return self.profit

    def set_shoe(self, shoe: Shoe):
        self.shoe = shoe

    def set_strategy(self, strategy):
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





    