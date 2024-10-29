def trekking_mania(teams):
    musala = 0
    mont_blanc = 0
    kilimanjaro = 0
    k2 = 0
    everest = 0
    total_peoples_count = 0
    for _ in range(teams):
        peoples_count = int(input())
        total_peoples_count += peoples_count

        if peoples_count <= 5:
            musala += peoples_count
        elif 5 < peoples_count <= 12:
            mont_blanc += peoples_count
        elif 12 < peoples_count <= 25:
            kilimanjaro += peoples_count
        elif 25 < peoples_count <= 40:
            k2 += peoples_count
        else:
            everest += peoples_count

    return (f"{musala / total_peoples_count * 100:.2f}%\n{mont_blanc / total_peoples_count * 100:.2f}%"
            f"\n{kilimanjaro / total_peoples_count * 100:.2f}%\n"
            f"{k2 / total_peoples_count * 100:.2f}%\n{everest / total_peoples_count * 100:.2f}%")


teams_count = int(input())
print(trekking_mania(teams_count))
