class person:
            def __init__(self,name,age):
                self.name=name
                self.age=age
        

            def display(self):
                print("person details")
                print(f"name:{self.name}")
                print(f"age:{self.age}")


class employee(person):
            def __init__ (self, name,age,employee_id,salary):
                person.__init__(self,name,age)
                self.employee_id=employee_id
                self.salary=salary

            def display(self):
                person.display(self)
                print(f"employee_id:{self.employee_id}")
                print(f"salary:{salary}")


class manager(employee):
                def __init__(self ,name,age,employee_id,salary,department):
                    employee.__init__(self,name,age,employee_id,salary)
                    self.department=department

                def display(self):
                    employee.display(self)
                    print(f"department:{department}")

                #-------main program--------#
p=None
e=None
m=None
print(("--- python OOP project :employee managemet system ---") )
while True:
                print("-------------main menu---------")
                print("choose an operation")
                print("1.create a person")
                print("2.crate an employee")
                print("3.create a manager")
                print("4. show details")
                print("5.exit")

                choice=input("enter your choice:")



                if choice=="1":   
                
                        name=input("enter your name:")
                        age=int(input("enter your age:"))
                        p=person(name,age)

                        print(f"person created with name:{name} and age:{age}")


                        print("------choose another operation------")


                elif choice =="2":
                    name=input("enter your name")
                    age=int(input("enter your age:"))
                    employee_id=input("enter your employee_id:")
                    salary=input("enter your salary")
                    e=employee(name,age, employee_id,salary)

                    print(f"employee created with name:{name} and age:{age} and employee_id:{employee_id} and salary:{salary}")  
                    print() 

                    print("------choose another operation------")


                

                elif choice =="3":
                    name=input("enter your name")
                    age=int(input("enter your age:"))
                    employee_id=input("enter your employee_id:")
                    salary=input("enter your salary")  
                    department=input("enter your department")
                    m=manager(name,age,employee_id,salary,department)

                    print(f"employee created with name:{name} and age:{age} and employee_id:{employee_id} and salary:{salary} and department{department}")  
                    print() 


                    print("------choose another operation------")

                elif choice == "4":
                    print("choose details to show:")
                    print("1. Person")
                    print("2. Employee")
                    print("3. Manager")

                    option = input("show any one:")

                    if option == "1" and p is not None:
                     p.display()

                    elif option == "2" and e is not None:
                     e.display()

                    elif option == "3" and m is not None:
                     m.display()

                    else:
                     print("no data available")

                    print()
                    print("------choose another operation------")

                elif choice == "5":
                    print("Exiting the system. All resources have been freed.")
                    print()
                    print("Goodbye!!")
                    break
    

        

            


            