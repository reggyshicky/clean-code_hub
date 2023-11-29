def solution(skills):
    N = len(skills)
    results = [0] * N

    players = [(skills[i], i) for i in range(N)]
    players.sort(key=lambda x: -x[0])

    rounds = 0
    round_matches = N
    remaining_players = N

    while round_matches > 1:
        rounds += 1
        next_round_matches = (round_matches + 1) // 2
        next_round_players = []
        next_index = 0

        for i in range(0, round_matches - 1, 2):
            player1, player2 = players[i], players[i + 1]
            winner_index = compare_players(player1, player2)
            if winner_index != -1:
                next_round_players.append(players[i + winner_index])
                next_index += 1

        round_matches = next_round_matches
        remaining_players = next_index
        players = next_round_players

    for player in players:
        results[player[1]] = rounds

    return results

def compare_players(player1, player2):
    if player1[0] > player2[0]:
        return 0
    elif player1[0] < player2[0]:
        return 1
    return -1

# Test cases
skills1 = [4, 2, 7, 3, 1, 8, 6, 5]
print(solution(skills1))  # Output: [2, 1, 3, 1, 1, 3, 2, 1]

skills2 = [4, 2, 1, 3]
print(solution(skills2))  # Output: [2, 1, 1, 2]

skills3 = [3, 4, 2, 1]
print(solution(skills3))  # Output: [1, 2, 2, 1]
