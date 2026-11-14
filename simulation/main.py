from deck import Shoe
from strategy import BasicStrategy, HitTill17Strategy
from hand import Hand, DealerHand
from blackjack_game import BlackjackGame

if __name__ == "__main__":
   bj_game = BlackjackGame(num_decks=1, hit_on_soft_17=True, strategy="Counting")
   bj_game.deal_init_cards()
   profit = bj_game.play_turn()
   print(profit)
   bj_game.deal_init_cards()
   profit = bj_game.play_turn()
   print(profit)
   bj_game.deal_init_cards()
   profit = bj_game.play_turn()
   print(profit)
   bj_game.deal_init_cards()
   profit = bj_game.play_turn()
   print(profit)
   bj_game.deal_init_cards()
   profit = bj_game.play_turn()
   print(profit)
   bj_game.deal_init_cards()
   profit = bj_game.play_turn()
   print(profit)
   bj_game.deal_init_cards()
   profit = bj_game.play_turn()
   print(profit)
   bj_game.deal_init_cards()
   profit = bj_game.play_turn()
   print(profit)
   bj_game.deal_init_cards()
   profit = bj_game.play_turn()
   print(profit)
