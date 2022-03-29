#############################################################
#ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
#almost_there(90) --> True
#almost_there(104) --> True
#almost_there(150) --> False
#almost_there(209) --> True

#############################################################

def almost_there(inputval):
    print(f"Absolute value is   {abs(inputval)}")
    if abs(inputval) < 10 :
        print(f"You are within 10")
    else:
        pass

almost_there(9)

