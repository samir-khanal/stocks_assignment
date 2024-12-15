class Person:
    def __init__(self,name,address,age):
        self.name = name
        self.address = address
        self.age = age

    def display_info(self):
        print(f"name: {self.name}")
        print(f"address: {self.address}")
        print(f"age: {self.age}")

person_info = Person("Samir","KTM",21)

person_info.display_info()