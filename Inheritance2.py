# Example 4


class Animal:
    def sound(self):
        print("All animals Makes sound")

class Dog(Animal):
    def bark(self):
        print("Dogs generally barks")

class Cat(Animal):
    def meow(self):
        print("Cats Meow")


dog1 = Dog()
dog1.sound()
dog1.bark()

cat1 = Cat()
cat1.sound()
cat1.meow()





# 5 Example

#Multiple Inheritance 

print("Example 5")
class Father:
    def father_skill(self):
        print("Good at farming")

class Mother:
    def mother_skill(self):
        print("Good at cooking")

class Child(Father,Mother):
    def child_skill(self):
        print("Good footballer")


c = Child()
c.father_skill()
c.mother_skill()
c.child_skill()


# Multilevel Inheritance

print("MultiLevel inheritance Question")

class Grandfather:
    def asset(self):
        print("Owns Homes")
            

class Father(Grandfather):
    def car(self):
        print("Own a car")

class Child(Father):
    def laptop(self):
        print("Owns a laptop")

Child = Child()
Child.asset()
Child.car()
Child.laptop()



# Questions to practise it out


class Person:
    def greet(Self):
        print("Hello, I am a person")

class Student(Person):
    def study(self):
        print("I am studying")

stu = Student()
stu.greet()
stu.study()

# 2 Question MEthod overriding

class Shape:
    def area(self):
        print("Area is undefined")

class Circle(Shape):
    def area(self):
        print("Area = 3.14 *r *r")

s1 = Shape()
s1.area()

s2 = Circle()
s2.area()


# 3 Practise Question

class Animal:
    def eat(self):
        print("I can eat")

class Dog(Animal):
    def bark(self):
        print("Woof woof!!")

d1 = Dog()
d1.eat()
d1.bark()

# 4 Question practise


class Laptop:
    def __init__(self,brand):
        self.brand = brand
        print(brand)

class GamingLaptop(Laptop):
    def __init__(self, brand):
        super().__init__(brand)
        

    def features(self):
        print("RGB Keyboard and high performance")
    


c1 = Laptop("Acer")

c2 = GamingLaptop("DEll")
c2.features()


# 5 question pratice


class Father:

    def work(self):
        print("Works as Engineer")

class Mother:

    def hobby(self):
        print("Loves Gardening")


class Child(Father , Mother):
    def play(self):
        print("Playing Football")


c1 = Child()
c1.work()
c1.hobby()
c1.play()


# 6 Practise questions



class Grandfather:
    def property(self):
        print("Owns Land")

class Father(Grandfather):
    def car(self):
        print("Owns a car")

class Son(Father):
    def bike(self):
        print("Owns a bike")

son = Son()
son.property()
son.car()
son.bike()



# 7 Override Method

class Employee:
    def work(self):
        print("Works 9 to 5")

class Freelancer(Employee):
    def work(self):
        print("Works Flexible Hours")
    

employee =Employee()
employee.work()

freelancer =Freelancer()
freelancer.work()











