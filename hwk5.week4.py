#5-)Futbolcular dosyasındaki futbolcu isimlerini yazdığınız program ile
#Türkçe karakter içermeyecek bir hale getirip yeni bir dosyaya kaydediniz.


kaynak = "şçöğüıŞÇÖĞÜİ"
hedef = "scoguiSCOGUI"
with open("futbolcular.txt", "r+") as f:
    veri = f.read()
    print(veri)
    çeviri_tablosu = str.maketrans(kaynak, hedef)

    print(veri.translate(çeviri_tablosu))
    f.write(veri.translate(çeviri_tablosu))
