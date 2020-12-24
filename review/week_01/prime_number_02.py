target_number = 120


def find_prime_number(number):
    prime_number = [2]
    for a_number in range(3, number + 1):
        for a_num in prime_number:
            if a_number % a_num == 0 and a_num * a_num <= a_number:
                break
        else:
            prime_number.append(a_number)

    return prime_number


result = find_prime_number(target_number)
print(result)
