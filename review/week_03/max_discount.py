product_price = [30000, 2000, 1500000]
coupon_discount = [20, 40]


def max_discount_price(product_price_array, coupon_discount_array):
    product_price_array.sort(reverse=True)
    coupon_discount_array.sort(reverse=True)

    discounted_price = 0
    product_price_array_index = 0
    coupon_discount_array_index = 0

    while product_price_array_index < len(product_price_array) and coupon_discount_array_index < len(
            coupon_discount_array):
        discounted_price += product_price_array[product_price_array_index] * (
                    1 - coupon_discount_array[coupon_discount_array_index] / 100)
        product_price_array_index += 1
        coupon_discount_array_index += 1

    while product_price_array_index < len(product_price_array):
        discounted_price += product_price_array[product_price_array_index]
        product_price_array_index += 1

    return discounted_price


result = max_discount_price(product_price, coupon_discount)
print(result)
