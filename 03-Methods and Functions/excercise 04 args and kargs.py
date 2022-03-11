def starargs(*args,**kargs):
    print(f"{args}  {kargs}"  )
    print(kargs)

student = {"Name1":"ashfaq","Name2":"tahani" }

starargs(1, 2, "hello",'I am here', student )
