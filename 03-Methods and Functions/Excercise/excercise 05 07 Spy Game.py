#SPY GAME: Write a function that takes in a list of integers and 
# returns True if it contains 007 in order
#spy_game([1,2,4,0,0,7,5]) --> True
#spy_game([1,0,2,4,0,5,7]) --> True
#spy_game([1,7,2,0,4,5,0]) --> False

def spy_game(nums):
    #firstnum = 0
    #secondnum = 0
    #thirdnum = 0
    code = [0,0,7,'x']
        #print(f"{i}")
    for num in nums:
        if code[0] == num:
            code.pop(0)

    return len(code) == 1


numlist = [2,50,30,49,0,0,7,4]
output = spy_game(numlist)
print(f"{output}")