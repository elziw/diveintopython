



#Here the first 0 between curly brackets refers to mylist wherehas  the 0 or 1 one between brackets refers to the item index inside the list.

query = 'user=pilgrim&database=master&password=PapayaWhip'
splittedlist = query.split('&')
print(splittedlist)
print(type(splittedlist))


for v in splittedlist:
    if '=' in v:
        print(v.split('=', 1))

by = b'acbde'
s = 'b'
print(by.count(s.encode()))








