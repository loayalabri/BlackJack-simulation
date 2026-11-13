from blackjack_game import BlackjackGame
from card import Card
from hand import Hand, DealerHand
from strategy import HitTill17Strategy, BasicStrategy, HighLowStrategy


def test_play_turn():
    game = BlackjackGame(1, True, "HitTill17")
    dealer = DealerHand()
    player = Hand()
    card1 = Card("J", "Spades")
    card2 = Card("A", "Spades")
    card3 = Card("J", "Hearts")
    card4 = Card("A", "Hearts")

    dealer.add_card(card1)
    dealer.add_card(card2)
    player.add_card(card3)
    player.add_card(card4)

    game.set_dealer_hand(dealer)
    game.set_player_hand(player)
    print(game.play_turn())

if __name__ == "__main__":
    test_play_turn()

