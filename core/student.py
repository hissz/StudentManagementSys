import sys
import os
BaseDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BaseDir)

from data import database
from core import orm
from data.database import session
from core import common

class Student(object):
    def __init__(self, qq):
        self.qq = qq

    def get_qq(self):
        return database.get_qq()

    def submit_task(self, lesson_name, lesson_date):
        # 提交作业
        lesson_record = common.get_lesson_record(lesson_name, self.qq)
        if lesson_record != None:
            lesson_record.task_status = 1
            session.commit()
            return True
        else:
            return False

    def get_score(self, lesson_name):
        # 查看成绩
        lesson = common.get_lesson(lesson_name)
        student = common.get_student_by_qq(self.qq)
        if lesson != None and student != None:
            lesson_record = session.query(orm.LessonRecord).filter(
                orm.LessonRecord.lesson == lesson,
                orm.LessonRecord.student == student,
            ).first()
            if lesson_record != None:
                return lesson_record.score
        else:
            return None

    def get_rank(self, lesson_name):
        # 获取排名
        lesson = common.get_lesson(lesson_name)
        student = common.get_student_by_qq(self.qq)
        if lesson != None and student != None:
            lesson_records = session.query(orm.LessonRecord).filter(
                orm.LessonRecord.lesson == lesson
            ).order_by(orm.LessonRecord.score.desc()).all()
            students = list(map(lambda record: record.student, lesson_records))
            # print(students) 输出列表
            if student in students:
                rank = students.index(student)
                return rank+1  # 索引从0开始
        return None

