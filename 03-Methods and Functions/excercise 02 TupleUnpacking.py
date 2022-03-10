####################
###This example using TUPLE unpacking. 
#######################3'''

employeedata = [("billy",400),("Cassie",300 ) , ("John",500) ]

def employeecheck(inputtuple):
    
    current_max = 0
    employee_of_month = 0
    
    for employee , hours in inputtuple:
        print(f"{employee} {hours}")
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        
        return("employee",hours)


employeecheck(employeedata)