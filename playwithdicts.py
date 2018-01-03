import glob
import os
mydict = {'Name': 'Zied', 'Surname': 'Bejaoui', 'Age': '33'}

print(mydict['Name'])

mydict['Name'] = 'Amina'

print(mydict)

metadatadic = {f: os.stat(f) for f in glob.glob('*playwith*.py')}
print(metadatadic)
type(metadatadic)
print(metadatadic.keys())

for f in glob.glob('*playwith*.py'):
    metadatadic1 = {f:os.stat(f)}
    print(metadatadic)
    type(metadatadic)
    print(metadatadic.keys())
    size = metadatadic['playwithsets.py'].st_size
    print(size)



