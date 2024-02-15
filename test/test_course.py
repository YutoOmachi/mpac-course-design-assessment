import unittest
from app.course_service_impl import CourseServiceImpl

class TestCourse(unittest.TestCase):
  def setUp(self):
    """Perfroms initial setup before every test cases."""
    self.course_service = CourseServiceImpl()

  def test_create_course_zero(self):
    """Tests empty courses list."""
    self.assertEqual(self.course_service.get_courses(), [], "The course should empty")

  def test_create_course_single(self):
    """Tests adding one course."""
    course1 = self.course_service.create_course("CSCC69")

    self.assertEqual(len(self.course_service.get_courses()), 1, "There should be one course")
    self.assertTrue(course1 in self.course_service.get_courses(), "A course is missing")

  def test_create_course_multiple(self):
    """Tests adding multiple courses."""
    course1 = self.course_service.create_course("CSCC69")
    course2 = self.course_service.create_course("CSCD03")
    course3 = self.course_service.create_course("CSCD58")

    self.assertEqual(len(self.course_service.get_courses()), 3, "There should be three courses")
    self.assertTrue(course1 in self.course_service.get_courses(), "A course is missing")
    self.assertTrue(course2 in self.course_service.get_courses(), "A course is missing")
    self.assertTrue(course3 in self.course_service.get_courses(), "A course is missing")

  def test_get_course_by_id(self):
    """Tests get_course_by_id function."""
    course1 = self.course_service.create_course("CSCC69")

    self.assertEqual(len(self.course_service.get_courses()), 1, "There should be one course")
    self.assertEqual(course1, self.course_service.get_course_by_id(course1.id), "A course could not be found using id")

  def test_get_course_by_id_fail(self):
    """Tests get_course_by_id function when the course with id does not exist"""
    course1 = self.course_service.create_course("CSCC69")

    try:
      self.course_service.get_course_by_id(100)

      self.fail("Getting course by id that does not exist should fail")
    except:
      self.assertEqual(len(self.course_service.get_courses()), 1, "There should be one course")
      self.assertTrue(course1 in self.course_service.get_courses(), "A course is missing")

  def test_delete_course(self):
    """Tests deleting a course."""
    course1 = self.course_service.create_course("CSCC69")
    course2 = self.course_service.create_course("CSCD03")

    self.course_service.delete_course(course1.id)

    self.assertEqual(len(self.course_service.get_courses()), 1, "There should be one course")
    self.assertTrue(course2 in self.course_service.get_courses(), "A course is missing")

  def test_delete_course_fail(self):
    """Tests deleting a course when a course does not exist."""
    course1 = self.course_service.create_course("CSCC69")
    course2 = self.course_service.create_course("CSCD03")

    try:
      self.course_service.delete_course(100)

      self.fail("Deleting course that does not exist should fail")
    except:
      self.assertEqual(len(self.course_service.get_courses()), 2, "There should be two courses")
      self.assertTrue(course1 in self.course_service.get_courses(), "A course is missing")
      self.assertTrue(course2 in self.course_service.get_courses(), "A course is missing")

  def test_enrol_student_single(self):
    """Tests enrolling a student to a course."""
    course1  = self.course_service.create_course("CSCC69")
    student1 = self.course_service.create_student("s1")

    self.course_service.enroll_student(course1.id, student1.id)

    self.assertEqual(len(course1.students_enrolled), 1, "There should be one student enrolled in the course")
    self.assertTrue(student1.id in course1.students_enrolled, "A student is missing in the course")

  def test_enrol_student_multiple(self):
    """Tests enrolling students to a course."""
    course1  = self.course_service.create_course("CSCC69")
    student1 = self.course_service.create_student("s1")
    student2 = self.course_service.create_student("s2")

    self.course_service.enroll_student(course1.id, student1.id)
    self.course_service.enroll_student(course1.id, student2.id)

    self.assertEqual(len(course1.students_enrolled), 2, "There should be two students enrolled in the course")
    self.assertTrue(student1.id in course1.students_enrolled, "A student is missing in the course")
    self.assertTrue(student2.id in course1.students_enrolled, "A student is missing in the course")

  def test_enrol_student_fail(self):
    """Tests enrolling duplicate students to a course."""
    course1  = self.course_service.create_course("CSCC69")
    student1 = self.course_service.create_student("s1")

    self.course_service.enroll_student(course1.id, student1.id)

    try:
      self.course_service.enroll_student(course1.id, student1.id)
      self.fail("Adding duplicate student to a course should throw exception")
    except:
      self.assertEqual(len(course1.students_enrolled), 1, "There should be two students enrolled in the course")
      self.assertTrue(student1.id in course1.students_enrolled, "A student is missing in the course")

  def test_dropout_student(self):
    """Tests dropping a course for a student."""
    course1                         = self.course_service.create_course("CSCC69")
    assignment1                     = self.course_service.create_assignment(course1.id, "A1")
    student1                        = self.course_service.create_student("s1")
    assignment1.grades[student1.id] = 100

    self.course_service.enroll_student(course1.id, student1.id)

    self.assertTrue(course1 in self.course_service.get_courses(), "A course is missing")

    self.course_service.dropout_student(course1.id, student1.id)

    self.assertTrue(student1.id not in course1.students_enrolled, "The student should be dropped from the course")
    self.assertEqual(assignment1.grades.get(student1.id), None, "The assignment grades should be erased")


  def test_dropout_student_fail(self):
    """Tests dropping a course for a student when the student is not enrolled in the course."""
    course1  = self.course_service.create_course("CSCC69")
    student1 = self.course_service.create_student("s1")
    try:
      self.course_service.dropout_student(course1.id, student1.id)

      self.fail("It shoudl throw exception when dropping student from a course that he/she is not enrolled in")
    except:
      self.assertEqual(len(course1.students_enrolled), 0, "There should be no students enrolled in the course")


if __name__ == '__main__':
  unittest.main()