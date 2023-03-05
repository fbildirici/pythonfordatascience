#### dict comprehension

dictionary = {'a' : 1,
              'b' : 2,
              'c' : 3,
              'd' : 4


dictionary.keys() ## a,b,c,d
dictionary.values() # 1,2,3,4
dictionary.items() #tuple halinde çiftler

### hadi bu sözlükteki her value değerinin karelerini alalım

{k: v ** 2 for (k, v) in dictionary.items()}

## value değerlerine işlem yapalım

{k.upper(): v for (k, v) in dictionary.items()}


####### UYGULAMA SORUSU#########


