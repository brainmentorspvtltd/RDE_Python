class Student:
    name = None
    address = None
    branch = 'ME'
    college = 'RDEC'
    marks = None

    def showStudent(self):
        print(self.name)
        print(self.address)
        print(self.branch)
        print(self.college)
        print(self.marks)

student_1 = Student()
student_1.name = 'Ram'
student_1.address = 'Delhi'
student_1.marks = 78
# student_1.showStudent()

student_2 = Student()
student_2.name = 'Shyam'
student_2.address = 'UP'
student_2.marks = 81
student_2.showStudent()


