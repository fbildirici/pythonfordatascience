#####################################
# Enumerate: Otomatik Counter/Indexer ile for loop
#####################################

students = ["Yuval", "Noah", "Harari", "Emrah", "Safa", "Gurkan"]

for student in students:
    print(student)

    for index, student in enumerate(students, 1):
        print(index, student)

## for ile index listesi çıkarılır, students içindeki öğrenciler 0'dan 5'e sıralanır önce index sonra öğrenci yazdırılır
## , 1 yazdığımızda 0dan değil 1den başlayarak numaralandırılır

#### bir örnek yapalım, student listesini tarasın indexte çift listede olan karakterleri
#### A listesine yazsın, olmayanları B listesine bunun için 2'ye bölünme kuralını kullanalım

A = []
B = []

for index, student in enumerate(students):
    if index % 2 == O:
        A.append(student)
    else:
        B.append(student)
    print(index, student)



