# Homework : EP6
# Title : class
# Programer: Wiriya Tumnao
# date: Mar 9, 2023

class company():
    companyName = 'Tumnao Technology company'
    departmentName = 'Information Systems Department'
  
    # constructor
    def __init__(self, empName, salary):
        self.empName = empName
        self.salary = salary

    def salaryCheck(self):
        if self.salary >=100000:
            print(f'พนักงานชื่อ: {self.empName}')
            print(f'ตำแหน่ง : GM\n')
        elif self.salary >=50000:
           print(f'พนักงานชื่อ: {self.empName}')
           print (f'ตำแหน่ง : Manager\n')
        elif self.salary >=20000:
            print(f'พนักงานชื่อ: {self.empName}')
            print(f'ตำแหน่ง : Supervisor\n')
        else:
           print(f'พนักงานชื่อ: {self.empName}')
           print(f'ตำแหน่ง : Staff\n')
# instance
print (f'ชื่อบริษัท : {company.companyName}')
print (f'ผลิตภัณฑ์ : {company.departmentName}')

company01 = company('เพชร ทำเนาว์',150000)
company01.salaryCheck()

company02 = company('ภูมิ ทำเนาว์',60000)
company02.salaryCheck()


company03 = company('วิริยะ ทำเนาว์',15000)
company03.salaryCheck()


# End
