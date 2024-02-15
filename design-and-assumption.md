# Design
For storing courses, assignments, and students information, I decided to create Classes for each of them and store them in a list. This approach ensures extensibility by ensuring an easy way of adding more attributes to the classes later if necessary.

For a minimal solution, student class is not necessary but I added them because I thought it would be more maintainable if there were any changes to the requirements.

Another way, I could have stored the objects was by using dictionaries that map the object's id to the object itself. This will make data retrieval faster since we find most of the data by the id. However, it takes a lot of space and for this project in particular, I thought using a dictionary was unnecessary.


# Assumptions
1. I am assuming that for every call, the input is of a valid type and for any get/remove calls, the entry exists. With this assumption, I made sure to throw error messages when there was no valid entry for get/remove calls
 
2. I am assuming that the program that is using the CourseServiceImpl class is not going to modify any of the returned values of the methods in the course service class. This assumption is necessary because Python doesn't allow immutable fields, unlike some languages like Java. When the user modifies the returned object it can change the stored objects inside of theCourseServiceImpl. If the user could modify these objects, we can use deepcopy function to return the copy of the object instead of the object itself.

3. I am assuming the id is int from the abstract methods declaration. This led me to use incremental id generation instead of generating random UUID.


## Online resources used:
https://www.programiz.com/python-programming/docstrings
