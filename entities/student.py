import itertools

class Student:
  """
  A class to represent a student.

  ...

  Attributes
  ----------
  id_iter: 
    used to generate incremental unique id
  id : uuid
    id of the student (must be unique)
  name : str
    name of the student
  """

  id_iter = itertools.count()

  def __init__(self, name):
    """
    Constructs all the necessary attributes for the student object.

    Parameters
    ----------
      name : str
        name of the person
    """
    self.id = next(self.id_iter)
    self.name = name