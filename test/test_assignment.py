import unittest
from app.course_service_impl import CourseServiceImpl

class TestAssignment(unittest.TestCase):
  def setUp(self):
    """Perfroms initial setup before every test cases."""
    self.course_service = CourseServiceImpl()
    self.course         = self.course_service.create_course("CSCC69")
    self.student1       = self.course_service.create_student("Tom")
    self.student2       = self.course_service.create_student("Jay")

    self.course_service.enroll_student(self.course.id, self.student1.id)
    self.course_service.enroll_student(self.course.id, self.student2.id)

  def test_create_assignment_zero(self):
    """Tests creating no assignments."""
    assignments = self.course_service.get_assignments_by_course_id(self.course.id)

    self.assertEqual(assignments, [], "The course should no assignments")
    
  def test_create_assignment_single(self):
    """Tests creating one assignment."""
    assignment1 = self.course_service.create_assignment(self.course.id, "A1")
    assignments = self.course_service.get_assignments_by_course_id(self.course.id)

    self.assertEqual(len(assignments), 1, "The course should have one assignment")
    self.assertTrue(assignment1 in assignments, "An assignment is missing")

  def test_create_assignment_multiple(self):
    """Tests creating multiple assignments."""
    assignment1 = self.course_service.create_assignment(self.course.id, "A1")
    assignment2 = self.course_service.create_assignment(self.course.id, "A2")
    assignments = self.course_service.get_assignments_by_course_id(self.course.id)

    self.assertEqual(len(assignments), 2, "The course should have two assignments")
    self.assertTrue(assignment1 in assignments, "An assignment is missing")
    self.assertTrue(assignment2 in assignments, "An assignment is missing")

  def test_submit_assignment_single(self):
    """Tests submitting an assignment."""
    assignment1 = self.course_service.create_assignment(self.course.id, "A1")
    grade1      = 50

    self.course_service.submit_assignment(self.course.id, self.student1.id, assignment1.id, grade1) 

    self.assertEqual(len(assignment1.grades), 1, "The assignment should have one grade record")   
    self.assertEqual(assignment1.grades.get(self.student1.id), grade1, "The assignment grade do not match")   

  def test_submit_assignment_multiple(self):
    """Tests submitting multiple assignments."""
    assignment1 = self.course_service.create_assignment(self.course.id, "A1")
    grade1      = 50
    grade2      = 80
    
    self.course_service.submit_assignment(self.course.id, self.student1.id, assignment1.id, grade1) 
    self.course_service.submit_assignment(self.course.id, self.student2.id, assignment1.id, grade2) 

    self.assertEqual(len(assignment1.grades), 2, "The assignment should have two grade record")   
    self.assertEqual(assignment1.grades.get(self.student1.id), grade1, "The assignment grade do not match")  
    self.assertEqual(assignment1.grades.get(self.student2.id), grade2, "The assignment grade do not match")  

  def test_submit_assignment_fail_not_enrolled(self):
    """Tests submitting an assignment where the stundet is not enrolled in the course."""
    assignment1 = self.course_service.create_assignment(self.course.id, "A1")
    student     = self.course_service.create_student("Fake")
    grade1      = 50

    try:
      self.course_service.submit_assignment(self.course.id, student, assignment1.id, grade1) 
    except:
      self.assertEqual(len(assignment1.grades), 0, "The assignment should have no grade record")   

  def test_submit_assignment_fail_invalid_grade(self):
    """Tests when an submitted assingments have grade outside of 0 to 100."""
    assignment1 = self.course_service.create_assignment(self.course.id, "A1")
    grade1      = -10
    grade2      = 1000

    try:
      self.course_service.submit_assignment(self.course.id, self.student1.id, assignment1.id, grade1) 
    except:
      self.assertEqual(len(assignment1.grades), 0, "The assignment should have no grade record")   

    try:
      self.course_service.submit_assignment(self.course.id, self.student2.id, assignment1.id, grade2) 
    except:
      self.assertEqual(len(assignment1.grades), 0, "The assignment should have no grade record")

  def test_get_assignment_grade_avg_none(self):
    """Tests the assingment_grade_avg with no submission."""
    assignment1 = self.course_service.create_assignment(self.course.id, "A1")
    avg_grade   = self.course_service.get_assignment_grade_avg(self.course.id, assignment1.id)
    
    self.assertEqual(avg_grade, 0, "The average grade for the assingment do not match")

  def test_get_assignment_grade_avg(self):
    """Tests the assingment_grade_avg with some submissions."""
    assignment1 = self.course_service.create_assignment(self.course.id, "A1")
    grade1      = 50
    grade2      = 80

    self.course_service.submit_assignment(self.course.id, self.student1.id, assignment1.id, grade1) 
    self.course_service.submit_assignment(self.course.id, self.student2.id, assignment1.id, grade2) 

    avg_grade = self.course_service.get_assignment_grade_avg(self.course.id, assignment1.id)
    
    self.assertEqual(avg_grade, 65, "The average grade for the assingment do not match")

  def test_get_student_grade_avg_none(self):
    """Tests the student_grade_avg with no submission."""
    assignment1 = self.course_service.create_assignment(self.course.id, "A1")
    avg_grade   = self.course_service.get_student_grade_avg(self.course.id, assignment1.id)
    
    self.assertEqual(avg_grade, 0, "The average grade for the student do not match")

  def test_get_student_grade_avg(self):
    """Tests the student_grade_avg with some submissions."""
    assignment1 = self.course_service.create_assignment(self.course.id, "A1")
    assignment2 = self.course_service.create_assignment(self.course.id, "A2")
    grade1      = 50
    grade2      = 80
    
    self.course_service.submit_assignment(self.course.id, self.student1.id, assignment1.id, grade1) 
    self.course_service.submit_assignment(self.course.id, self.student1.id, assignment2.id, grade2) 

    avg_grade = self.course_service.get_student_grade_avg(self.course.id, self.student1.id)

    self.assertEqual(avg_grade, 65, "The average grade for the student do not match")

  def test_get_top_five_students(self):
    """Tests get_top_five_students with more than 5 students submitting the assignment."""
    assignment1 = self.course_service.create_assignment(self.course.id, "A1")
    student3    = self.course_service.create_student("s3")
    student4    = self.course_service.create_student("s4")
    student5    = self.course_service.create_student("s5")
    student6    = self.course_service.create_student("s6")
    grade1      = 50
    grade2      = 60
    grade3      = 70
    grade4      = 80
    grade5      = 90
    grade6      = 100
    
    self.course_service.enroll_student(self.course.id, student3.id)
    self.course_service.enroll_student(self.course.id, student4.id)
    self.course_service.enroll_student(self.course.id, student5.id)
    self.course_service.enroll_student(self.course.id, student6.id)

    self.course_service.submit_assignment(self.course.id, self.student1.id, assignment1.id, grade1)
    self.course_service.submit_assignment(self.course.id, self.student2.id, assignment1.id, grade2)
    self.course_service.submit_assignment(self.course.id, student3.id, assignment1.id, grade3)
    self.course_service.submit_assignment(self.course.id, student4.id, assignment1.id, grade4)
    self.course_service.submit_assignment(self.course.id, student5.id, assignment1.id, grade5)
    self.course_service.submit_assignment(self.course.id, student6.id, assignment1.id, grade6)

    top_five = self.course_service.get_top_five_students(self.course.id)

    self.assertEqual(len(top_five), 5, "There number of students in the top five list is incorrect")
    self.assertTrue(self.student2.id in top_five, "top five student don't match")
    self.assertTrue(student3.id in top_five, "top five student don't match")
    self.assertTrue(student4.id in top_five, "top five student don't match")
    self.assertTrue(student5.id in top_five, "top five student don't match")
    self.assertTrue(student6.id in top_five, "top five student don't match")

  def test_get_top_five_students_less_than_five(self):
    """Tests get_top_five_students with less than 5 students submitting the assignment."""
    assignment1 = self.course_service.create_assignment(self.course.id, "A1")
    grade1      = 50
    grade2      = 60

    self.course_service.submit_assignment(self.course.id, self.student1.id, assignment1.id, grade1)
    self.course_service.submit_assignment(self.course.id, self.student2.id, assignment1.id, grade2)

    top_five = self.course_service.get_top_five_students(self.course.id)

    self.assertEqual(len(top_five), 2, "There number of students in the top five list is incorrect")
    self.assertTrue(self.student1.id in top_five, "top five student don't match")
    self.assertTrue(self.student2.id in top_five, "top five student don't match")


if __name__ == '__main__':
  unittest.main()