#### List & Dict Comprehension ####

### bir veri setindeki değişken isimlerini değiştirmek

#before
# ['total', 'speeding', 'alcohol', 'not_distracted', 'no_previous', 'ins_premium', 'ins_losses', 'abbrev']

#after
# ['TOTAL', 'SPEEDING', 'ALCOHOL', 'NOT_DISTRACTED', 'NO_PREVIOUS', 'INS_PREMIUM', 'INS_LOSSES', 'ABBREV']

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

##burada bir modulden gitti column verilerini aldık

for col in df.columns:
    print(col.upper())

    ## burada gittik bu değerleri büyüttük

A = []

for col in df.columns:
    A.append(col.upper()

df.columns = A

df = sns.load_dataset("car_crashes")
    ## bunları bir listeye kesin bir şekilde atayalım
