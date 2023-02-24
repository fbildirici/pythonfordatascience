########################
##### Uygulama #########
########################

## divide_students fonksiyonunu yazınız
## Çift indexte olan öğrencileri bir listeye alınız.
## Tek indexte yer alan öğrencileri başka bir listeye alınız
## Fakat bu iki liste tek bir liste olarak return olsun.

students = ["Yuval", "Noah", "Harari", "James", "Jared", "Diamond"]


def divide_students(students):
    groups = [[], []]
    for index, student in enumerate(students):
        if index % 2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)
        print(groups)
        return groups


st = divide_students(students)
st[0]