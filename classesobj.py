# x = 5
# print(type(x))

# class laptop:
#     def __init__(self):
#         print("Hello world")
#     def config(self):
#         print("Asus","i7","1TB")
# laptop1=laptop()
# laptop2=laptop()
#laptop.config(laptop1) 
# laptop.config(laptop2)
# class student:
#     def __init__(self,name,rollno):
#         self.name = name
#         self.rollno = rollno
#     def info(self):
#         print("name :",self.name,"rollno is : ",self.rollno) 
# student1=student("Rajesh","21")
# student2=student("srikaran","44")
# student.info(student1)
# student.info(student2) 
# print(id(student2))
# print(id(student1))

# class person:
#     def __init__(self):
#         self.name = "Virat"
#         self.number = 18
#     def compare(self,other):
#         if(self.number == other.number):
#             return True
#         else:
#             return False        
# p1 = person()
# p2 = person()
# p2.number = 45
# if p1.compare(p2):
#     print("same")
# else:
#     print("different")    
#  p1.name = "Kohli"
# print(p1.number)
# print(p2.name)
# Instance Variables-value varies from obj to obj
# static variable
# class car:
#     wheels = 4
#     def __init__(self):
#         self.company = "bmw"
#         self.mileage = 10
# car1 = car()
# car2 = car()
# car.wheels = 5
# print(car1.mileage,car1.wheels)
# print(car2.mileage,car2.wheels)

class student:
    collegeName = "LPU"
    def __init__(self,python,web,math):
        self.subject1 = python
        self.subject2 = web
        self.subject3 = math
# def avgcalculator(self):
#     return (self.subject1 + self.subject2 + self.subject3)/3

# def get_subject1(self):
#     return self.subject1

def collegedetail(cls):
    return cls.collegeName

student1 = student(4,7,8)
student2 = student(2,3,9)
print(student1.collegedetail())
