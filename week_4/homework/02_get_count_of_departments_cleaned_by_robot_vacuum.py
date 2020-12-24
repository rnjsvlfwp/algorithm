current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def get_d_when_rotate_left(d):
    return (d + 3) % 4


def get_d_when_back(d):
    return (d + 2) % 4


def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    # 1. 처음
    queue = list([[r, c, d]])
    number_of_cleaned = 1
    room_map[r][c] = 2

    while queue:

        r, c, d = queue.pop(0)
        temp_d = d

        for i in range(4):
            temp_d = get_d_when_rotate_left(temp_d)
            new_r, new_c = r + dr[temp_d], c + dc[temp_d]

            if 0 <= new_r < len(room_map) and 0 <= new_c < len(room_map[0]) and current_room_map[new_r][new_c] == 0:

                number_of_cleaned += 1
                room_map[new_r][new_c] = 2
                queue.append([new_r, new_c, temp_d])
                break

            elif i == 3:

                new_r, new_c = r + dr[get_d_when_back(d)], c + dc[get_d_when_back(d)]
                queue.append([new_r, new_c, d])

                if current_room_map[new_r][new_c] == 1:

                    return number_of_cleaned




# 57이 출력되어야 합니다!
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))
