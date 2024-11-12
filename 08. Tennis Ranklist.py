W = 2000
F = 1200
SF = 720


def tennis_ranking_list(tournament_count, points):
    # count points
    points_earned = 0
    race_earned = 0

    for _ in range(tournament_count):
        ranking = input()

        if ranking == "W":
            points_earned += 2000
            race_earned += 1
        elif ranking == "F":
            points_earned += 1200
        elif ranking == "SF":
            points_earned += 720

    final_points = points_earned + points
    average_points = int(points_earned / tournament_count)
    percent = race_earned / tournament_count * 100

    return f"Final points: {final_points}\nAverage points: {average_points}\n{percent:.2f}%"


count = int(input())
points = int(input())
print(tennis_ranking_list(count, points))
