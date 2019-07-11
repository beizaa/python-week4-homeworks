#3-)Kullanıcıdan bir input alınız. Girmiş olduğu
#inputtaki rakamların toplamını veren bir program yazınız.
#(Kullanıcı rakam girmek zorunda değil.
#farklı karakter girişi de yapabilir.)
#Örnek input = "art12kl4*"



girdi=input("bir seyler yazin.")
harfler_isaretler = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM~!@#$%^&*()_+{}:<>?`,./;'[]\|=-" 
yeni_girdi = ""
for i in girdi:
    if not i in harfler_isaretler:
        yeni_girdi += i
print(yeni_girdi)
for i in yeni_girdi:
    yeni_girdi +=i
print(yeni_girdi)

for n in yeni_girdi:
    print(int(n+n))      #bu toplama islemi bolumunu yapamadim

#yanlis calisiyor


#YA DA
birseyler=input("Bir seyler yazin:")
def findSum(birseyler): 
  
    buraya = ""
    Sum = 0
  
for i in birseyler:
    if (i.isdigit()):
        buraya += i  
    else:  
        Sum += int(buraya)  
        buraya = "0"
         
print(findSum(birseyler))

#kaynaklardan anladigim kadariyla boyle bir alternatif var ama bu da calismiyor.
