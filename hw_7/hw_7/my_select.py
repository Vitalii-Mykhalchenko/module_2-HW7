from main import Groups, Students, Grades, Subjects, Teacher_subject, Teachers, session
from sqlalchemy import desc, func



def select_1():
    query = session.query(
        Students.student_id,
        Students.first_name,
        Students.last_name,
        func.avg(Grades.grade).label('average_grade')
    ).join(Grades, Students.student_id == Grades.student_id).group_by(
        Students.student_id,
        Students.first_name,
        Students.last_name
    ).order_by(func.avg(Grades.grade)).limit(5)

    results = query.all()
    for res in results:
        print(res)


def select_2():
    query = session.query(
        Students.student_id,
        Students.first_name,
        Students.last_name,
        Grades.subject_id,
        Subjects.subject_name,
        func.round(func.avg(Grades.grade), 2).label('avg_grade')
    ).join(
        Grades, Students.student_id == Grades.student_id
    ).join(
        Subjects, Grades.subject_id == Subjects.subject_id
    ).group_by(
        Students.student_id,
        Students.first_name,
        Students.last_name,
        Grades.subject_id,
        Subjects.subject_name
    ).order_by(
        func.avg(Grades.grade).desc()
    ).limit(1)

    results = query.all()
    for res in results:
        print(res)


def select_3():
    query = session.query(
        Subjects.subject_name,
        func.round(func.avg(Grades.grade), 2)
    ).join(
        Grades, Subjects.subject_id == Grades.subject_id
    ).filter(
        Subjects.subject_name == "Механіка"
    ).group_by(
        Subjects.subject_name,
    )

    results = query.all()
    for res in results:
        print(res)


def select_4():
    query = session.query(
        Grades.subject_id,
        Subjects.subject_name,
        func.round(func.avg(Grades.grade), 2)
    ).join(
        Subjects, Grades.subject_id == Subjects.subject_id
    ).group_by(
        Grades.subject_id,
        Subjects.subject_name
    )

    results = query.all()
    for res in results:
        print(res)


def select_5():
    query = session.query(
        Teachers.first_name,
        Teachers.last_name,
        Subjects.subject_name
    ).join(
        Teacher_subject, Teachers.teacher_id == Teacher_subject.teacher_id
    ).join(
        Subjects, Subjects.subject_id == Teacher_subject.subject_id
    ).group_by(
        Teachers.first_name,
        Teachers.last_name,
        Subjects.subject_name
    )

    results = query.all()
    for res in results:
        print(res)


def select_6():
    query = session.query(
        Students.student_id,
        Students.first_name,
        Students.last_name,

        func.round(func.avg(Groups.group_id),)
    ).join(
        Groups, Students.group_id == Groups.group_id
    ).group_by(
        Students.student_id,
        Students.first_name,
        Students.last_name
    ).order_by(
        func.avg(Groups.group_id).desc()
    )

    results = query.all()
    for res in results:
        print(res)


def select_7():
    query = session.query(
        Grades.student_id,
        Students.first_name,
        Students.last_name,
        Groups.group_name,
        Grades.grade,
        Subjects.subject_name
    ).join(
        Students, Students.student_id == Grades.student_id
    ).join(
        Groups, Groups.group_id == Students.group_id
    ).join(
        Subjects, Subjects.subject_id == Grades.subject_id
    )

    results = query.all()
    for res in results:
        print(res)


def select_8():
    query = session.query(
        Teachers.first_name,
        Teachers.last_name,
        Subjects.subject_name,
        func.round(func.avg(Grades.grade), 1)
    ).join(
        Teacher_subject, Teachers.teacher_id == Teacher_subject.teacher_id
    ).join(
        Subjects, Teacher_subject.subject_id == Subjects.subject_id
    ).join(
        Grades, Subjects.subject_id == Grades.subject_id
    ).group_by(
        Teachers.first_name,
        Teachers.last_name,
        Subjects.subject_name
    )
    results = query.all()
    for res in results:
        print(res)


def select_9():
    query = session.query(
        Students.student_id,
        Students.first_name,
        Students.last_name,
        Subjects.subject_name
    ).join(
        Grades, Students.student_id == Grades.student_id
    ).join(
        Subjects, Subjects.subject_id == Grades.subject_id
    )
    results = query.all()
    for res in results:
        print(res)


def select_10():
    subquery = session.query(
        func.max(Grades.grade_id).label('max_grade_id')
    ).group_by(
        Grades.subject_id, Grades.student_id
    ).subquery()

    query = session.query(
        Subjects.subject_name,
        Students.student_id,
        Students.first_name,
        Students.last_name,
        Teachers.teacher_id,
        Teachers.first_name,
        Teachers.last_name
    ).join(
        Teacher_subject, Subjects.subject_id == Teacher_subject.subject_id
    ).join(
        Teachers, Teacher_subject.teacher_id == Teachers.teacher_id
    ).join(
        Grades, Subjects.subject_id == Grades.subject_id
    ).join(
        Students, Grades.student_id == Students.student_id
    ).filter(
        Students.first_name == 'Роман',
        Students.last_name == 'Штокало',
        Teachers.first_name == 'Трохим',
        Teachers.last_name == 'Бандурка',
        Grades.grade_id == subquery.c.max_grade_id
    )
    results = query.all()
    for res in results:
        print(res)


if __name__ == '__main__':
    print('------------ Select 1 ------------')
    select_1()

    print('------------ Select 2 ------------')
    select_2()

    print('------------ Select 3 ------------')
    select_3()

    print('------------ Select 4 ------------')
    select_4()

    print('------------ Select 5 ------------')
    select_5()

    print('------------ Select 6 ------------')
    select_6()

    print('------------ Select 7 ------------')
    select_7()

    print('------------ Select 8 ------------')
    select_8()

    print('------------ Select 9 ------------')
    select_9()

    print('------------ Select 10 ------------')
    select_10()
