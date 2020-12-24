input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z"]
    max_occurrence = 0
    max_alphabet = alphabet_array[0]

    for alphabet in alphabet_array:                                                                                                               # 1.알파벳 array 크기만큼 순환, 누적: 26
        occurrence = 0                                                                                                                            # 1.입력 1번, 누적: 26*1
        for char in string:                                                                                                                       # 2.string 크기만큼 순환, 누적: 26*N
            if char == alphabet:                                                                                                                  # 2.if문 비교, 누적: 26*N(1)
                occurrence += 1                                                                                                                   # 2.연산, 누적: 26*N(2)

        if occurrence > max_occurrence:                                                                                                           # 3.if문 비교, 누적: 26*1
            max_alphabet = alphabet                                                                                                               # 3.대입 연산, 누적: 26*2
            max_occurrence = occurrence                                                                                                           # 3.대입 연산, 누적: 26*3
                                                                                                                                                  # 결과: 26(1+2*N+3) = 52N + 104

    return max_alphabet

result = find_max_occurred_alphabet(input)
print(result)