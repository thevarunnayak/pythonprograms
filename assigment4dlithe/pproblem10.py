import re
string = input()
special = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
if special.search(string) is None:
    print("String is accepted")

else:
    print("String is not accepted.")
