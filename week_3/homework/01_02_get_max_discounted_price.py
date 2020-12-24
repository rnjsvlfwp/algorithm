shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    prices.sort(reverse=True)
    coupons.sort(reverse=True)

    prices_length = len(prices)
    coupons_length = len(coupons)
    shop_prices_index = 0
    user_coupons_index = 0
    saled_price = 0

    while shop_prices_index < prices_length and user_coupons_index < coupons_length:
        saled_price += prices[shop_prices_index] * (1 - coupons[user_coupons_index] / 100)
        shop_prices_index += 1
        user_coupons_index += 1

    while shop_prices_index < prices_length:
        saled_price += prices[shop_prices_index]
        shop_prices_index += 1

    return saled_price


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.
