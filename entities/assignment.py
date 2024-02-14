import itertools

class Assignment:
  """
  A class to represent a student.

  ...

  Attributes
  ----------
  id_iter: 
    used to generate incremental unique id
  id : int
    id of the assignment (must be unique)
  course_id : uuid
    id of the course that this assignment is assigned in
  name : str
    name of the assignment
  scores : {uuid : int}
    dictionary that maps student's id to his/her score (between 0 and 100) in the assignment 
  """

  id_iter = itertools.count()
  
  def __init__(self, course_id, name):
    """
    Constructs all the necessary attributes for the assignment object.

    Parameters
    ----------
    course_id : int
      id of the course that this assignment is assigned in
    name : str
      name of the assignment
    """
    self.id = next(self.id_iter)
    self.course_id = course_id
    self.name = name
    self.scores = {}   