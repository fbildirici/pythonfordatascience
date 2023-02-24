#######################
# Döngüler (Loops #####
#######################

#### For Loop #########

students = ["John", "Mark", "Venessa", "Mariam"]

students[0] #students listesinden ilkini getirir
students[1] #ikinci Markı getirir

### python döngü için bir eleman ve iki döngü belirteci ister

for student in students:
    print(student)

### her öğrenci ismini büyütecek bir for döngüsü yazalım
### upper yöntemini ekliyoruz ####

for student in students:
    print(student.upper())


### maaşların olduğu bir liste verelim

salaries = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

### döngüyü yazalım salary diye çağırarak her elemanı

for salary in salaries:
    print(salary)

### maaşlara yüzde 20 zam yapacağımız bir döngü yazalım

for salary in salaries:
    print(salary*20/100 + 100)

### float değerleri integer olarak yazdıralım

for salary in salaries:
    print(int(salary*20/100 + salary))

    ## 30 yapalım

for salary in salaries:
    print(int(salary*30/100 + salary))

#### tekrar eden işler yapmamak prensibi için programlamada önemli bir nokta
#### for döngüsünü bir fonksiyonla birleştirip değişkenlerimizi, parametrelerimiz olarak ayarlayalım


def new_salary(salary, rate):
    return int(salary*rate/100 + salary)

### burada parametreleri mevcut maaş ve artış oranı olarak tanımladığımız bir fonksiyon yazdık
### zam oranının da algoritmasını return fonksiyonu içinde integer görünecek biçimde tanımladık

new_salary(1500, 10)
new_salary(2000, 30)

### burada yukarıdaki fonksiyonu esas alacak iki tane new salary örneği yazdırdık


### salaries listesi içerisinden salary değerini getirecek bir for döngüsünü vereceğimiz
### artış oranı ile yazdıralım.

for salary in salaries:
    print(new_salary(salary, 20))
## yüzde 20 artış ile tüm değerleri yazdırıyoruz.

#### başka bir listeyle çalışalım

salaries2 = [1233, 12231231, 1223, 213213, 65465, 64645, 64564, 4565, 6878, 786787]

for salary in salaries2:
    print(new_salary(salary, 15))

#### bir maaş listesinde 5000den büyük veya eşit olanlara farklı(10) küçük olanlara farklı (20) zam yapalım
### yukarıdaki şu listeyi esas alalım

salaries = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

for salary in salaries:
    if salary >= 3000:
    print(new_salary(salary, 10))
else:
    print(new_salary(salary, 20))

