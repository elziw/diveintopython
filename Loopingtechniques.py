# Looping through a dictionnary items
films = {'the revenant': 'Leonardo Dicaprio', 'cast away': 'Tom Hanks'}

for k, v in films.items():
    print(k, v)

# Looping through a list by displaying indexes :

charts = ['Ed Sheeran', 'Rihana', 'Eminem']
for i,v in enumerate(charts):
    print(i, v)

questions = ['Name', 'Age', 'Favourite Color']
answers = ['Zied', 33, 'Blue']
for i, v in zip(questions, answers):
    print('What is your {0} ? , its {1}.'.format(i, v))

#Looping through a list in reverse
range = [1, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range.__reversed__():
    print(i)

#Connot reverse a set as memebers are not ordered.

#Loop through a set in sorted order :
intset = {1, 44, 2, 15, 12, 30, 67, 4}
for i in sorted(intset):
    print(i)

basket = ['strawberyy', 'banana', 'apple', 'lemon']
for i in sorted(basket):
    print(i)
    print(type(i))


