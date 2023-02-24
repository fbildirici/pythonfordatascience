####Practice####

### Aşağıdaki şekilde string değiştiren bir fonksiyon yazmak isteyelim

### before : "hi my name is fatih and im learning in python for data science for academic research"
### after  "Hi mY NaMe iS FaTiH aNd Im LeArNiNg In PyThOn FoR dAtA sCiEnCe FoR aCaDeMiC rEsEaRch"

### buraya baktığımızda yöntem olarak şöyle birşey çıkacak önümüze
### stringin içerisinde gezeceğiz indexte tek ve çift karakterlere operasyon uygulayacağız
### onu da bir yere kaydedeceğiz : ör: new_string değişkeni

### hatırlayalım
### boyut bilgisi öğrenme

len("pythonfordatascience")
range(len("pythonfordatascience")) ## 0,20 0dan20ye kadar karakterleri gezdi

range(0, 20) ## aynı sonucu böyle de alabiliriz
"pythonfordatascience"[9] ##index listesinden seçme

### buradaki her indexi teker teker gezecek bir for döngüsü yazalım

for i in range(len("pythonfordatascience")):
    print(i) ### 0dan başlayıp 19a kadar (toplam 20) indexi listeledi bunu aşağıya uygulayalım
    ## new stringe değerleri kaydedeceğiz gerisini burada gördük



def alternating(string):
    new_string = ""
    ## girilen stringin indexlerinde gez
    for string_index in range(len(string)):
      if string_index % 2 == 0:
          ##index çift ise harfleri büyük yap
        new_string += string[string_index].upper()
      else:
        new_string += string[string_index].lower()
            ## index küçük ise harfleri küçük yap
    print(new_string)
    ### ekrana indexin bulunduğu stringi yazdır

alternating("python") ### tanımlanan fonksiyonu şu stringi baz alarak uygula
alternating("hi my name is fatih and im learning in python for data science for academic research")


