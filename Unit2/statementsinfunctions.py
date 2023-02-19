##########Fonksiyonlarda statement/body bölümü#########
#######################################################

###fonksiyon tanımı:
### def function_name (parameters_arguments):
###     statements (function body)
##################################

def say_hi ():
    print("Merhaba")
    print("Hi")
    print("Hello")

#function ve body tanımlandığı say hi çağırdığında ilgili değerler gelecek

say_hi()

##### say hi için bir tipte örnek tanımlama mesela string tipi

def say_hi (string):
    print(string)
    print("Hi")
    print("Hello")

    ### ilk satıra string bir değer isteyecek

say_hi("academicdatascience ")

### ilk satırda girdiğimiz bu string değeri getirmeli

def multiplication(a,b):
    c= a*b
    print(c)

multiplication(10, 8)

##multiplication işlemi ve c parametresinde a*b argümanı tanımı

#### girilen değerleri bir liste içerisine saklayan fonksiyon

list_store = []

def add_element(a, b):
    c = a * b
    list_store.append(c)
    print(list_store)

## list store listesi tanımladı add_element fonksiyonu içerisinde
## a ve b argümanları tanımlandı, append ile listeye eleman eklenir
## print ile list store ekrana yazdırılır, liste elemanları için ise add_element çağrılır

add_element(1, 8)
add_element(18, 8)
add_element(180, 10)

## değerler c= a*b fonksiyon atamasında gösterildiği gibi çarpılarak liste içine yazılır

