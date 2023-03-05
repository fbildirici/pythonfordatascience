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

## amaç: çift sayıların karesini alarak bir sözlüğe eklemek
## odak: keyler aynı kalacak, valueların bir kısmının karesi alınacak onlar değişecek

numbers = range(10) ##0dan 10a kadar sayı oluştur
new_dict = {} #boş bir sözlük oluştur

for n in numbers:
    if n % 2 == 0:
     new_dict[n] = n ** 2        ##burada ilk [n] değişmeyecek keyi atar, ikincisi value değerini

### dictcomprehension

{n: n ** 2 for n in numbers if n % 2 == 0}

