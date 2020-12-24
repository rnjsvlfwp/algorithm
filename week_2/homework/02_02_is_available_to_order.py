shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    menus.sort()
    for order in orders:
        if not binary(menus, order):
            return False
    return True


def binary(array, target):
    current_min = 0
    current_max = len(array) - 1
    current_mid = (current_min + current_max) // 2

    while current_min <= current_max:
        if array[current_mid] == target:
            return True
        elif array[current_mid] < target:
            current_min = current_mid + 1
        else:
            current_max = current_mid - 1
        current_mid = (current_min + current_max) // 2
    return False


result = is_available_to_order(shop_menus, shop_orders)
print(result)
