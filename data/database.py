import random
import sys
import os
import string

BaseDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BaseDir)

from sqlalchemy.orm import sessionmaker
from core import orm


Session = sessionmaker(orm.engine)
session = Session()

def get_qq():
    nums = string.digits  # 0123456789
    qq = "".join(random.sample(nums, 6))  # 获取6位QQ号
    return qq


def database():
    # 初始化数据库
    student1 = orm.Student(name="Tom", qq=get_qq())
    student2 = orm.Student(name="Jack", qq=get_qq())
    student3 = orm.Student(name="Jimi", qq=get_qq())
    student4 = orm.Student(name="Ben", qq=get_qq())
    student5 = orm.Student(name="Jone", qq=get_qq())

    teacher1 = orm.Teacher(name="李老师")
    teacher2 = orm.Teacher(name="王老师")
    teacher3 = orm.Teacher(name="白老师")

    lesson1 = orm.Lesson(name="语文")
    lesson2 = orm.Lesson(name="数学")
    lesson3 = orm.Lesson(name="英语")

    lesson_record1 = orm.LessonRecord(lesson= lesson1, student =student1)
    lesson_record2 = orm.LessonRecord(lesson= lesson2, student =student2)
    lesson_record3 = orm.LessonRecord(lesson= lesson3, student =student3)

    session.add_all([student1, student2, student3, student4, student5])
    session.add_all([teacher1, teacher2, teacher3])
    session.add_all([lesson1, lesson2, lesson3])
    session.add_all([lesson_record1, lesson_record2, lesson_record3])

    session.commit()
    print("数据初始化成功！")

if __name__ == "__main__":
    database()
    session.close()