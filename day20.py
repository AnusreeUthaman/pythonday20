#OBJECT ORIENTED PROGRAMMING LANGUAGE

 #class-prototype/blueprint to create an object
         #>properties(attributes)
         #>behaviour(methods)

 #object-instance(examples) of class
     

#__init__-constructor method invokes creation of object

#self- referance of that object 


#PILLARS
#1.encapsulation:-
    #is hiding information (data) and showing only necessary details outside world.

#2.inheritance-parent child relation
    #is when one thing gets properties and characteristics from another thing 
    #acquiring properties and behaviour from a parent

#3.polymorphism-the ability of an object to take on multiple 

#4.data abstraction-hidden
    #showing only necessary information,hiding the rest


'''
#pass-is a placeholder statement that does nothing when executed
    def fun():
        pass #to be implemented later.

'''

class Watch:
    def __init__(self,Brand,color):
        
         self.Brand_name=Brand#attribute
         self.color=color#attribute
         self.time="12:00 PM"#attribute
         
    def display_time(self):#method
        print(f"Time:{self.time}")#method

watch1=Watch("Rolex","silver")#object creation
watch2=Watch("Titan","black")#object creation

watch1.display_time()
watch2.display_time()


class Watch:
    def __init__(self,Brand,color,price):

        self.Brand_name=Brand
        self.color=color
        self.time="12.00 PM"
        self.price=price
        
    def show_details(self):
        print(f"Brand:{self.Brand_name}")
        print(f"color:{self.color}")
        print(f"Time:{self.time}")
        print(f"price:{self.price}")

watch1=Watch("Rolex","silver",50000)
watch2=Watch("Titan","black",20000)

watch1.show_details()
watch2.show_details()


class Watch:
    def __init__(self,Brand,color,new_time):
        self.Brand_name=Brand
        self.color=color
        self.time="12:00 PM"
        self.time=new_time

    def update_time(self):
        print(f"updated_time:{self.time}")

watch1=Watch("Rolex","silver","10:00 AM")
watch2=Watch("Titan","black","11:00 AM")

watch1.update_time()
watch2.update_time()

class Watch:
    def __init__(self,Brand,color,price,budget):
        self.Brand_name=Brand
        self.color=color
        self.price=price
        self.budget=budget
        
    def is_affordable(self,budget):
        if self.price<=budget:
            print("its affordable")
        else:
            print("not affordable")
            
watch1=Watch("Rolex","silver",1000,500)
watch2=Watch("Titan","black",1000,2000)

watch1.is_affordable(500)
watch2.is_affordable(2000)


#inheritance-

class Animal:
    def __init__(self,name):
        self.name=name

class Dog(Animal):
    def speak(self):
        print("woo")

class Cat(Animal):
    def speak(self):
        print("meow")

animal1=Animal("Sample")
animal2=Dog("Buddy")
animal3=Cat("pinky")

print(animal1.name)
print(animal2.name,animal2.speak())
print(animal3.name,animal3.speak())


print(animal1.name)
print(animal2.name)
animal2.speak()
print(animal3.name)
animal3.speak()


class Animal:
    def __init__(self,name):
        self.name=name

        
class Dog(Animal):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age

    def speak(self):
        print("woow")
        
    def age_(self):
        print(f"Age:{self.age}")
        
        
class Cat(Animal):
    def speak(self):
        print("meoww")
        
animal1=Animal("sample")
animal2=Dog("rockey",0)
animal2_=Dog("buddy",3)
animal3=Cat("pinky")

animal2.speak()
animal2_.age_()
animal3.speak()



