import itertools

class Student:
  """
  A class to represent a student.

  ...

  Attributes
  ----------
  id_iter: 
    used to generate incremental unique id
  id: uuid
    id of the student (must be unique)
  name: str
    name of the student
  """

  id_iter = itertools.count()

  def __init__(self, name: str):
    """
    Constructs all the necessary attributes for the student object.

    Parameters
    ----------
      name : str
        name of the person
    """
    self.id:   int = next(self.id_iter)
    self.name: str = name