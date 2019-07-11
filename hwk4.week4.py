#4-)Futbolcular dosyasındaki futbolculardan
#ismi sesli harf ile başlayanları ayrı bir dosyaya yazdırınız.


with open("futbolcular.txt", "r+") as f:  #veriyi alacagimiz zaten varolan dosya
    veri=f.read()

sesli_harfler="aeıioöuü"                  #sesli harfler
sesli_futbolcular= ""                     #sesli harfle baslayan futbolcular listesine bir deger atadik
for i in "futbolcular.txt":               #dosyadaki bir oge
    if i.startswith(sesli_harfler)== True:#sesli harf ile basliyorsa
        sesli_futbolcular +=i             #atadigimiz degere ekle
fs = open("sesli_harfli_futbolcular,txt", "w") #sesliler icin yeni bir dosya ac 
fs.write(sesli_futbolcular)               #ve buraya yaz

fs.close()


#program calismiyor
