try:
    f = open(testfile,'r')
    #f.write("Adding some new content")
except NameError:
    print("some error occured")
else:
    print("you have done executing the code. ")