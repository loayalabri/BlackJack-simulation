from deck import Shoe
from strategy import BasicStrategy, HitTill17Strategy
from hand import Hand, DealerHand

if __name__ == "__main__":
   test_deck = Shoe(num_decks=1)
   player_hand = Hand()
   dealer_hand = DealerHand(hit_on_soft_17=True)
   player_hand.add_card(test_deck.deal_card())
   print(f"dealt 1 card to player, {player_hand}")
   dealer_hand.add_card(test_deck.deal_card())
   print(f"dealt 1 card to dealer, {dealer_hand}")
   player_hand.add_card(test_deck.deal_card())
   print(f"dealt 1 card to player, {player_hand}")
   dealer_hand.add_card(test_deck.deal_card())
   print(f"dealt 1 card to dealer, {dealer_hand}")
   BasicStrategy = BasicStrategy().get_action(player_hand, dealer_hand)
#    if hit_till_17_strategy == 'Hit':
#        player_hand.add_card(test_deck.deal_card())
#        print(f"dealt 1 card to player, {player_hand}")
#    Basic_strategy = BasicStrategy().get_action(player_hand, dealer_hand)
   if BasicStrategy == 'Hit':
       player_hand.add_card(test_deck.deal_card())
       print(f"dealt 1 card to player, {player_hand}")
   print(f"BasicStrategy: Player hand {player_hand}")
   print(f"BasicStrategy: Dealer hand {dealer_hand}")