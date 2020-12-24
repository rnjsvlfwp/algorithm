shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    prices.sort(reverse=True)
    coupons.sort(reverse=True)

    prices_length = len(prices)
    coupons_length = len(coupons)
    saled_price = 0

    for index in range(prices_length):
        if index <= coupons_length - 1:
            saled_price += prices[index] * (1 - coupons[index] / 100)
        else:
            saled_price += prices[index] * (1 - 0 / 100)

    return int(saled_price)


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.
