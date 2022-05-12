
import os
os.system("cls" if os.name == "nt" else "clear")

# def print_type(data):
#     for i in data:
#         print(i , type(i))



# test = [1, 2, "Ömer", [3, 4, 5], (6, 7, 8), {9, 10, 11}, True]

# print_type(test)


# class Person:
#     name = "Ömer"
#     age = 28


# person1 = Person()
# person2 = Person()

# print(person1.name)
# print(person2.name)

# Person.job = "Student"

# print(person1.job)

##class attributes vs instance attributes

# person1.location = "Turkey"

# print(person1.location)

# person2.name = "Bahar"

# print(person1.name)

# class Person:
#     name = "Ömer"
#     age = 28

#     def test(self):
#         print("test")
    
#     def set_details(self, name, age):
#         self.name = name
#         self.age = age
#     def get_details(self):
#         print(self.name, self.age)

# person1 = Person()
# # person1.test()
# person1.get_details()
# person1.set_details("Aoran", 37)
# person1.get_details()


# class Person:
#     company = "Clarusway"

#     def set_details(self, name, age):
#         self.name = name
#         self.age = age
#     def get_details(self):
#         print(self.name, self.age)  

#     @staticmethod

#     def salute():
#         print("Hi there!")


# person1 = Person()

# person1.salute()


## SPECİAL METHODS

# class Person:
#     company = "Clarusway"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def get_details(self):
#         print(self.name, self.age)

#     def __str__(self):
#         return f"{self.name} {self.age}"


# person1 = Person("Ömer", 28)
# person1.get_details()

# print(person1)


#ENCAPSULATİON AND OBSTRACTİON

# class Person:
#     company = "Clarusway"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self._id = 5000
#         self.__id2 = 4000

#     def get_details(self):
#         print(self.name, self.age)

#     def __str__(self):
#         return f"{self.name} {self.age}"

# person1 = Person("Ömer", 28)

# print(person1._Person__id2)


#INHERITANCE AND POLYMORPHISM


# class Person:
#     company = "Clarusway"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self._id = 5000
#         self.__id2 = 4000

#     def get_details(self):
#         print(self.name, self.age)

#     def __str__(self):
#         return f"{self.name} {self.age}"

# class Lang:
#     def __init__(self, Langs):
#         self.langs = Langs

#     def display_langs(self):
#         print(self.langs)


# class Employee(Person, Lang):
#     def __init__(self, name, age, path, langs):
#         # self.name = name
#         # self.age = age
#         super().__init__(name, age)
#         self.path = path
#         Lang.__init__(self, langs)
        
#     # OverWrite

#     def get_details(self):
#         print(f"{self.name} {self.age} {self.path} {self.langs}")
        

# emp1 = Employee("Ömer", 28, "Full Stack", ["Python", "Java Script"])
# emp1.get_details()


class Person():
    def __init__(self, age, name, surname):
        self.age = age
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"My name is {self.name} {self.surname} and I am {self.age} years old."

    def get_details(self):
        print(self.name, self.surname, self.age)


class School():
    def __init__(self, school):
        self.school = school

class Student(Person, School):
    def __init__(self, age, name, surname, path, school):
        super().__init__(age, name, surname)
        School.__init__(self, school)
        self.school = school
        self.path = path

    def __str__(self):
        return f"My name is {self.name} {self.surname}.I am {self.age} years old.My path is {self.path}.And I am stundying in {self.school} "

    def get_details(self):
        return (self.name, self.surname, self.age, self.school, self.path)
        

    
    

person1 = Student(28, "Ömer", "Zemheri", "FS", "Clarusway")

print(person1.get_details())
print(person1)