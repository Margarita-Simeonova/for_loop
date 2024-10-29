def oscars(actor_name, academy_points, members_count):
    for _ in range(members_count):

        if academy_points > 1250.5:
            break

        member_jury_name = input()
        member_points = float(input())
        academy_points += (len(member_jury_name) * member_points) / 2

    if academy_points > 1250.5:
        return f"Congratulations, {actor_name} got a nominee for leading role with {academy_points:.1f}!"
    else:
        return f"Sorry, {actor_name} you need {1250.5 - academy_points:.1f} more!"


actor_name = input()
points = float(input())
count = int(input())
print(oscars(actor_name, points, count))
