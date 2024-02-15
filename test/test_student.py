import unittest
from app.course_service_impl import CourseServiceImpl

class Teststudent(unittest.TestCase):
  def setUp(self):
    """Perfroms initial setup before every test cases."""
    self.course_service = CourseServiceImpl()

  def test_create_student_zero(self):
    """Tests empty student list."""
    self.assertEqual(self.course_service.get_students(), [], "The students should be empty")

  def test_create_student_single(self):
    """Tests adding one student."""
    student1 = self.course_service.create_student("s1")

    self.assertEqual(len(self.course_service.get_students()), 1, "There should be one student")
    self.assertTrue(student1 in self.course_service.get_students(), "A student is missing")

  def test_create_student_multiple(self):
    """Tests adding multiple students."""
    student1 = self.course_service.create_student("s1")
    student2 = self.course_service.create_student("s2")
    student3 = self.course_service.create_student("s3")

    self.assertEqual(len(self.course_service.get_students()), 3, "There should be three students")
    self.assertTrue(student1 in self.course_service.get_students(), "A student is missing")
    self.assertTrue(student2 in self.course_service.get_students(), "A student is missing")
    self.assertTrue(student3 in self.course_service.get_students(), "A student is missing")

  def test_get_student_by_id(self):
    """Tests get_student_by_id function."""
    student1 = self.course_service.create_student("s1")

    self.assertEqual(len(self.course_service.get_students()), 1, "There should be one student")
    self.assertEqual(student1, self.course_service.get_student_by_id(student1.id), "A student could not be found using id")

  def test_get_student_by_id_fail(self):
    """Tests get_student_by_id function when the student with id does not exist"""
    student1 = self.course_service.create_student("s1")

    try:
      self.course_service.get_student_by_id(100)
      self.fail("Getting student by id that does not exist should throw an exception")
    except:
      self.assertEqual(len(self.course_service.get_students()), 1, "There should be one student")
      self.assertTrue(student1 in self.course_service.get_students(), "A student is missing")

  def test_delete_student(self):
    """Tests deleting a student."""
    student1 = self.course_service.create_student("s1")
    student2 = self.course_service.create_student("s2")

    self.course_service.delete_student(student1.id)

    self.assertEqual(len(self.course_service.get_students()), 1, "There should be one student")
    self.assertTrue(student2 in self.course_service.get_students(), "A student is missing")

  def test_delete_student_fail(self):
    """Tests deleting a student when a student does not exist."""
    student1 = self.course_service.create_student("s1")
    student2 = self.course_service.create_student("s2")

    try:
      self.course_service.delete_student(100)
      self.fail("Deleting student that does not exist should throw and exception")
    except:
      self.assertEqual(len(self.course_service.get_students()), 2, "There should be two students")
      self.assertTrue(student1 in self.course_service.get_students(), "A student is missing")
      self.assertTrue(student2 in self.course_service.get_students(), "A student is missing")