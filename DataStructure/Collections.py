import collections

how_many = "abc abc def"
c = collections.Counter(how_many) #dictionary with numbers
print(c["a"])

print(how_many.split("b"))