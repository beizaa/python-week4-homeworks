#2-)Kullanıcıdan bir input alınız. Girmiş olduğu inputta
#büyük harf sayısı, küçük harf sayısı, rakam sayısı ve
#bunların haricindeki özel karakter sayılarını veren bir program yazınız.


kelime = input("Herhangi bir kelime: ")
sayaç = ""
for ifade in kelime:
    if ifade not in sayaç:
        sayaç += ifade
for ifade in sayaç:
    print("{} ifadesi {} kelimesinde {} kez geçiyor!".format(ifade,
                                                             kelime,
                                                             kelime.count(ifade)))



#Calisiyor ama tam istenen sey degil.
