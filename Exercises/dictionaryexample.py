#### dictionary#####
####################

dict = {'Christian' : ["America", 18],
          'Daisy' : ["England", 12],
         'Yuval' : ["Israel", 22],
          'Dante' : ["Italy", 22]
        }

######## key değerlerine erişelim

dict.keys() ##key isimlerini verir

##### value değerlerine erişelim

dict.values() ##keye karşılık gelen değerleri verir

### bir keydeki değeri güncellemek
dict.update({ 'Daisy' : ["England", 13]})

dict

###  Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz

dict.update({'Ahmet' : ["Turkey", 24]})
dict

## Antonio'yu dictionary'den siliniz

dict.pop("Antonio")
dict ##pop delete komutu

