from core import player_io
def calculate_hand_value(hand: list[dict]) -> int:
    count = 0
    for card in hand:
        count += int(card["rank"])
    return count



def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    cerd1 = deck.pop()
    cerd2 = deck.pop()
    player['hand'].append(cerd1)
    player['hand'].append(cerd2)
    print("This is the player's initial card sum. ",calculate_hand_value(player['hand']))
    cerd11 = deck.pop()
    cerd22= deck.pop()
    dealer['hand'].append(cerd11)
    dealer['hand'].append(cerd22)
    print("This is the amount of the dealer's initial cards. ",calculate_hand_value(dealer['hand']))




def dealer_play(deck: list[dict], dealer: dict) -> bool:
    while True:
        dealer['hand'].append(deck.pop())
        count = calculate_hand_value(dealer['hand'])
        if count < 18:
            continue
        if count > 21:
            print('You are disqualified! You are over 21.')
            return False
        break
    return True

def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    deal_two_each(deck,player,dealer)
    while player_io.ask_player_action() == "h":
        print(";;")

        player['hand'].append(deck.pop())
        count = calculate_hand_value(player['hand'])
        if count > 21:
            print('You are disqualified! You are over 21.')
            print("the dealer is winner")
            break
        continue
    else:
        if not dealer_play(deck,dealer):
            print('player is winner')
            return
        else:

            if calculate_hand_value(player['hand']) == calculate_hand_value(dealer['hand']):
                print('draw')
                return
            if calculate_hand_value(player['hand']) > calculate_hand_value(dealer['hand']):
                print('player is winner')
                return
            else:
                print('dealer is winner')
                return