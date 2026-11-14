from deck import Shoe
from card import Card


def test_shoe():
    shoe = Shoe(num_decks=6)

    assert len(shoe) == 312

    card = shoe.deal_card()
    assert isinstance(card, Card)
    assert len(shoe) == 311

    assert abs(shoe.penetration() - 1/312) < 1e-10

    while not shoe.need_reshuffle():
        shoe.deal_card()

    assert shoe.penetration() >= 0.75

    shoe.reset()

    assert len(shoe) == 312
    assert shoe.penetration() == 0
    assert not shoe.need_reshuffle()

    print("All shoe tests passed!")

test_shoe()


