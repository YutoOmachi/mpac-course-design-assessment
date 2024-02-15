import math
from typing import List
from app.course_service import CourseService
from entities.assignment import Assignment
from entities.course import Course
from entities.student import Student

class CourseServiceImpl(CourseService):
  """
  A class to implement the CourseService interface according to the requirements.

  ...

  Attributes
  ----------
  assignments: [Assignment]
    holds the list of assignments
  assignments: [Course]
    holds the list of courses
  assignments: [Student]
    holds the list of students
  """
  def __init__(self):
    """
    Constructs all the necessary attributes for the assignment object.
    """
    self.assignments: List[Assignment] = []
    self.courses:     List[Course]     = []
    self.students:    List[Student]    = [] 

  def get_courses(self) -> List[Course]:
    """
    Returns a list of all courses.
    """
    return self.courses

  def get_course_by_id(self, course_id: int) -> Course:
    """
    Returns a course by its id.
    """
    for course in self.courses:
      if course.id == course_id:
        return course
      
    raise ValueError("There is no course with id {id}".format(id = course_id))

  def create_course(self, course_name: str):
    """
    Creates a new course.
    """
    new_course = Course(course_name)

    self.courses.append(new_course)

    return new_course

  def delete_course(self, course_id: int):
    """
    Deletes a course by its id.
    """
    course_to_remove = self.get_course_by_id(course_id)

    self.courses.remove(course_to_remove)

    for assignment in self.assignments:
      if assignment.course_id == course_id:
        self.assignments.remove(assignment)

    return course_to_remove

  def create_assignment(self, course_id: int, assignment_name: str) -> Assignment:
    """
    Creates a new assignment for a course.
    """
    new_assignment = Assignment(course_id, assignment_name)

    self.assignments.append(new_assignment)

    return new_assignment

  def get_assignments_by_course_id(self, course_id: int) -> List[Assignment]:
    """
    Find assignments by its course_id
    """
    return list(filter(lambda assignment: assignment.course_id == course_id, self.assignments))

  def enroll_student(self, course_id: int, student_id: int):
    """
    Enrolls a student in a course.
    """
    student = self.get_student_by_id(student_id)
    course  = self.get_course_by_id(course_id)

    if student.id in course.students_enrolled:
      raise ValueError("This student with id {student_id} already joined the course with id {cource_id}"
                       .format(student_id = student_id, course_id = course_id))
    
    course.students_enrolled.append(student_id)

  def dropout_student(self, course_id: int, student_id: int):
    """
    Drops a student from a course.
    """
    student = self.get_student_by_id(student_id)
    course  = self.get_course_by_id(course_id)

    if student.id not in course.students_enrolled:
      raise ValueError("Student with id = {id} is not taking this course".format(id = student_id))
      
    course.students_enrolled.remove(student_id)

    for assignment in self.assignments:
      if assignment.course_id == course_id and student_id in assignment.grades:
        assignment.grades.pop(student_id)

  def submit_assignment(self, course_id: int, student_id: int, assignment_id: int, grade: int):
    """
    Submits an assignment for a student. A grade of an assignment will be an integer between 0 and 100 inclusive.
    """
    if (grade < 0 or grade > 100): 
      raise ValueError("Grade must be between 0 to 100")
    
    course = self.get_course_by_id(course_id)

    if student_id not in course.students_enrolled:
      raise ValueError("Student with id = {id} is not taking this course".format(id = student_id))
    
    for assignment in self.assignments:
      if assignment.id == assignment_id and assignment.course_id == course_id:
        assignment.grades[student_id] = grade
        return
  
    raise ValueError("Assignment with id = {id}, course_id = {course_id} does not exist"
                     .format(id = assignment_id, course_id = course_id))

  def get_assignment_grade_avg(self, course_id: int, assignment_id: int) -> int:
    """
    Returns the average grade for an assignment. Floors the result to the nearest integer.
    """
    total_grade = 0

    for assignment in self.assignments:
      if assignment.id == assignment_id and assignment.course_id == course_id:
        if len(assignment.grades) == 0:
          return 0
        for student_id in assignment.grades:
          total_grade += assignment.grades.get(student_id)
        return total_grade/len(assignment.grades)
      
    raise ValueError("Assignment with id = {id}, course_id = {course_id} does not exist"
                     .format(id = assignment_id, course_id = course_id))
  
  def get_student_grade_avg(self, course_id: int, student_id: int) -> int:
    """
    Returns the average grade for a student in a course. Floors the result to the nearest integer.
    """
    total_grade = 0
    count       = 0

    course = self.get_course_by_id(course_id)

    for assignment in self.assignments:
      if assignment.course_id == course.id and student_id in assignment.grades:
        total_grade += assignment.grades.get(student_id)
        count += 1
  
    if count == 0:
      return 0
    
    return math.floor(total_grade/count)

  def get_top_five_students(self, course_id: int) -> List[int]:
    """
    Returns the IDs of the top 5 students in a course based on their average grades of all assignments.
    """
    students_enrolled = self.get_course_by_id(course_id).students_enrolled

    if len(students_enrolled) < 5:
      return students_enrolled[:]

    students_enrolled.sort(reverse=True)

    return students_enrolled[:5]
  
  def get_students(self) -> List[Student]:
    """
    Returns a list of all students.
    """
    return self.students

  def get_student_by_id(self, student_id: int) -> Student:
    """
    Returns a course by its id.
    """
    for student in self.students:
      if student.id == student_id:
        return student
      
    raise ValueError("There is no student with id {id}".format(id = student_id))

  def create_student(self, student_name: int) -> Course:
    """
    Creates a new student.
    """
    new_student = Student(student_name)

    self.students.append(new_student)

    return new_student

  def delete_student(self, student_id: int) -> Course:
    """
    Deletes a course by its id.
    """
    student = self.get_student_by_id(student_id)

    self.students.remove(student)