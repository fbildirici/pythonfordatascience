print ("Hello World")

##############################
# sayılar numbers ve karakter dizileri strings
##############################

#integer
print(9)

#float
9.2

#veritipibulma

type(9.2)

################################
#Atamalar ve Değişkenler (Assignment and Variables)
################################

b = "hello ai era"

a= 9
c= 17

a*c


################################
#Virtual environment - sanal ortam ve package management - paket yönetimi
################################

#conda env list - listing environments

#sanal ortam oluşturma:
# conda create -n firstvirtualenv

#sanal ortamı aktif hale getirme çalışmak için
#conda activate firstvirtualenv
#içerik kontrolü: conda list (paket,kütüphane vs.)

#paket yükleme - conda install numpy

#çoklu paket yükleme environment içinde - conda install numpy scipy pandas

#paket silme conda remove packagename

#belirli bir versiyona göre paket yükleme - conda install numpy=1.20.1

#conda upgrade numpy - tek paketin en güncelini yükleme

#conda upgrade all - tüm yüklü paketleri en güncele çekme

#pip ile çalışma (python package index)

#paket yükleme
# pip install paket_adi ör: numpy
# pip install pandas==1.2.1 --> spesifik versiyona göre paket yükleme

#ortamı ve bağımlılıkları export etme conda env export > environment.yaml

#ortamdan çıkma conda deactivate
#ortamı silme conda remove -n deneme(envname)

#yaml ile environmentın kopyasını oluşturma conda env create -f environments.yaml




