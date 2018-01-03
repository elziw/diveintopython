import glob
import os
my_tuple = ("a","b","c","d","e","f")
print(my_tuple)
print(my_tuple[1:3])
print(my_tuple[1:-3])
(MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY) = range(7)
print(MONDAY)
print(SUNDAY)
v = ("a", "b", "c")
(x, y, z) = v
print(x)
print(z)

glob.glob('*.py')
for f in glob.glob('*.py'):
        filetuple = (os.path.realpath(f), os.stat(f).st_size)
        print(filetuple)