#############################
# - Fonksiyonlar
# - Döngüler
# - Koşullar
# - Comprehensions
##############################

######### Fonksiyon Okuryazarlığı ####

print("a")
?print #<built-in function print> bir fonksiyondur atanan değerler argüman, atandığı değerler
#parametre

print("a", "b")

#sep parametresi örneğin değerler arasına karakter yerleştirir

print("a", "b", sep="__")
## a__b çıktısını verir

#consoleda fonksiyonlara ilişkin işlemler için
# help(print) örneğin komutuyla işlemler alınır.

######## Fonksiyon Tanımlama ##################

def calculate(x):
    print(x*2)

### calculate fonksiyonu tanımladık ve bu fonksiyona x çarpı 2 argümanını yazdık

calculate(5)
#dediğimizde 2 ile çarpan calculate fonksiyon sonucunu getiriyor

## iki argümanlı / parametreleri bir fonksiyon tanımlama #########

def summer(arg1, arg2):
    print(arg1 + arg2)

    summer(7, 8)

##arg1 , arg2 argümanları tanımlandı, fonksiyon olarak toplam fonksiyonu verildi
# bu fonksiyon değerleri summer fonksiyonu içerisinde çağrılınca çağrılan değerler toplanıp 15 çıktı.

summer(8, 7)



################################
#########DOCSTRING##############
################################
### argüman içerisine üç tırnak """""" açıp entera basarak doc
### settingsden docstrings için google seçilip yeniden konfigürasyonla yaratıldı
def summer(arg1, arg2):
    """
    Sum of two numbers
    Args:
        arg1: int, float
        arg2: int,float

    Returns: int, float

    """
    print(arg1 +arg2)

#### consoledan help(argumen) ile detaylı bilgiler görülüp içerisine clean code için daha detaylı bilgi yazılabilir.



