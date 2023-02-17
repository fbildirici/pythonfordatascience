############## Liste (List) #######################

# - Değiştirilebilir
# - Sıralıdır. Index işlemi yapılabilir
# - Kapsayıcıdır

notes = [1, 2, 3, 4]
type (notes)
##notes isimli bir liste oluşturup tipini görme

names = ["a", "b", "v"]
names = ["a", "b", "v", "d"]

not_name = [1, 2, 3, "a", "b", "v", True, [1,2,3]]

not_name[0]
not_name[5]
not_name[7]

#7.karakterdeki liste tek bir liste olarak ele alınır

notes[0] = 99
notes #ilkkarakteri 99 ile değiştirecek

not_name[0:4] #diziyi böler

dir(notes)
##liste için kullanılabilecek metodlar

###len metodu uzunluk################

len(notes)
len(not_name)

######append = kelime ekler##########

notes
notes.append(100)
notes

#diziye 100 elemanını ekledi

####### pop: indexe göre siler #########

notes
notes.pop(0) #ilk elemanı siler
notes

######### insert: indexe göre ekler ######

notes.insert(2, 128) #2ci argümanı 128 ekler
notes

