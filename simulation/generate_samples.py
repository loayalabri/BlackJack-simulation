import csv
import itertools
import random
from blackjack_game import BlackjackGame


def generate_save_data(path: str, seed=None, reps=100, hands=100):
    strategies = ["HitTill17", "Basic", "Counting"]
    num_decks = [1, 6]
    dealer_behaviour = [True, False]
    
    # Build all treatment runs: 100 reps x 3 strategies x 2 deck sizes x 2 dealer rules = 1200 runs
    runs = list(itertools.product(range(1, reps + 1), strategies, num_decks, dealer_behaviour))
    
    # Randomize execution order reproducibly
    rng = random.Random(seed)
    rng.shuffle(runs)
    
    with open(path, "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "replicate",
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

        for run_id, (replicate, strat, num_deck, behave) in enumerate(runs):
            run_seed = seed + run_id if seed is not None else None
            game = BlackjackGame(
                num_decks=num_deck,
                hit_on_soft_17=behave,
                strategy_name=strat,
                seed=run_seed
            )
            for hand in range(1, hands + 1):
                game.deal_init_cards()
                result = game.play_turn()
                result["replicate"] = replicate
                result["hand"] = hand
                writer.writerow(result)



