import sys
import os
BaseDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BaseDir)

from core import orm
from data.database import session


def get_student_by_qq(student_qq):
    """通过学生qq获取学生信息"""
    student = session.query(orm.Student).filter(
        orm.Student.qq == student_qq).first()
    return student


def get_lesson(lesson_name):
    """通过班级名称获取班级信息"""
    Lesson = session.query(orm.Lesson).filter(
        orm.Lesson.name == lesson_name).first()
    return Lesson


def get_lesson_record(lesson_name, student_qq):
    """通过班级名称，学生qq，日期获取班级记录"""
    lesson = get_lesson(lesson_name)
    student = get_student_by_qq(student_qq)
    if lesson != None and student != None:
        lesson_record = session.query(orm.LessonRecord).filter(
            orm.LessonRecord.Lesson == lesson,
            orm.LessonRecord.student == student,
        ).first()
        return lesson_record
    else:
        return None

