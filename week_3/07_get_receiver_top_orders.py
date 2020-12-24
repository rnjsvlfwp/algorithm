top_heights = [6, 9, 5, 7, 4]


def get_receiver_top_orders(heights):
    heights_length = len(heights)
    result = [0] * heights_length

    for height_index in range(heights_length - 1):
        pop_height = heights.pop()
        heights_length = len(heights)
        for compare_index in range(heights_length - 1, 0, -1):
            if pop_height < heights[compare_index]:
                result[heights_length] = compare_index + 1
                break
    return result


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!
