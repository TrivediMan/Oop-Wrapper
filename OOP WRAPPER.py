print("--- Python OOP Project: Employee Management system ---")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def show_details(self):
        super().show_details()
        print(f"Salary: {self.salary}")


class Manager(Employee):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)
        self.department = department

    def show_details(self):
        super().show_details()
        print(f"Department: {self.department}")


# Storage for created objects
people = []

def compare_salaries():
    employees = [p for p in people if isinstance(p, Employee)]
    if len(employees) < 2:
        print("Need at least 2 employees to compare salaries.")
        return
    for i in range(len(employees)):
        for j in range(i + 1, len(employees)):
            e1 = employees[i]
            e2 = employees[j]
            if e1.salary > e2.salary:
                print(f"{e1.name} has a higher salary than {e2.name}.")
            elif e1.salary < e2.salary:
                print(f"{e2.name} has a higher salary than {e1.name}.")
            else:
                print(f"{e1.name} and {e2.name} have equal salaries.")


# Menu
while True:
    print("\n--- Python OOP Project: Employee Management System ---")
    print("Choose an operation:")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Show Details")
    print("5. Compare Salaries")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Rahul: ")
        age = int(input("30: "))
        person = Person(name, age)
        people.append(person)

    elif choice == '2':
        name = input("Hiren: ")
        age = int(input("28: "))
        salary = float(input("50000: "))
        emp_id = input("E123: ")
        employee = Employee(name, age, salary)
        people.append(employee)

    elif choice == '3':
        name = input("Tony Stark: ")
        age = int(input("40: "))
        salary = float(input("100000: "))
        empl_id = input("M456: ")
        department = input("sales: ")
        manager = Manager(name, age, salary, department)
        people.append(manager)

    elif choice == '4':
        for i, p in enumerate(people):
            print(f"\n--- Details of Person {i + 1} ---")
            p.show_details()

    elif choice == '5':
        compare_salaries()

    elif choice == '6':
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please try again.")

    print("Exiting the system. All resources have been freed.")
    print("Goodbye!")