class Student:
    # Constructor
    def __init__(self):
        print("Constructor Called...")
        self.name = None
        self.address = None
        self.branch = 'ME'
        self.college = 'RDEC'
        self.marks = None
        self.data = []

    def showStudent(self):
        self.data.append([self.name, self.address, self.marks, self.branch])
        print(self.data)

student_1 = Student()
student_1.name = 'Ram'
student_1.address = 'Delhi'
student_1.marks = 78
student_1.showStudent()

student_2 = Student()
student_2.name = 'Shyam'
student_2.address = 'UP'
student_2.marks = 81
student_2.branch = 'CE'
student_2.showStudent()

