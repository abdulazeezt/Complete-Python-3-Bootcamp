import re
mytext1 = "The person's phone number is 408-555-1234. Call soon!"
matchresult = re.search(r"\d\d\d-\d\d\d-\d\d\d\d",mytext1)
matchresult.start
print ("Our input string is: " + matchresult.string)
print (" matching the pattern")
print (f"This is the match for phone r\"\d\d\d-\d\d\d-\d\d\d\d\" :  {matchresult.group()}")

print ("Matching using quantifiers")

matchresult1 = re.search(r"\d{3}-\d{3}-\d{4}",mytext1)


print (" matching the quantifiers")
print (f"This is the match for phone number  using quantifiers r\"\d{3}-\d{3}-\d{4}\" :  {matchresult1.group()}")

