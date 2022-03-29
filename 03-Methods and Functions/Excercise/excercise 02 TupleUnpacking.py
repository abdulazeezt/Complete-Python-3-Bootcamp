####################
###This example using TUPLE unpacking. 
####################

employeedata = [("billy",40000),("Cassie",300 ) , ("John",500) , ("Unknown",300) ]

def employeecheck(inputtuple):
    current_max = 0
    employee_of_month =  ""
    for employee , hours in inputtuple:
        #print(f"{employee} {hours}")
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
            print(f"new value will be added{hours}")
        else:
            pass

        print(f"currnt emp is {employee} and hours {hours}")

    return(employee_of_month,current_max)

employeecheckresult = employeecheck(employeedata)
print(f"The output is : {employeecheckresult}")

### WE CAN DO TUPLE UNPACING IN THIS WAY TOO. BY DIRECTLY SAVING THE RESULT TO VARIABLE.
empofmonth , hourworked = employeecheck(employeedata)
