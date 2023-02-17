########################
# Karakter Dizileri (Strings)
########################

print("Academics")
print('Academics')

"Academics"

name="John"
name

#### Çok Satırlı Karakter Dizileri #####


long_str= """Veri Yapıları: Hızlı Özet
Sayılar (Numbers): int, float, complex
Karakter Dizileri (Strings): str
List, Dictionary, Tuple, Set
Boolean (TRUE-FALSE): bool"""

### Karakter Dizilerinin Elemanlarına Erişmek###

name
name[0] #pythonda karakterler sıfırla başlar, ilk harfe erişim için

name[3]

### Karakter Dizilerinde Slice İşlemi ###

name [0:2]

long_str[0:10]

long_str

"veri" in long_str

"Veri" in long_str #Case Sensitivity


##### String (Karakter Dizisi) Metodları ######
###############################################

dir(int)

dir(str)

#######len = uzunluk metodu #####################################

name = "John"
type(name)
type(len)

len(name) # 4 çıkmalı uzunluk
len("fatihbildiriciforacademia") #ctrl basıp metoda tıkladığımızda ilgili wiki dosyası açılır

###### upper-lower : kücük - büyük dönüşümleri #################

"pythonfordatascienceinacademicanalysis".upper() #tüm harfleri büyük yapar
"PYTHONFORDATASCIENCEINACADEMICANALYSIS".lower() #tüm harfleri küçük yapar

#upper ve lower class içerisinde tanımlandığı için type fonksiyonu çalışmaz ve bunlar metoddur
#class içerisinde olmayanlar fonksiyondur

### replace - karakter değiştirir #################
###################################################

hi = "Hello to Python for Data Science Course"
hi.replace("l","p")

####### hello - heppo olarak değişti ##########

############# Split - stringi böler############

"Hello to Python for Data Science".split() ###kelimeler bölünüp ayrılıyor

############# Strip - Kırpma İşlemini Yapar ###

" ofofo ".strip()     ##başındaki boşlukları kırpar ofofo
"ofofo".strip("o")    ##başta ve sondaki o harflerini kırpar fof

###### Capitalize - ilk harfi büyütür ############

"pythonforacademicdataanalysis".capitalize()

dir("pythonforacademicdataanalysis") #kullanılabilecek metodları listeler

"pythonfordatascience".startswith("o") #boolean başladığı harf, karakter kontrolü false döndü


