def number(a,b):
    if type(a) != str or type(b) != str:
       return '0'
    elif a == b:
        return '1'
    elif len(a) > len(b):
        return '2'
    elif b == 'learn' :
       return '3'

print(number(1,'2'))
print(number('11','11'))
print(number('123','24'))
print(number('1','learn'))
print(number('2','22'))