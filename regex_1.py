# import re
# value = "This is a string"
# output = re,search("^This.*strings$",value)
# print(output)


pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+=-])(?=.{8,})"
# \	Used to drop the special meaning of character following it
# []	Represent a character class
# ^	Matches the beginning
# $	Matches the end
# .	Matches any character except newline
# |	Means OR (Matches with any of the characters separated by it.
# ?	Matches zero or one occurrence
# *	Any number of occurrences (including 0 occurrences)
# +	One or more occurrences
# {}	Indicate the number of occurrences of a preceding RegEx to match.
# ()	Enclose a group of RegEx