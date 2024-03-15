from main import Groups, Studens, Teachers, Subjects, Teacher_subject, Grades
from faker import Faker
import random
from sqlalchemy.orm import declarative_base, sessionmaker, Mapped, mapped_column, relationship
from sqlalchemy import Column, create_engine, Integer, String, ForeignKey, select, Text, and_, desc, func, DateTime

engine = create_engine(
    'postgresql://postgres:password_bd@localhost:5432/postgres', echo=False)
DBSession = sessionmaker(bind=engine)
session = DBSession()

NUMBER_GROUPS = 3
NUMBER_STUDENTS = 30
NUMBER_SUBJECTS = 8
NUMBER_TEACHERS = 5
NUMBER_GRADES = 100

def fill():
    fake = Faker('uk_UA')
    # for table groups
    for _ in range(3):  # Цикл для створення трьох груп
        group_name = fake.company()  # Генеруємо випадкове ім'я групи
        group= Groups(group_name=group_name)
        session.add(group)
    session.commit()

    # for tabke students
    group_ids = range(1,4)
    for _ in range(50):
        group_id = random.choice(group_ids)
        # Генеруємо випадкові дані для кожного студента
        first_name = fake.first_name()
        last_name = fake.last_name()
        # Вставляємо згенеровані дані до бази даних
        student = Studens(first_name=first_name, last_name =last_name, group_id= group_id)
        session.add(student)
    session.commit()

    # for teacher
    for _ in range(5):
        first_name = fake.first_name()
        last_name = fake.last_name()
        teachers = Teachers(first_name=first_name, last_name=last_name)
        session.add(teachers)
    session.commit()

    # for subjects

    for subj in ["Математичний аналіз", "Фізика", "English",
                    "Програмування", "Інженерна графіка", "Електротехніка", "Механіка"]:
        
        subject = Subjects(subject_name=subj)
        session.add(subject)
    session.commit()

    # # for subject_teacher
    teacher_ids = range(1, 6)
    subject_ids = range(1, 8)

    for teacher_id in teacher_ids:
        subjects_taught = random.sample(subject_ids, random.randint(1, len(subject_ids)))
        for subject_id in subjects_taught:
            existing_record = session.query(Teacher_subject).filter_by(teacher_id=teacher_id, subject_id=subject_id).first()
            if existing_record is None:
                subj_teach = Teacher_subject(teacher_id=teacher_id, subject_id=subject_id)
                session.add(subj_teach)
        session.commit()

    # створюємо оцінки для учнів
    student_ids = range(1, 51)
    for student_id in student_ids:
        for subject_id in subject_ids:
            grade = random.randint(1, 12)
            grade = Grades(grade=grade, student_id=student_id,
                           subject_id=subject_id)
            session.add(grade)
    session.commit()
fill()