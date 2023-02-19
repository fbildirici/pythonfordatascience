#### ön tanımlı default arguments/parameters#######
###################################################

def divide (a, b):
    print( a / b)

divide(1, 2)

### divide fonksiyonu içerisinde a ve b parametreleri tanımlandı
### ekrana print için a / b argümanı yazıldı
### divide 1/2 çağırılarak ekrana bölümü yazıldı

def divide (a, b=1):
    print(a / b)

divide(1)

#### b değeri default öntanımlı olarak 1 atandı ve a için değer atama gerekti sadece

############### Ne zaman fonksiyon yazılır? #############
#########################################################

### varm, moisture, charge
# örnek olarak üç farklı kaynaktan gelen değerleri inceleyelim tek tek

(56 + 15) / 80
(56 + 15) / 70
(17 + 45) / 80

###bunu tek tek yapmak yerine bir fonksiyon yazmak verimli bir yoldur
## örnek olarak

def calculate (varm, moisture, charge):
    print((varm + moisture)/charge)

    calculate(98, 12, 74)

