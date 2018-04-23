import sys
import os
BaseDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BaseDir)

from core.student import Student
from core.teacher import Teacher

def student_view():
    """学生视图"""
    qq = input("请输入学生qq号：")
    student = Student(qq)
    while True:
        choice = input("1.交作业，2.查成绩，3.看排名,4返回")
        if choice == "1":
            lesson_name = input("课程名称:")
            ret = student.submit_task(lesson_name)
            print(ret)
        elif choice =="2":
            lesson_name = input("课程名称:")
            ret=student.get_score(lesson_name)
            print(ret)
        elif choice == "3":
            lesson_name = input("课程名称:")
            ret = student.get_rank(lesson_name)
            print(ret)
        elif choice == "4":
            main()
        else:
            print("请输入正确的选项")

def teacher_view():
    """教师视图"""
    teacher_name = input("输入老师姓名:")
    teacher = Teacher(teacher_name)
    while True:
        choice = input("1.增加课程，2.增加上课记录，3.把学生增加到班级，4.修改学生成绩，5.返回")
        if choice == "1":
            lesson_name = input("课程名称:")
            ret = teacher.add_lesson(lesson_name)
            print(ret)
        elif choice == "2":
            lesson_name = input("课程名称:")
            ret = teacher.add_lesson_record(lesson_name)
            print(ret)
        elif choice == "3":
            qq = input("请输入学生qq号：")
            lesson_name = input("课程名称:")
            ret = teacher.add_student_to_lesson(qq, lesson_name)
            print(ret)
        elif choice=="4":
            qq = input("请输入学生qq号：")
            lesson_name = input("课程名称:")
            score = input("成绩:")
            ret = teacher.modify_score(lesson_name, qq, score)
            print(ret)
        elif choice=="5":
            main()
        else:
            print("请输入正确的选项")

def main():
    role = input("选择角色：1.教师，2.学生：")
    if role == "1":
        teacher_view()
    elif role == "2":
        student_view()
    else:
        print("输入错误，退出程序")

if __name__ == "__main__":
    main()

