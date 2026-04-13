# parent class person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        return f"{self.name} is {self.age} years old"
    
# child class student
class Student(Person):
    def __init__(self, name, age, student_id):
        # super() links to the parent(Person)
        super().__init__(name,age)

        self.student_id = student_id
        self.grades=[]

    def add_grade(self, grade):
        self.grades.append(grade)
    
    #overriding Parent method describe()
    def describe(self):
        return f"Student {self.name} (ID: {self.student_id}) is {self.age} years old."
    
s1 = Student("Alice", 20, "S1234")
print(s1.name)
print(s1.describe())

s1.add_grade(95)
print(s1.grades)