#Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage

    def details(self):
        print("Maximum Speed is",self.max_speed,"And Mileage is",self.mileage)
obj=Vehicle(300,24)
obj.details()

def get_next_highest_salary(employees):
    for employee in employees:
        next_highest_salary = 0
        next_highest_name = None
        for compare_employee in employees:
            if compare_employee['Department'] == employee['Department'] and compare_employee['Salary'] > employee['Salary']:
                if next_highest_salary == 0 or compare_employee['Salary'] < next_highest_salary:
                    next_highest_salary = compare_employee['Salary']
                    next_highest_name = compare_employee['Employee']
        employee['next_highest_salary'] = next_highest_salary
        employee['next_highest_name'] = next_highest_name
    return employees
emp=[{'Employee': 'A', 'Salary':1000, 'Department': 'IT'},
       {'Employee': 'C', 'Salary':3000, 'Department': 'IT'},
       {'Employee': 'B', 'Salary':2000, 'Department': 'IT'},
       {'Employee': 'D', 'Salary':4000, 'Department': 'HR'},
       {'Employee': 'E', 'Salary':2000, 'Department': 'HR'},
       {'Employee': 'F', 'Salary':1500, 'Department': 'IT'},
       {'Employee': 'G', 'Salary':7000, 'Department': 'HR'}]
a = get_next_highest_salary(emp)
print(a)