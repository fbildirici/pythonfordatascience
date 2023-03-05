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

## maaşlar listesindeki her maaşı 2 ile çarpacak bir comprehension yazalım

[salary * 2 for salary in salaries]

## hadi maaşı 3000den küçükleri 2 ile çarpalım sadece liste olarak alalım

[salary * 2 for salary in salaries if salary < 3000]

### not comprehension yapısında if tek kullanılırsa sağa yazılır
## else ile birlikteyse sola, for blogunun önüne yazılır

[salary * 2 if salary < 3000 else salary * 0 for salary in salaries]

## hadi bir de elimizdeki bir fonksiyonu bu comprehension içerisine ekleyelim

[new_salary(salary * 2) if salary < 3000 else new_salary(salary * 0.2 )for salary in salaries]

## burada new_Salary fonksiyonu içerisinde yaptık her iki işlemi de

## başka bir örnek yapalım öğrenci ve istenmeyen listesindeki öğrencileri gezsin
# comprehension içerisinde istenmeyenleri küçük diğerlerini büyük yazsın

students = ["Yuval", "Noah", "Harari", "Cem", "Say"]

students_no = ["Yuval", "Noah"]

[student.lower() if student in students_no else student.upper() for student in students]

[student.upper() if student not in students_no else student.lower() for student in students]