shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "떡볶이"]


def is_available_to_order(menus, orders):
    possible_menu = []
    for a_menus in menus:
        for a_orders in orders:
            if a_menus == a_orders:
                possible_menu.append(a_orders)
    if len(shop_orders) == len(possible_menu):
        return True
    else:
        return False


result = is_available_to_order(shop_menus, shop_orders)
print(result)
