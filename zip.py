#Elinizde isimlerin ve soyisimlerin bulunduğu iki tane liste olsun.
#isimler -----> ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
#soyisimler -----> ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]
#Bu isimleri ve soyisimleri sırasıyla eşleştirin ve ekrana alt alta isimleri ve soyisimleri yazdırın.
#Not: zip() fonksiyonunu kullanmaya çalışın.

isim = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
soy = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

for i,j in zip(isim,soy):
    print(i,j)