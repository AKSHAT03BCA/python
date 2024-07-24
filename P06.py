a=20
b=20
if (a is b):
    print("line 1 - a and b have same identity")
else:
    print("line 1 - a and b have not same identity")
if (id(a) == id(b)):
    print("line 2 - a and b have same identity")
else:
     print("line 2 - a and b not have same identity")

b=30
if (a is b):
    print("line 3 - a and b have same identity")
else:
    print("line 3 - a and b have not same identity")
if (a is not b):
    print("line 4 -  a and b have not smae identity")
else:
    print("line 4 - a and b have same identity")
