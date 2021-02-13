class Student:
    # Constructor
    def __init__(self,name,address,marks,branch='ME'):
        print("Constructor Called...")
        self.name = name
        self.address = address
        self.branch = branch
        self.college = 'RDEC'
        self.marks = marks
        self.data = []

    def showStudent(self):
        self.data.append([self.name, self.address, self.marks, self.branch])
        print(self.data)


student_1 = Student('Ram','Delhi',70)
student_1.showStudent()

student_2 = Student('Shyam','UP',90,'CE')
student_2.showStudent()

