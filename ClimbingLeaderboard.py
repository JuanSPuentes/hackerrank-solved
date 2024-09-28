""" Climbing the Leaderboard
https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem """

def climbingLeaderboard(ranked, player)-> list:
    """
    Returns the player's position on the leaderboard after each game.

    Args:
        ranked (list): Leaderboard scores in descending order.
        player (list): Player's scores.

    Returns:
        list: Player's leaderboard position after each game.
    """
    # Remove duplicates and keep scores in descending order
    ranked = sorted(set(ranked), reverse=True)
    
    result = []
    ranked_index = len(ranked) - 1

    for score in player:
        while ranked_index >= 0 and score >= ranked[ranked_index]:
            ranked_index -= 1
        result.append(ranked_index + 2)
    return result

if __name__ == '__main__':
    ranked = [100, 90, 90, 80, 75, 60]
    player = [50, 65, 77, 90, 102]
    result = climbingLeaderboard(ranked, player)
    print(result)  # [6, 5, 4, 2, 1]
