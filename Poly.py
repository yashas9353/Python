# Operator overLoading
class Student:

    def __init__(self, name, rollnum):
        self.name = name
        self.rollnum = rollnum

    def __add__(self, other):
        s = self.name + other.name
        r = other.rollnum + self.rollnum
        return Student(s, r)

    def __str__(self):
        return "{} {}".format(self.name, self.rollnum)


s1 = Student('Yashas', 41)
s2 = Student('Varshitha', 49)

s3 = s1 + s2

print(s1)
print(s2)
print(s3)
