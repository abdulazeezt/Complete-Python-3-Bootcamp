from one import one_func

one_func()

################# One.py #################################
def two_func():
    print("I am two.py : I am from two_func")

if __name__ == "__main__":
    print("I am two.py : This is been run from two.py directly")
else:
    print(" this is two.py : THis is been running through another script    ")

##########################################################