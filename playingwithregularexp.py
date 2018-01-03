import re

# addresses = ["11 rue de Lorraine 92600", "17 Ter rue du Tintorêt 92600", "2 Oulton Road N155PY", "44 rue 18 Janvier 7050", '12 rue de morue 93400', '33 rue de rue 4400']
# s = "rue"
# for i in addresses:
#     if 'rue' in i:
#         print(re.sub(r'\brue\b', 'road', i)
# )

pattern = '^M{0,3}$'

source = ["", "M", "MM", "MMM", 'MMMM', 'MMA', 'ACD']


for i, v in enumerate(source):
      print(i, re.search(pattern, v))

pattern = '''
    ^                   # beginning of string
    M{0,3}              # thousands - 0 to 3 Ms
    (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 Cs),
                        #            or 500-800 (D, followed by 0 to 3 Cs)
    (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 Xs),
                        #        or 50-80 (L, followed by 0 to 3 Xs)
    (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 Is),
                        #        or 5-8 (V, followed by 0 to 3 Is)
    $                   # end of string
    '''
print(re.search(pattern, 'M', re.VERBOSE))
print(re.search(pattern, 'MCMLXXXIX', re.VERBOSE))
print(re.search(pattern, 'MMMDCCCLXXXVIII', re.VERBOSE))
print(re.search(pattern, 'M'))



