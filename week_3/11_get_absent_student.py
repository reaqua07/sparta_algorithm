all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]

# 이중 반복해서 비교 : N^2 : 시간 복잡도 측면에서 비효율적
# for all_student in all_students:
#     for present_student in present_students:

# 해쉬 테이블 이용(딕셔너리)
def get_absent_student(all_array, present_array):
    student_dict = {}
    # 학생들을 하나하나 등록(키값 등록)
    for key in all_array:
        student_dict[key] = True

    # 앞서 저장한 딕에서 키값이 겹치면 삭제
    for key in present_array:
        del student_dict[key]

    # 삭제되고 남은 학생의 키값 반환
    for key in student_dict.keys():
        return key

    return


print(get_absent_student(all_students, present_students))