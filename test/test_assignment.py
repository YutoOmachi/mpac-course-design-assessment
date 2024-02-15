import unittest
from app.course_service_impl import CourseServiceImpl

class TestAssignment(unittest.TestCase):
  def setUp(self):
    """Perfroms initial setup before every test cases."""
    self.course_service = CourseServiceImpl()
    self.course         = self.course_service.create_course("CSCC69")
    self.student_id1    = 1
    self.student_id2    = 2

    self.course_service.enroll_student(self.course.id, self.student_id1)
    self.course_service.enroll_student(self.course.id, self.student_id2)

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

    self.course_service.submit_assignment(self.course.id, self.student_id1, assignment1.id, grade1) 

    self.assertEqual(len(assignment1.grades), 1, "The assignment should have one grade record")   
    self.assertEqual(assignment1.grades.get(self.student_id1), grade1, "The assignment grade do not match")   

  def test_submit_assignment_multiple(self):
    """Tests submitting multiple assignments."""
    assignment1 = self.course_service.create_assignment(self.course.id, "A1")
    grade1      = 50
    grade2      = 80
    
    self.course_service.submit_assignment(self.course.id, self.student_id1, assignment1.id, grade1) 
    self.course_service.submit_assignment(self.course.id,self. student_id2, assignment1.id, grade2) 

    self.assertEqual(len(assignment1.grades), 2, "The assignment should have two grade record")   
    self.assertEqual(assignment1.grades.get(self.student_id1), grade1, "The assignment grade do not match")  
    self.assertEqual(assignment1.grades.get(self.student_id2), grade2, "The assignment grade do not match")  

  def test_submit_assignment_fail_not_enrolled(self):
    """Tests submitting an assignment where the stundet is not enrolled in the course."""
    assignment1   = self.course_service.create_assignment(self.course.id, "A1")
    student_id100 = 100
    grade1        = 50

    try:
      self.course_service.submit_assignment(self.course.id, student_id100, assignment1.id, grade1) 
    except:
      self.assertEqual(len(assignment1.grades), 0, "The assignment should have no grade record")   

  def test_submit_assignment_fail_invalid_grade(self):
    """Tests when an submitted assingments have grade outside of 0 to 100."""
    assignment1 = self.course_service.create_assignment(self.course.id, "A1")
    grade1      = -10
    grade2      = 1000

    try:
      self.course_service.submit_assignment(self.course.id, self.student_id1, assignment1.id, grade1) 
    except:
      self.assertEqual(len(assignment1.grades), 0, "The assignment should have no grade record")   

    try:
      self.course_service.submit_assignment(self.course.id, self.student_id2, assignment1.id, grade2) 
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

    self.course_service.submit_assignment(self.course.id, self.student_id1, assignment1.id, grade1) 
    self.course_service.submit_assignment(self.course.id, self.student_id2, assignment1.id, grade2) 

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
    
    self.course_service.submit_assignment(self.course.id, self.student_id1, assignment1.id, grade1) 
    self.course_service.submit_assignment(self.course.id, self.student_id1, assignment2.id, grade2) 

    avg_grade = self.course_service.get_student_grade_avg(self.course, self.student_id1)

    self.assertEqual(avg_grade, 65, "The average grade for the student do not match")

  def test_get_top_five_students(self):
    """Tests get_top_five_students with more than 5 students submitting the assignment."""
    assignment1 = self.course_service.create_assignment(self.course.id, "A1")
    student_id1 = 1
    student_id2 = 2
    student_id3 = 3
    student_id4 = 4
    student_id5 = 5
    student_id6 = 6
    grade1      = 50
    grade2      = 60
    grade3      = 70
    grade4      = 80
    grade5      = 90
    grade6      = 100
    
    self.course_service.submit_assignment(self.course.id, student_id1, assignment1.id, grade1)
    self.course_service.submit_assignment(self.course.id, student_id2, assignment1.id, grade2)
    self.course_service.submit_assignment(self.course.id, student_id3, assignment1.id, grade3)
    self.course_service.submit_assignment(self.course.id, student_id4, assignment1.id, grade4)
    self.course_service.submit_assignment(self.course.id, student_id5, assignment1.id, grade5)
    self.course_service.submit_assignment(self.course.id, student_id6, assignment1.id, grade6)

    top_five = self.course_service.get_top_five_students(self.course.id)

    self.assertEqual(top_five, [student_id6, student_id5, student_id4, student_id3, student_id2],
                     "top five student don't match")

  def test_get_top_five_students_less_than_five(self):
    """Tests get_top_five_students with less than 5 students submitting the assignment."""
    assignment1 = self.course_service.create_assignment(self.course.id, "A1")
    student_id1 = 1
    student_id2 = 2
    student_id3 = 3
    grade1      = 50
    grade2      = 60
    grade3      = 70
    
    self.course_service.submit_assignment(self.course.id, student_id1, assignment1.id, grade1)
    self.course_service.submit_assignment(self.course.id, student_id2, assignment1.id, grade2)
    self.course_service.submit_assignment(self.course.id, student_id3, assignment1.id, grade3)

    top_five = self.course_service.get_top_five_students(self.course.id)

    self.assertEqual(top_five,
                     [student_id3, student_id2],
                     "top five student don't match")


if __name__ == '__main__':
  unittest.main()