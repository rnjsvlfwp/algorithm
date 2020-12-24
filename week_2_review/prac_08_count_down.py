input = 60


def count_down(time):

    if time < 0:
        return
    print(time)

    return count_down(time - 1)


count_down(input)