# You should write all four classes in this file

from turtle import pos


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age
        return self

    def get_name(self):
        return self.name

class Student(Person):
    def __init__(self, name, age, grade):
        Person.__init__(self, name, age)
        self.grade = grade

    def get_grade(self):
        return self.grade

    def change_grade(self, grade):
        self.grade = grade

    
class Staff(Person):
    def __init__(self, name, age, position):
        Person.__init__(self, name, age)
        self.position = position

    def get_position(self):
        return self.position

    def change_position(self, position):
        self.position = position
        return self


    
class Roster:
    def __init__(self):
        self.list = []

    def add(self,entry):
        self.list.append(entry)

    def size(self):
        return len(self.list)

    def remove(self, entry):
        self.list.remove(entry)

    def get_person(self, name):
        for entry in self.list:
            if(entry.get_name() == name):
                return entry
        return None

    def map(self, lambda_func):
        self.list = list(map(lambda_func, self.list))



