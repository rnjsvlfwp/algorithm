input = 100


def find_prime_list_under_number(number):
    prime_list = []
    i_count = 0
    for n in range(2, number + 1):  # n: 2 ~ 10
        for i in prime_list:  # i: []/2/3/5/7
            i_count += 1
            if n % i == 0:
                break
        else:
            prime_list.append(n)

    return prime_list, i_count


result = find_prime_list_under_number(input)
print(result)
