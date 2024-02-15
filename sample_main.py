from app.course_service_impl import CourseServiceImpl

if __name__ == "__main__":
  course_service = CourseServiceImpl()

  # Start receiving requests...

  #create courses
  course1 = course_service.create_course("course1")
  course2 = course_service.create_course("course2")

  #print courses
  courses = course_service.get_courses()
  print("list of courses: {course_list}".format(course_list = list(map(lambda c: c.name, courses))))  
  print("first course added is {c1}".format(c1 = course_service.get_course_by_id(course1.id)))

  #create assignments
  assignment1 = course_service.create_assignment(course1.id, "assignment1")  
  assignment2 = course_service.create_assignment(course1.id, "assignment2")

  #print assignments for course1
  assignmens_for_course1 = course_service.get_assignments_by_course_id(course1.id)
  print("list of assignments for course1: {assignments}".format(assignments = list(map(lambda a: a.name, assignmens_for_course1))))

  #create students
  student1 = course_service.create_student("student1")  
  student2 = course_service.create_student("student2")

  #enroll students to course1
  course_service.enroll_student(course1.id, student1.id)  
  course_service.enroll_student(course1.id, student2.id)

  #print the enrolled students for course1
  print("list of students (ids) enrolled in course1: {students}".format(students = course1.students_enrolled))

  #add grades for assignment1 and assignment2
  course_service.submit_assignment(course1.id, student1.id, assignment1.id, 90)  
  course_service.submit_assignment(course1.id, student1.id, assignment2.id, 100)
  course_service.submit_assignment(course1.id, student2.id, assignment1.id, 50)  
  course_service.submit_assignment(course1.id, student2.id, assignment2.id, 60)

  #print the average grades for student1 and student2
  print("average grade for student1 in course1 is {avg}".format(avg = course_service.get_student_grade_avg(course1.id, student1.id)))
  print("average grade for student2 in course1 is {avg}".format(avg = course_service.get_student_grade_avg(course1.id, student2.id)))

  #print the assignment average grade
  print("average grade for assignment1 is: {avg}".format(avg = course_service.get_assignment_grade_avg(course1.id, assignment1.id)))  
  print("average grade for assignment1 is: {avg}".format(avg = course_service.get_assignment_grade_avg(course1.id, assignment2.id)))  

  #get top five students in the course
  print("top five students (ids) in course1 is {top_five}".format(top_five = course_service.get_top_five_students(course1.id)))