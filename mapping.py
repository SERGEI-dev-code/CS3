class Course:
    def __init__(self, courseId, title):
        self.courseId = courseId
        self.title = title
        self.students = []

    def getStudents(self):
        return self.students

    def addStudents(self, student):
        self.students.append(student)


class Student:
    def __init__(self, studentId, name):
        self.studentId = studentId
        self.name = name

    def enrollInCourse(self, course):
        course.addStudents(self)
