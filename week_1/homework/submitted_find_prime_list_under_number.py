input = 150


def find_prime_list_under_number(number):
    a_num_array = [0] * number
    i_count = 0
    for a_num_index in range(number):
        a_num_array[a_num_index] = a_num_index + 1

    prime_num = []
    for a_prime_index in range(number):
        a_num = a_num_array[a_prime_index]

        if a_num == 1:
            a_num_array[a_prime_index] = 0

        elif a_num < 4:
            prime_num.append(a_num)
        else:
            for element in range(2, a_num):
                i_count += 1
                if a_num % element == 0:
                    break
            else:
                prime_num.append(a_num)


    return prime_num, i_count


result = find_prime_list_under_number(input)
print(result)
