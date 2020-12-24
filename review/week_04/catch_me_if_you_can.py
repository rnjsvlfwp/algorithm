from collections import deque

c = 11
b = 2


def catch_me(cony_loc, brown_loc):
    time_second = 0
    queue = deque()
    queue.append(brown_loc)

    while queue:

        if cony_loc == brown_loc:
            return time_second

        # 1. 코니의 거리를 계산한다.
        time_second += 1
        cony_loc += time_second

        brown_now = queue.popleft()
        for index in range(3):
            brown
        # 2. 브라운 가능한 거리를 계산하고 맞는지 확인한다.
        #   B – 1, B + 1, 2 * B


    # 3. 만약 맞으면 함수 빠져나온다.

    return


print(catch_me(c, b))  # 5가 나와야 합니다!

# queue = deque()
# queue.append(3)
# queue.append(7)
# queue.append(4)
# print(queue.popleft())
