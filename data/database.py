import datetime
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


def init_data():
    # 初始化数据库
    student1 = orm.Student(name="Tom", qq=get_qq())
    student2 = orm.Student(name="Jack", qq=get_qq())
    student3 = orm.Student(name="Jimi", qq=get_qq())
    student4 = orm.Student(name="Ben", qq=get_qq())
    student5 = orm.Student(name="Jone", qq=get_qq())

    teacher1 = orm.Teacher(name="李老师")
    teacher2 = orm.Teacher(name="王老师")
    teacher3 = orm.Teacher(name="白老师")

    Lesson1 = orm.Lesson(name="语文")
    Lesson2 = orm.Lesson(name="数学")
    Lesson3 = orm.Lesson(name="英语")

    Lesson_record1 = orm.LessonRecord(Lesson= Lesson1, student =student1)
    Lesson_record2 = orm.LessonRecord(Lesson= Lesson1, student =student2)
    Lesson_record3 = orm.LessonRecord(Lesson= Lesson3, student =student3)

    session.add_all([student1, student2, student3, student4, student5])
    session.add_all([teacher1, teacher2, teacher3])
    session.add_all([Lesson1, Lesson2, Lesson3])
    session.add_all([Lesson_record1, Lesson_record2, Lesson_record3])

    session.commit()
    print("数据初始化成功！")