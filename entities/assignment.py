import itertools
from typing import Dict
from entities.student import Student

class Assignment:
  """
  A class to represent a student.

  ...

  Attributes
  ----------
  id_iter: 
    used to generate incremental unique id
  id: int
    id of the assignment (must be unique)
  course_id: int
    id of the course that this assignment is assigned in
  name: str
    name of the assignment
  grade: {int : int}
    dictionary that maps student's id to his/her grades (between 0 and 100) in the assignment 
  """

  id_iter = itertools.count()
  
  def __init__(self, course_id: int, name: str):
    """
    Constructs all the necessary attributes for the assignment object.

    Parameters
    ----------
    course_id: int
      id of the course that this assignment is assigned in
    name: str
      name of the assignment
    """
    self.id:        int            = next(self.id_iter)
    self.course_id: int            = course_id
    self.name:      str            = name
    self.grades:    Dict[int, int] = {}   