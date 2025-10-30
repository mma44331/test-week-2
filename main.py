from core import deck,game_logic,player_io



if __name__ == "__main__":
    deck.build_standard_deck()
    deck.shuffle_by_suit(deck,swaps)

    player = {"hand": []}
    dealer = {"hand": []}

    game_logic.run_full_game(deck, player, dealer)