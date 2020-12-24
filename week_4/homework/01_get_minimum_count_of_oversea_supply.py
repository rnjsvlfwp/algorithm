import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    number_of_supply = 0
    dates.append(k)
    dates.insert(0, 0)
    supplies.append(0)
    supplies.insert(0, 0)
    dates_length = len(dates)

    for dates_index in range(1, dates_length):
        difference_dates = dates[dates_index] - dates[dates_index - 1]

        if stock <= 0 or stock <= difference_dates:
            stock += supplies[dates_index]
            number_of_supply += 1
            stock = stock - difference_dates
        else:
            stock = stock - difference_dates

        if dates[dates_index] == 30:
            break

    return number_of_supply


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))
