class Person:
    def __init__(self, uname, city, age):
        self.uname = uname
        self.city = city
        self.age = age

    def get_name(self):
	    return self.uname

class User(Person):
     def __init__(self, uname, city, age, salary):
          super().__init__(uname, city, age)
          self.salary = salary
    

if __name__ == '__main__':
    p1 = Person('viswhas','Bangalore', '30')
    print(p1.uname)
    p1.tag = "Friend"
    print(p1.tag)