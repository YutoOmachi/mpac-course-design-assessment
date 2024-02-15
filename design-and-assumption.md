# Design
For maintaining courses, assignments and students information, I decided to create Classes for each of them and store them in a list. This approach ensures the extensibility by ensuring an easy way of adding more attributes to the classes later if necessary.

For minimal solution, student class is not necessary but I added them because I though it would be more maintainable if there would be any changes to the requirements.

Another way, I could have stored the objects was by using dictionary that maps the object's id to the object itself. This will make the retrieval of data faster since we find most of the data by the id. However, it takes a lot of space and for this project in particular, I thought it was not necessary to use dictionary.


# Assumptions
1. I am assuming that for every call, the input is of a valid type and for any get/remove calls, the entry exists. With this assumption, I made sure to throw error messages when there is no valid entry for get/remove calls
 
2. I am assuming that the program that is using CourseServiceImpl class is not going to modify any of the returned value of the methods in the course service class. This assumption is necessary because python doesn't allow immutable fields unlike some languages like Java. When user modifies the returned object it can change the stored objects inside of theCourseServiceImpl. If the user could modify these objects, we can use deepcopy function to return the copy of the object instead of the object itself.

3. I am assuming the ids are int from the abstract methods. This lead me to the use incremental id generation instead of generating random UUID.


## Online resources used:
https://www.programiz.com/python-programming/docstrings