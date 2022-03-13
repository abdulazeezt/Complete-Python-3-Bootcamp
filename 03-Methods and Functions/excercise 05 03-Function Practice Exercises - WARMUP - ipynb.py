## LESSER OF TWO EVENS: ###########
'''
def Lesser_of_two_evens(a,b):
    if a < b :
        print (f"b is the larger {b} than a {a}")
    elif b > a :
        print(f"b {b} is greater than a {a}")
    else:
        print(f" Both are equal b {b} and a  {a}")
Lesser_of_two_evens(20,20)
'''

### ANIMAL CRACKERS:

def animal_crackers(text):
    print(f"You have inserted \" {text} \"  ")
    #list1 = split(text)
    texts = str(text)
    texts1 = texts.split()
    
    print(f"You have inserted \" {texts1} \"  ")

animal_crackers(f"Hello how are you ")

