import itertools

class Course:
  """
  A class to represent a course.

  ...

  Attributes
  ----------
  id_iter: 
    used to generate incremental unique id
  id : int
    id of the course (must be unique)
  name : str
    name of the course
  students_enrolled : [uuid]
    list of student that is taking the course currently
  """
  
  id_iter = itertools.count()

  def __init__(self, name):
    """
    Constructs all the necessary attributes for the course object.

    Parameters
    ----------
    name : str
      name of the assignment
    """
    self.id = next(self.id_iter)
    self.name = name
    self.students_enrolled = []  
