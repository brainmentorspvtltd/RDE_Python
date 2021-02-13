class Student:
    # Constructor
    def __init__(self,name):
        print("Constructor Called...")
        self.name = name

    def showStudent(self):
        print(self.name)

class Student_V2(Student):
    def __init__(self,name):
        super().__init__(name)
        self.address = 'Delhi'
    # overriding
    def showStudent(self):
        print(self.name, self.address)

obj_1 = Student_V2('Ram')
obj_1.showStudent()