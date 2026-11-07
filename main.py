from simulation.deck import Deck

if __name__ == "__main__":
   test_deck = Deck(num_decks=1)
   print(test_deck)
   test_deck.shuffle()
   test_deck.print_cards()
   print(len(test_deck))
   for _ in range(2):
       card = test_deck.deal_card()
       print(f"Dealt card: {card}")