all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나"]


def present_student(all_student_array, present_student_array):
    student_dict = dict()
    for key in all_student_array:
        student_dict[key] = True
    # print(student_dict)

    for key in present_student_array:
        del student_dict[key]

    for key in student_dict.keys():
        return key

result = present_student(all_students, present_students)
print(result)
