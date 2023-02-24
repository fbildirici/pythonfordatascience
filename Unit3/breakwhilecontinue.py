###############################
## break & continue & while
###############################

salaries = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000]

### break ifadesi aranan koşul yakalandığında döngünün durmasını sağlar

for salary in salaries:
    if salary == 4000:
        break
    print(salary) ###4000e kadar olan maaşları listeler 4000e gelince durur

for salary in salaries:
    if salary == 4000:
        continue  ## verilen değere eşit olan 4000ü pas geçmesini sağlar
    print(salary)


## while = dığı sürece demektir
## numarayı 1 atayıp numara 5ten küçük olduğu sürece 1 ekleyip yazdıralım
## 1,2,3,4 değerlerini döndürür

number = 1
while number < 5:
    print(number)
    number += 1