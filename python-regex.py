
# find email with patter "@gmail.com"

# import re module
import re

myEmail = ["jissmon@gmail.com", "jerin@yahoo.com"]
# create a regex pattern
searchPattern = re.compile("@gmail\.com")
for email in myEmail:
    # search that pattern in given email
    if searchPattern.search(email):
    	# print those emails
        print(email)


