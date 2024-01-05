# class Welcome:
#     Fname = str(None)
#     Lname = str(None)
#
#     def setFname(self, Fname):
#         self.Fname = Fname
#
#     def setLname(self, Lname):
#         self.Lname = Lname
#
#     def getFname(self):
#         return self.Fname
#
#     def getLname(self):
#         return self.Lname
#
#     def greet(self):
#         print("Hello Welcome to Python")
#
#
# obj1 = Welcome()
#
# obj1.setFname("Yashas")
# obj1.setLname("Raj")
#
# print("First Name:{} Last Name:{}".format(obj1.getFname(), obj1.getLname()))
#
# obj2 = Welcome()
#
# obj2.setFname("Steeven")
# obj2.setLname("Raj")
#
# print("First Name:{} Last Name:{}".format(obj2.getFname(), obj2.getLname()))

# class Welcome:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def greet(self):
#         print("Welcome {} and ur age is {}".format(self.name, self.age))
#
#     def compare(self, other):
#         if self.age == other.age:
#             return True
#         else:
#             return False
#
#
# wel = Welcome('Yashas', 21)
# wel.greet()
#
# wel1 = Welcome('Yashas', 21)
# wel1.greet()
#
#
# class Car:
#     wheel = 4
#
#     def __init__(self):
#         self.mil = 8
#         self.com = 'BMW'
#
#
# c1 = Car()
# c2 = Car()
#
# c1.mil = 10
# c1.com = 'Maruthi'
#
# Car.wheel = 5
#
# print(c1.mil, c1.com, c1.wheel)
# print(c2.mil, c2.com, c2.wheel)

class Student:
    schoolName = "New Balaji"

    def __init__(self, name, clz):
        self.name = name
        self.clz = clz

    @classmethod
    def school_name(cls):
        return cls.schoolName

    @staticmethod
    def fact(n):
        if n == 1:
            return 1
        else:
            return n * Student.fact(n - 1)

    def print_student(self):
        print("Name : {} and Class: {}".format(self.name, self.clz))


s1 = Student('Yashas', 10)
s2 = Student('Varshitha', 10)

if __name__ == '__main__':
    print("School Name : {}".format(Student.school_name()))
    s1.print_student()

    print("School Name : {}".format(Student.school_name()))
    s2.print_student()

    res = Student.fact(5)
    print(res)
