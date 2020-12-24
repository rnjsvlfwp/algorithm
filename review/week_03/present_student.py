all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나"]


def present_student(all_student_array, present_student_array):
    for a_present_student in present_student_array:
        if a_present_student in all_student_array:
            del all_student_array[all_student_array.index(a_present_student)]
    return all_student_array


result = present_student(all_students, present_students)
print(result)
