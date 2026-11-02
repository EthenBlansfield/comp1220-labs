"""Part C tests. Your code goes in Lab7/people.py."""
from people import Person, Student, Instructor


def test_person_introduces():
    assert Person("Sam").introduce() == "Hi, I'm Sam."


def test_student_is_a_person():
    assert isinstance(Student("Kai"), Person)


def test_student_introduces():
    assert Student("Kai").introduce() == "Hi, I'm Kai, a student."


def test_student_starts_with_no_scores():
    assert Student("Kai").scores == []


def test_add_score_keeps_order():
    student = Student("Kai")
    student.add_score(90)
    student.add_score(80)
    assert student.scores == [90, 80]


def test_average():
    student = Student("Kai")
    student.add_score(90)
    student.add_score(80)
    assert student.average() == 85


def test_average_with_no_scores_is_0():
    assert Student("Kai").average() == 0


def test_instructor_is_a_person():
    assert isinstance(Instructor("Dr. Lee", "Computer Science"), Person)


def test_instructor_introduces():
    teacher = Instructor("Dr. Lee", "Computer Science")
    assert teacher.introduce() == "Hi, I'm Dr. Lee and I teach Computer Science."


def test_each_class_introduces_its_own_way():
    people = [Person("Sam"), Student("Kai"), Instructor("Dr. Lee", "Math")]
    lines = [p.introduce() for p in people]
    assert lines == ["Hi, I'm Sam.", "Hi, I'm Kai, a student.", "Hi, I'm Dr. Lee and I teach Math."]
