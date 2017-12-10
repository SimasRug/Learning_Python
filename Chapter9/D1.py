def conversion(value):
    alias = {'a':'id0', 'b':'id0', 'c':'id0','d':'id1', 'e':'id1', 'f':'id1', 'g':'id2', 'h':'id2', 'i':'id2', 'j':'id3', 'k':'id3', 'l':'id3', 'm':'id4', 'n':'id4', 'o':'id4', 'p':'id5', 'q':'id5', 'r':'id5', 's':'id5', 't':'id6', 'u':'id6', 'v':'id6', 'w':'id7', 'x':'id7', 'w':'id7', 'z':'id7', ' ':'id8', '1':'id9' }
    dictionary = {'id0':2, 'id1':3, 'id2':4, 'id3':5, 'id4':6, 'id5':7, 'id6':8, 'id:7':9, 'id8':0, 'id9':1}
    
    first_part = value[:-4]
    convert = value[-4:len(value)]
    convert = convert.lower()
    converted = ''
    for x in convert:
        converted += str(dictionary[alias[x]]) 
    return first_part + converted

num = '4100-555-BoOk'
print(conversion(num))






# print(dictionary[alias['a']])