###
## numpy - pandas - data visualization - gelişmiş keşifçi fonksiyonel

## numpy
## neden numpy? numpy array oluşturmak ve işlemler

import numpy as np

a = [1, 2, 3, 4]
b = [2, 3, 4, 5]

## klasik yolla bu iki liste elemanlarını çarpalım

ab = []

for i in range(0, len(a)):
    ab.append(a[i] * b[i])


## numpy ile yazalım

a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])

a*b

### böylece döngü vs yazmadan numpy array kullanarak işlem yaptık