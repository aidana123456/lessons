'''
#0
a = {3,10,11,13,31,21,1,10,3,5,6,6}
a.discard(7)
print(a)

#1
a = {"dog", "cat", "mouse", "sheep"}
b = {"cow", "horse", "donkey", "cat", "dog"}
a.intersection_update(a)
print(b)

#2

a = {"cow", "horse", "donkey", "cat", "dog"}

b = {"dog", "cat", "mouse", "sheep"}
a.difference(b)
print(a)

#3
a = {21,'hi', 25,'yes',6}
a.add('3')
a.pop()
print(a)

#00
menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
plus = {'besh_barmak': 130}
menu.update(plus)
print(menu)
menu.update({'lagman' :135})
print(menu)
menu.pop('borsh')
print(menu)

#01
menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
plus = {'drinks': ['coca-cola','fanta','cola']}
menu.update(plus)
print(menu)

#02
set1 = {'add()', 'remove()' , 'clear()','update()','difference()','discard()' ,'intersection()' ,'intersectin_update()' ,' discard()', 'pop()'}
dic = {'clear()','get()', 'keys()','values()','items()','update()','tuple()', 'set()','list()','dict()'}
d = set1.intersection(dic)
print(d)
'''
#31

