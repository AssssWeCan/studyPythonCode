from collections import OrderedDict

dictionary = OrderedDict()
dictionary['xiaoming'] = 'c'
dictionary['xiaojiling'] = 'none'
dictionary['zhoutong'] = 'php'
dictionary['liuxuan'] = 'c++'

for key,value in dictionary.items():
    print(key + ' like ' + value + ' most')