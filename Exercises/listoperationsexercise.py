###list operation

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]

len(lst) ##eleman sayısı öğrenme

## sıfır ve onuncu indexteki elemanları çağır

lst[0]
lst[10]

## Verilen liste üzerinden "D","A","T","A" oluştur

dataindex = lst[0 : 4]
dataindex
## sekizinci indexteki elemanı silme

lst.pop(8)
lst ## n silindi

### listeye eleman ekleme

lst.append("academicdatascience")
lst ## string ifade liste sonuna eklendi

### sildiğimiz sekizinci sıradaki N harfini tekrar ekleyelim

lst.insert(8, "N")

lst

