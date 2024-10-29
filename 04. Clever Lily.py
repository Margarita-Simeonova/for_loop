def clever_lily(years, washmash_price, toy_price):

    money_have = 0
    toys_count = 0
    year_count = 1

    for year in range(1, years + 1):

        if year % 2 == 0:
            money_have += year * 5
            money_have -= 1

        else:
            toys_count += 1
        year_count += 1

    money_from_toys = toy_price * toys_count
    total = money_from_toys + money_have

    difference = abs(total - washmash_price)
    if total >= washmash_price:
        return f"Yes! {difference:.2f}"
    else:
        return f"No! {difference:.2f}"


years = int(input())
washmash_price = float(input())
toy_price = float(input())
result = clever_lily(years, washmash_price, toy_price)
print(result)
