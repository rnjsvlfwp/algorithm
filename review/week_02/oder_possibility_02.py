menus = ["떡볶이", "만두", "오뎅", "사이다", "콜라"]
orders = ["오뎅", "콜라", "만두"]


def order_possibility(menu_array, order_array):
    menus_set = set(menu_array)

    for a_order in order_array:
        if a_order not in menu_array:
            return False
    else:
        return True


print(order_possibility(menus, orders))
