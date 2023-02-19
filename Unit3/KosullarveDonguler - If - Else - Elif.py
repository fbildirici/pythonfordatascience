#################################
###Kosullar (Conditions) ########
#################################

#### True-False ile başlayalım ##

1 == 1
1 == 2

## if

if 1 == 1:
    print("something")

### if koşulu sağladığı için ekrana something yazılır

if 1 == 2:
    print("something")

## sonuç döndürmez , aşağıdaki şekilde deneyelim

number = 11

if number == 10:
    print("number is 10")

### number değeri 11 olduğu için kontrol eder 10u yanlışlar ve sonuç döndürmez

number = 10
number = 20

def number_check(number):
    if number == 10:
        print("number is 10")

number_check(10)
number_check(12)

### numara tanımladık, number check fonksiyonu ile if koşulu tanımladık
### o fonksiyonun numarayı sağladığı durumda yazdırılır, yoksa boş döner

############## Yengeye Else İf Dedin Usta ###########################
##################### ELSE & Elif ###################################



def number_check(number):
    if number == 10:
        print("number is 10")

number_check(10)

#### 10 olduğu için dolu , olmasa boş çıkarır
#### else ile koşullu durum ekleyelim

def number_check(number):
    if number == 10:
        print("number is 10")
    else:
        print("number is not 10")

number_check(11)

#### numara 11 olduğu için else printini döndürür

###### elif ########
###### birden fazla koşulun olduğu doğru durumlarda kullanılır###
##### else yanlış durumda ####

def number_check(number):
    if number > 10:
        print("number is greater than 10")
    elif number < 10:
        print("number is less than 10")
    else:
        print("number is equal to 10")

number_check(12)
number_check(6)
number_check(10)

