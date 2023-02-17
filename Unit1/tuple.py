#####################################
##Demet (Tuple)######################
#Değiştirilemez, Sıralıdır, Kapsayıcıdır

t=("Python", "ML", 1, 2)
type(t)

t[0]
#tuple içerisindeki ilk elemanı getirir

t[0:3]
#ilk 3 elemanı bölüp getirir

t[0] = 99
#değiştirilemez olduğu için ilk eleman olarak 99 atanamaz, hata döner
# bunun için tupleı list yapıp, elemanı ekleyip tekrar tuplea çevirmek gerekir
# tuple daha güvenli bir yöntemdir o nedenle böyle caselerde kullanılır

t = list(t)
t[0]=99
t= tuple(t)
t

# 99 böylece t tupleından üretilmiş t listesine eklenir

