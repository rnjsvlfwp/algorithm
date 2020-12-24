top_heights = [6, 9, 5, 7, 4]


def get_receiver_top_orders(heights):
    result = [0] * len(heights)

    while heights:
        a_height = heights.pop()
        for index in range(len(heights) - 1, -1, -1):
            if heights[index] > a_height:
                result[len(heights)] = index + 1
                break
    return result



print(get_receiver_top_orders(top_heights))
