import re

pat="name"
str="was is name what Day  name Week year number name num str string "


a=re.search(r'[A-D]ay',str) # r - raw format
print(a)