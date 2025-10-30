def ask_player_action() -> str:
    while True:
        char = input("Entera character only 'S' or 'H': ")
        if char == "S" or char == "H":
            break
    return char
