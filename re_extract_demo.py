import re
demo_str =  "this_is_1231232_sdffd_12312"
m = re.findall(r"(?P<ordinal>\d+)",demo_str)
m = re.split(r"\d+",demo_str)
m = re.sub(r"\D+",repl="0",string = demo_str)
# re.findall re.sub re.split re
print(m)
import string
import operator
operator.iadd()
str.maketrans()
str.translate()
string.ascii_lowercase
string.ascii_uppercase

