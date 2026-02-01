#Design a console based "Employee Payroll system" using oops python
#the ssystem should calculate salary for different type of employess using all oops concepts
#employee - Abstract class
#full time employee - child class
#part time employee - child class
#salary - encapsulated Data 
#payroll system- controller(HAS-A)
#OUTPUT-
#employee Created
#salary:50000
#employee Created
#salary:4000
#abstraction
class Employee:
    def __init__(self,emp_id,name):
        self.emp_id=emp_id
        self.name=name
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self,emp_id,name,monthly_salary):
        super().__init__(emp_id,name)
        self._monthly_salary=monthly_salary
        #ENCAPSULATION because salary is protected

    def calculate_salary(self):
        return self._monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self,emp_id,name,hours_worked,rate_per_hour):
        super().__init__(emp_id,name)
        self._hours_worked=hours_worked
        self._rate_per_hour=rate_per_hour
    def calculate_salary(self):
        return self._hours_worked * self._rate_per_hour
    
class PayrollApp:
    def __init__(self):
        self.employee=None
    def create_employee(self,emp_type):
        if emp_type=="FullTime":
            self.employee=FullTimeEmployee(1,"Amit",5000)
        else:
            self.employee=PartTimeEmployee(2,"Neha",80,500)
        return "Employee Created"
    
    def get_salary(self):
        return self.employee.calculate_salary()
    
app=PayrollApp()
print(app.create_employee("fulltime"))
print("Salary: ",app.get_salary())
app2=PayrollApp()
print(app.create_employee("PartTIme"))
print("salary: ",app.get_salary())