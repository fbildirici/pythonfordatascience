#########comprehensions

### list comprehensions #####

salaries = [1000, 2000, 3000, 4000, 5000]

def new_salary(x):
    return x * 20  / 100 + x

for salary in salaries:
    print(new_salary(salary))
## her bir elemanda gezip yüzde 20 zam yapan bir fonksiyon yazdık, cepte.

## hadi şimdi bir null_list ekleyelim boş buradaki maaşları ona yazdıralım

null_list = []

for salary in salaries:
    null_list.append(new_salary(salary))

### maaşlar 3000den büyükse bir işlem küçükse başka bir işlem yapalım

for salary in salaries:
    if salary > 3000:
      null_list.append(new_salary(salary))
else:
      null_list.append(new_salary(salary * 2))

### bu işlemler klasik yöntemlerdi
## tüm bu işlemlerde sonucu liste olacak bu yapıyı tek bir list comprehension satırında görebiliriz

[new_salary(salary * 2) if salary < 3000 else new_salary(salary) for salary in salaries]

## sonuçta bize [2400.0, 4800.0, 3600.0, 4800.0, 6000.0] sonucunu döndürür aynı şekilde bu comprehension yapısı


