all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]


def get_absent_student(all_array, present_array):
    dictionary_array = {}

    for a_student in all_array:
        dictionary_array[a_student] = True

    for a_present_student in present_array:
        del dictionary_array[a_present_student]

    for unattending_student in dictionary_array.keys():
        return unattending_student


print(get_absent_student(all_students, present_students))
