from sqlalchemy import Column, create_engine, Integer, String, ForeignKey, select, Text, and_, desc, func, DateTime, text
from sqlalchemy.orm import declarative_base, sessionmaker, Mapped, mapped_column, relationship


engine = create_engine(
    'postgresql://postgres:password_bd@localhost:5432/postgres', echo=False)
DBSession = sessionmaker(bind=engine)
session = DBSession()

Base = declarative_base()


class Groups(Base):
    __tablename__ = 'groups'
    group_id = Column(Integer, primary_key=True, autoincrement=True)
    group_name = Column(String(150))

class Students(Base):
    __tablename__ = 'students'
    student_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(150))
    last_name = Column(String(150))
    group_id = Column(Integer, ForeignKey(Groups.group_id))

class Teachers(Base):
    __tablename__ = 'teachers'
    teacher_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(150))
    last_name = Column(String(150))

class Subjects(Base):
    __tablename__ = 'subjects'
    subject_id = Column(Integer, primary_key=True, autoincrement=True)
    subject_name = Column(String(150))


class Teacher_subject(Base):
    __tablename__ = 'teacher_subject'
    subject_id = Column(Integer, ForeignKey(
        Subjects.subject_id), primary_key=True)
    teacher_id = Column(Integer, ForeignKey(
        Teachers.teacher_id), primary_key=True)


class Grades(Base):
    __tablename__ = 'grades'
    grade_id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer)
    subject_id = Column(Integer)
    grade = Column(Integer)
    grade_date = Column(DateTime, default=func.now())
    student_id = Column(Integer, ForeignKey(Students.student_id))
    subject_id = Column(Integer, ForeignKey(Subjects.subject_id))


Base.metadata.create_all(engine)

