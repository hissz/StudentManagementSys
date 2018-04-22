import sys
import os
BaseDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BaseDir)

from data import database
from core import orm
from data.database import session
from core import common

class Teacher(object):
    def __init__(self, name):
        self.name = name

    def add_lesson(self, lesson_name):
        # 增加课程 成功True， 失败False
        try:
            lesson = orm.Lesson(name=lesson_name)
            session.add(lesson)
            session.commit()
            return True
        except:
            return False

    def add_student_to_lesson(self, student_qq, lesson_name):
        # 把学生增加到课程
        try:
            student =common.get_student_by_qq(student_qq)
            lesson = common.get_lesson(lesson_name)
            lesson.students.append(student)
            session.commit()
        except:
            return False
        return True

    def add_lesson_record(self, lesson_name):
        # 增加课程记录
        try:
            lesson=common.get_lesson(lesson_name)
            students = lesson.students
            records = []
            for student in students:
                lesson_record =common.get_lesson_record(
                    lesson_name,student.qq)

                if lesson_record == None:  # 记录为空再添加
                    lesson_record = orm.LessonRecord(
                        lesson=lesson, student=student,)
                    records.append(lesson_record)
            session.add_all(records)
            session.commit()
        except:
            return False
        return True

    def modify_score(self, lesson_name, student_qq, date, score):
        # 修改成绩
        lesson_record = common.get_lesson_record(lesson_name, student_qq)
        if lesson_record != None:
            lesson_record.score = score
            session.commit()
            return True
        else:
            return False