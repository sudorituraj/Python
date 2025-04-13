# Example 1
'''
class parent():
    def skills(self):
        print("I can cook and drive")

class child(parent):
    def hobbies(self):
        print("I love standup comedy")


obj = child()
obj.skills()
obj.hobbies()'''




# Example 2

'''
class Vehicle:  # PascalCase for class names
    def general_info(self):
        ask = input("What you Own? (bike or car) ").lower()
        if ask == "bike":
            print("All bikes have 2 wheels")
            return "bike"
        elif ask == "car":
            print("All cars have 4 wheels")
            return "car"
        else:
            print("Invalid input")
            return None

class Bike(Vehicle):  # Inherits from Vehicle
    def bike_info(self):  # Consistent method naming
        print("I've a bullet and a Splendor")

class Car(Vehicle):  # Inherits from Vehicle (not from Bike)
    def car_info(self):  # Consistent method naming
        print("I own two cars as well: 1. Astor, 2. Thar")

# Create Vehicle object
veh = Vehicle()

# Call general_info on the instance (not the class)
veh_type = veh.general_info()

if veh_type == "bike":
    my_bike = Bike()  # Different variable name
    my_bike.bike_info()
elif veh_type == "car":
    my_car = Car()  # Different variable name
    my_car.car_info()
    
    '''




# 3. Practise question


class Employee:
    def __init__(self , name , salary):
        self.name = name
        self.salary = salary
        pass
    

    def show(self):
        print(f"Name = {self.name}, Salary ={self.salary}")
              

class Manager(Employee):
    def __init__(self, name, salary,department):
        super().__init__(name, salary) # Calling parent constructor

        self.department = department

    def show_manager(self):
        print(f"Manager of {self.department} Department")



m1 = Manager("RITU RAJ","$1000","BCA")
m1.show()
m1.show_manager()



# best and good example of overriding

class SmartphoneCamera:
    def take_photo(self):
        print("Taking a standard Photo")

    def record_video(self):
        print("Recording 1080p video")

class Budgetphone(SmartphoneCamera):
    pass


class FlagshipPhone(SmartphoneCamera):
    def take_photo(self):
        print("Taking 48MP photo with night mode ")

    def record_video(self):
        print("Recoding 8K videos with cinematic stabilization")

class SelfiePhone(SmartphoneCamera):
    def take_photo(self):
        print("Taking 32MP selfie with beauty filter")

    def take_portrait(self):
        print("Taking Portraits with bokeh effect")





# Create objects
budget = Budgetphone()
flagship = FlagshipPhone()
selfie = SelfiePhone()

# Test functionality
print("Budget Phone:")
budget.take_photo()  # Uses parent's version
budget.record_video()  # Uses parent's version

print("\nFlagship Phone:")
flagship.take_photo()  # Uses overridden version
flagship.record_video()  # Uses overridden version

print("\nSelfie Phone:")
selfie.take_photo()  # Uses overridden version
selfie.take_portrait()  # Uses new method
selfie.record_video()  # Inherited from parent














































