from random import randint
from operator import index


def build_standard_deck() -> list[dict]:
    card_deck = []
    suite_list = ["H", "C", "D", "S"]
    rank_list = ["J","Q","K","A"]
    for suite in suite_list:
        for i in range(2, 11):
            card_dict = {}
            card_dict['rank'] = str(i)
            card_dict['suite'] = suite
            card_deck.append(card_dict)
        for item in rank_list:
            card_dict = {}
            card_dict['suite'] = suite
            if item == "A":
                card_dict['rank'] = "1"
            else:
                card_dict['rank'] = "10"
            card_deck.append(card_dict)
    return card_deck

def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    while swaps > 0:
        swaps -= 1
        index1 = randint(0,51)
        while True:
            index2 = randint(0,51)
            if index2 == index1:
                continue
            if deck[index2]['suite'] == "H":
                if index2 % 5 !=0:
                    continue
            if deck[index2]['suite'] == "C":
                if index2 % 3 != 0:
                    continue
            if deck[index2]['suite'] == "D":
                if index2 % 2 != 0:
                    continue
            if deck[index2]['suite'] == "S":
                if index2 % 7 != 0:
                    continue
            break
        deck[index1],deck[index2] = deck[index2],deck[index1]
    return deck



