import pprint
cats = [{'name': 'Zoe', 'desc':'chubby'},{'name': 'Este', 'desc': 'fluffy'}]
print(pprint.pformat(cats))
file = open('Cats.py', 'w')
file.write('cats ='+ pprint.pformat(cats)+'\n')
file.close()
pag = 233