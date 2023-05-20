def generate_pairings(players):
    # sort players by score
    sorted_players = sorted(players, key=lambda player: player.score)

    # generate pairings
    pairings = []
    while sorted_players:
        # take the first two players in the list
        player1 = sorted_players.pop(0)
        player2 = sorted_players.pop(0)

        # add them as a pairing
        pairings.append((player1, player2))

    return pairings
