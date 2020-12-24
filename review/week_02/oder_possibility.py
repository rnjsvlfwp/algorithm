menus = ["떡볶이", "만두", "오뎅", "사이다", "콜라"]
orders = ["오뎅", "콜라", "만두"]


def order_possibility(menu_array, order_array):
    menu_array.sort()
    # print(menu_array)

    for a_order in order_array:
        front = menu_array[0]
        rear = menu_array[-1]
        guess_index = len(menu_array) // 2
        while front <= rear:
            if a_order == menu_array[guess_index]:
                print(a_order)
                break
            elif a_order > menu_array[guess_index]:
                front = menu_array[guess_index]
                guess_index = (guess_index + len(menu_array)) // 2
            else:
                rear = menu_array[guess_index]
                guess_index = guess_index // 2
    return True


print(order_possibility(menus, orders))
