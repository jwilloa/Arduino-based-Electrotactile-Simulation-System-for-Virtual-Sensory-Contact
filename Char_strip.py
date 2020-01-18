import re
numbers = re.compile('-?\d+(?:\.\d+)?') #\d+(?:\.\d+)?
a = map(float, numbers.findall("['FBVector3d(-24.0865,', '91.1238,', '1.58411)', '>>>']]"))
del a[0]
print(a)
print(a[0])
print(a[1])
print(a[2])


