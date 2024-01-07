# class Student:
#
#     def __init__(self, name, rollnum, marks):
#         self.name = name
#         self.rollnum = rollnum
#         self.marks = marks
#
#     def print_student(self):
#         print("Name : {} and Rollnum : {} \n Marks :- {}".format(self.name, self.rollnum, self.marks.print_marks()))
#
#     class Marks:
#         def __init__(self, math, science):
#             self.math = math
#             self.science = science
#
#         def print_marks(self):
#             return "Math : {} and Science : {}".format(self.math, self.science)
#
#
# s1marks = Student.Marks(99, 98)
# s1 = Student('yashas', 41, s1marks)
# s1.print_student()
#
# s2marks = Student.Marks(75, 80)
# s2 = Student('Varshitha', 42, s2marks)
# s2.print_student()

# Super method example
class A:

    def __init__(self):
        print("From A")

    def feature(self):
        print("Feature from A")


class C:
    def __init__(self):
        print("From C")

    def feature(self):
        print("Feature from C")


class B(C, A):
    def __init__(self):
        super().__init__()
        print("From B")

    def feature(self):
        print("From feature B")

    def greet(self):
        print("Hello")

    def greet(self, name):
        print("Hello ", name)


Bobj = B()
Bobj.greet('yashas')
