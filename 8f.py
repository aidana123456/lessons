'''
#1
a = 'hello'.upper()
b = 'WORLD'.lower()
print(a,b)
#2
a = True
print(type(a))
b = str(a)
print(type(b))

#3
a = input()
b = 'Github'
c = a.join(b)
print(c)
#4
a = """Ботнет IPStorm , в который ранее входили 
лишь Windows-машины, увеличился до 13 500 зараженных 
"""
print(a.replace('е','3'))

#5
a = """Google создаст специальную команду для 
поиска багов в особо важных приложениях.
"""
b = a.split()
print(len(b))

#6
a = 'Самые важные собЫтия в миРе инфосека за сентябрь'
b = "|".join(a)
print(b)
#7
a = """хакеры слили в сеть данные пакистанской
 энергетической компании k-Electric"""
print(a.title())
'''

name = input('сиздин атыныз ким ?')
age = int(input('сиздин жашыныз канчада?'))
movie = input('жакшы коргон тасманызды атаныз?')
print('hello {}, you are {}, oh? good movie {}!'.format(name, age, movie))





















































































































































