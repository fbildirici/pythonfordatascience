###############SET##################
### Değiştirilebilir, Sırasız + Eşsizdir, Kapsayıcıdır
####################################

set1 = set([1, 3, 5])
set2 = set([1, 2, 3])

type(set1)

#### Set1'de olup Set2'de Olmayanlar ####

set1.difference(set2) #5 değeri döner

set2.difference(set1) #2 değeri döner

###### symmetric_difference = iki kümede de birbirine göre olmayanlar ######

set1.symmetric_difference(set2) #2,5 dönecek

######### intersection (iki kümenin kesişimi) ##########

set1.intersection(set2) #1,3 değerleri dönecek

set1-set2 #(difference döndürür)

########### union - iki kümenin birleşimi ##############

set1.union(set2) #tüm elemanları toplar birleştirir

######### isdisjoint? - iki kümenin kesişimi boş mu? ortaklık kontrol etme #########

set1.isdisjoint(set2) #boş olmadığı için false döner

set1 = set([7, 8, 9])
set2 = set([5, 6, 7, 8, 9, 10])

set1.isdisjoint(set2)
set2.isdisjoint(set1)

#### issubset - bir küme diğerinin alt kümesi mi################

set1.issubset(set2) #true dönecek
set2.issubset(set1) #false dönecek

##### issuperset - bir küme diğerini kapsıyor mu ############

set1.issuperset(set2) #false
set2.issuperset(set1) #true

