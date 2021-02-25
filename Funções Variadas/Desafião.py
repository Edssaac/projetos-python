first_value = '  FIRST challenge         '
second_value = '-  second challenge  -'
third_value = 'tH IR D-C HALLE NGE'

fourth_value = 'fourth'
fifth_value = 'fifth'
sixth_value = 'sixth'

# First challenge
print (first_value.lower().title().rjust(31))

# Second challenge
print(second_value.replace("-", " ").strip().capitalize())

# Third challenge


# print(first_value)
# print(second_value)
print(third_value.lower().replace(" ", "").capitalize().rjust(30), sep="")

# Fourth challenge - use only the print() function (no f-strings)
print(fourth_value, end="#")
print(fifth_value, end="#")
print(sixth_value, end="!")

# Fifth challenge - use only a single print() function.  Create tabs and new lines using f-strings.
print (f"\n\t{fourth_value}\n\t{fifth_value}\n\t{sixth_value}")