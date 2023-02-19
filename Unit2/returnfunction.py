#################################
###Return: Fonksiyon Çıktılarını Girdi Olarak Kullanmak###
#################################

def calculate(varm, moisture, charge):
    print((varm + moisture)/charge)

calculate(98, 12, 78) * 10

### burada nonetype ve initi çarpmıyor calculate işlemi için
### o yüzden çıktıyı çarpmak için return olarak gerçekleştirelim işlemi

def calculate(varm, moisture, charge):
    return (varm + moisture)/charge

calculate(98, 12, 78) * 10

##### burada return komutunu görünce işlem duruyor, calculate ile returnde çıkan veri tutulup
##### nonetype olsa da 10 int ile çarpılıp sonuç döndürülüyor

def calculate(varm, moisture, charge):
    varm = varm * 2
    moisture = moisture * 2
    charge = charge * 2
    output = (varm + moisture) / charge

    return varm, moisture, charge, output

type(calculate(98, 12, 78))

### tuple demet sınıfında olan  (196, 24, 156, 1.4102564102564104)
### sonucunu döndürür

varm, moisture, charge, output = calculate(98, 12, 78)

### 4 tane değişken atadı ör: varmı çalıştırırsak fonksiyon gereği gidip 2 ile çarpıp 196 döndürecek




##############################################################
###### Fonksiyon İçerisinden Fonksiyon Çağırmak ##############


def calculate(varm, moisture, charge):
return (varm + moisture) / charge

calculate(90, 12, 12) * 10

##### değerin integer olmasını istersek

def calculate(varm, moisture, charge):
return int ((varm + moisture) / charge)

calculate(90, 12, 12) * 10

#### ek bir fonksiyonda işlem yapalım

def standardization (a, p):
    return a * 10 / 100 * p * p

standardization(45, 1)

#########################
# yeni bir fonksiyon içerisinde bulunan argümanlar çağıracaksa ana fonksiyonu tanımlarken
# kullanılan argümanlar dışarıdan biçimlendirildiği notate edilecek şekilde yazılmalıdır
# örnek olarak all_calculation isimli bir ana fonksiyon tanımlayıp
# iki fonksiyondaki argümanları da oradan çağıralım.
#########################

def all_calculation (varm, moisture, charge, p):
    a = calculate(varm, moisture, charge)
    b = standardization(a, p)
    print(b * 10)

all_calculation(1, 3, 5, 12)


def all_calculation (varm, moisture, charge, a, p):
    print(calculate(varm, moisture, charge))
    b = standardization(a, p)
    print(b * 10)

all_calculation(1, 3, 5, 19, 12)






#################################################
###############Local & Global Variable ##########
#################################################

list_store = [1, 2]
type (list_store)

   def add_element(a, b):
       c = a * b
       list_store.append(c)
       print(list_store)

add_element(1, 9)

### sonuç olarak 1,9 arasına 1*2 sonucu olan 2 değeri list_store.append ile eklenir

