import csv
from blackjack_game import BlackjackGame




def generate_save_data(path: str, seed=None, reps=100, hands=100):
    strategies = ["HitTill17", "Basic", "Counting"]
    num_decks = [1, 6]
    dealer_behaviour = [True, False]
    with open(path, "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames= ["replicate",
                         "hand",
                         "num_decks",
                         "strategy",
                         "dealer_behaviour",
                         "bet", 
                         "round_outcome",
                         "cumilative_outcome",
                         "outcome"
                    ]
        )
        writer.writeheader()

        for replicate in range(1, reps + 1):
            for strat in strategies:
                for num_deck in num_decks:
                    for behave in dealer_behaviour:
                        game = BlackjackGame(num_decks=num_deck, hit_on_soft_17=behave, strategy_name=strat, seed=seed)
                        for hand in range(1, hands + 1):     
                            game.deal_init_cards()
                            result = game.play_turn()
                            result["replicate"] = replicate
                            result["hand"] = hand
                            writer.writerow(result)


