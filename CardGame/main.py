import argparse
from math import comb

def draw_probabilities(deck_size, target_count, hand_size):
    """
    Calculate probabilities of drawing target cards from a deck.

    Returns:
        p_at_least_one (float): Probability of drawing at least one target card.
        probs (dict): Probability of drawing exactly k target cards for k = 0..min(target_count, hand_size).
    """
    total_hands = comb(deck_size, hand_size)

    # Probability of at least one target card
    p_at_least_one = 1 - comb(deck_size - target_count, hand_size) / total_hands

    # Probability distribution for exactly k target cards
    max_k = min(target_count, hand_size)
    probs = {
        k: (comb(target_count, k) * comb(deck_size - target_count, hand_size - k)) / total_hands
        for k in range(max_k + 1)
    }

    return p_at_least_one, probs


def main():
    parser = argparse.ArgumentParser(
        description="Compute probabilities of drawing target cards from a deck, optionally after discarding known non-target cards."
    )
    parser.add_argument(
        "deck_size", type=int,
        help="Total number of cards in the initial deck"
    )
    parser.add_argument(
        "target_count", type=int,
        help="Number of target cards in the deck"
    )
    parser.add_argument(
        "hand_size", type=int,
        help="Number of cards to draw in the hand"
    )
    parser.add_argument(
        "discard_count", type=int,
        help="Number of cards discarded (with no target cards seen) before drawing"
    )
    args = parser.parse_args()

    deck_size = args.deck_size
    target_count = args.target_count
    hand_size = args.hand_size
    discard_count = args.discard_count

    # Validate parameters
    if not (0 <= target_count <= deck_size and 0 < hand_size <= deck_size):
        parser.error(
            "Ensure 0 <= target_count <= deck_size and 0 < hand_size <= deck_size."
        )
    if not (0 <= discard_count <= deck_size - hand_size):
        parser.error(
            "Ensure 0 <= discard_count <= deck_size - hand_size."
        )

    # Adjust deck after discarding known non-target cards
    remaining_deck = deck_size - discard_count

    p_at_least_one, probs = draw_probabilities(remaining_deck, target_count, hand_size)

    print(f"After discarding {discard_count} non-target cards:")
    print(f"Remaining deck size: {remaining_deck}")
    print(f"Drawing {hand_size} cards...")
    print(f"Probability of at least one target card: {p_at_least_one:.4%}")
    # Skip printing the zero-target probability
    for k in sorted(probs):
        if k == 0:
            continue
        print(f"Probability of exactly {k} target cards: {probs[k]:.4%}")

if __name__ == "__main__":
    main()

