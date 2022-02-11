'''#0
names =['Aidana' , 'Salima' , 'halid']
a = (5,'hello', 5,5,5,5,5,True, 'world', 2.88,"bestprog", 5, 'hello' , True, 3.88,)
names.extend(a)
names.remove('world')
names.pop(0)
print(names.index('hello'))
print(names)
names.pop(3)
print(names.count(5))

#1
d = ('hello', 66, 8.9)
print(d[1])
print(d[0])
print(d[2])

#2
lis = []
lis.append('ok')
lis.append(5)
lis.append(4.5)
lis.append(True)
tupl = ('altynbubu')
lis.append(tupl)
print(lis)

#3
lis = ['adil' , 'key' , 'bek' ,'gul']
str = " ".join(lis)
print(str)

#4
lis1 = ['fdg', 'fvg', 'fgfaf']
lis2 = ['Float',True,'bek']
lis1.extend(lis2)
print(lis1)
#5

a = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon',]
print(a.count("Jack"))
#6

a = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon',]
print(a.remove('Oskar'))

#7
a = ['altynbubu', 2000, 'python']
print(a)
#8

a = 'hello sjakkk', 'dsdss',30
print(a)
a = tuple('hello dsf')
print(a)
print(a.count(30))

my_list = ['python', 'is', 'awesome']
my_tuple = ('python' , 'is' ,'awesome')

print(my_list._sizeof())
print(my_tuple._sizeof_())

a = (1, 'b',3)
ex = list(a)
print(ex)

a = [1,'b',3]
ex = tuple(a)
print(ex)
a = {'c': 1, 'b': 'wow'}
ex = list(a)
print(ex)
'''
a =(('tom',33), ('bob',27))
ex = dict(a)
print(ex)
