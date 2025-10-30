from core import deck,game_logic



if __name__ == "__main__":
    card_deck = deck.build_standard_deck()
    shuffel_deck = deck.shuffle_by_suit(card_deck)

    player = {"hand": []}
    dealer = {"hand": []}

    game_logic.run_full_game(shuffel_deck, player, dealer)