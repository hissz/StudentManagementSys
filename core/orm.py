import os

from sqlalchemy import Integer, String, Column, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

BaseDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# engine = create_engine("sqlite:///%s/data/database.db"%(BaseDir))
engine = create_engine("mysql+pymysql://root:123456@localhost/testdb?charset=utf8")

Base = declarative_base()

class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))

    def __repr__(self):
        return "%s | %s"%(self.id, self.name)


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))
    qq = Column(String(32))

    def __repr__(self):
        return "%s | %s | %s" % (self.id, self.name, self.qq)

lesson2student = Table("lesson2student", Base.metadata,
                    Column("lesson_id", Integer, ForeignKey("lessons.id")),
                    Column("student_id", Integer, ForeignKey("students.id"))
                    )

class Lesson(Base):
    __tablename__ = "lessons"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32), unique=True)

    # 增加多对多的关系表
    students = relationship("Student", secondary=lesson2student, backref="lessons")

    def __repr__(self):
        return "%s | %s" % (self.id, self.name)



class LessonRecord(Base):
    __tablename__ = "lesson_records"
    id = Column(Integer, primary_key=True, autoincrement=True)
    lesson_id = Column(Integer, ForeignKey("lessons.id"))
    stu_id = Column(Integer, ForeignKey("students.id"))
    score = Column(Integer, default=0)

    lesson = relationship("Lesson", foreign_keys=[lesson_id], backref="lesson_records")
    student = relationship("Student", foreign_keys=[stu_id], backref="lesson_records")

    def __repr__(self):
        return "%s | %s |  %s | %s"%(self.id, self.lesson.name, self.student.name, self.score)

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("数据库初始化成功")