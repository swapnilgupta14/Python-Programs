class Employee:
    def __init__(self,job_band,employee_name,basic_salary,qualification):
        self.__job_band=job_band
        self.__employee_name=employee_name
        self.__basic_salary=basic_salary
        self.__qualification=qualification
        
    def get__employee_name(self):
        return self.__basic_salary
    def get__job_band(self):
        return self.__job_band
    def get__basic_salary(self):
        return self.__basic_salary
    def get__qualification(self):
        return self.__qualification
    
    def validate_job_band(self):
        pass
    def calculate_gross_salary(self):
        pass
    def validate_basic_salary(self):
        if self.__basic_salary>3000:
            return True
        else:
            return False
    def validate_qualification(self):
        if self.__qualification in emp_qualification:
            return True
        else:
            return False
        
class Graduate(Employee):
    def __init__(self,job_hand,employee_name,basic_salary,qualification,cgpa):
        super().__init__(job_band,employee_name,basic_salary,qualificationa):
            self.__cgpa=cgpa
    def get_cgpa(self):
        return self.__cgpa
    def validate__job_band(self):
        band=Employee.get__job_band(self)
        if band in graduate_job_band:
            return True
        else:
            return False
    def calculate_gross_salary(self):
        if self.validate_basic_salary()==True and self.validate_qualification()==True and self.validate_job_band()==True:
            incentive=0
            tpi=0
            salary=Employee.get__basic_salary(self)
            band=Employee.get__job_band(self)
            incent=emp_incentive(band)
            incentive=incent/100
        if 4<=self.__cgpa<=4.25:
            tpi=1000
        elif 4.26<=self.__cgpa<=4.5:
            tpi=1700
        elif 4.51<=self.__cgpa<=4.75:
            tpi=3200
        elif 4.76<=self.__cgpa<=5:
            tpi=5000
            
            
        
    class Lateral(Employee):
        def __init__(self,job_band,employee_name,basic_salary,qualification,skill_set):
            super().__init__(job_band,employee_name,basic_salary,qualification)
            self.__skill_set =skill_set
        def validate_job_band(self):
            band=Employee.get__job_band(self)
            if band in lateral_job:
                return True
            else:
                return False
        def calculate_gross_salary(self):
            if self.validate_basic_salary()==True and self.validate_qualification()==True and self.validate_job_band()==True:
                sme=0
                incentive=0
                band=Employee.get__job_band(self)
                salary=Employee.get._basic_salary(self)
                incent=emp_incentive[band]
                incentive=incent/100
                sme=bonus(self.__skill_set)
                gross_salary=salary+salary+incentive+sme+salary*0.12
                return gross_salary
            else:
                return -1
l=Lateral("D","Rajat",6500,"Masters","AGP")
g=Graduate("B","RajatV",6500,Masters,4.65)
print(l.get_skill_set())
print(l.validate_job_band())
print(l.validate_gross_salary())
print(g.calculate_gross_salary())
        
            