print("Hangi sayıya kadar binary ve hexadecimal degerlerin hesaplanmasini istersiniz? ")
limit=int(input())
print("Başlangıç olarak yazılmasını istediğiniz ondalık sayı aralığını giriniz")

print("Aralığın en küçük değeri girin ")
slicemin=int(input())
while (limit<slicemin):
      print("Aralığın en küçük değeri girin ")
      slicemin=int(input())
print("Aralığın en büyük değeri girin ")
slicemax=int(input())
while (limit<slicemax):
      print("Aralığın en büyük değeri girin ")
      slicemax=int(input())
      
ondalıklar=[i for i in range(1,limit+1)]
print("Ondalık Değerler")
for i in range(slicemin,slicemax+1):
      print(i)

def Binaryzation(s):
      if s>1:
            Binaryzation(s//2)
      print(s%2,end="")
      
binaryler=[]
hexalar=[]
for i in range(1,limit+1):
      binaryler.append(bin(i))
      hexalar.append(hex(i))
      
print("Binary Değerler")
for i in range(slicemin,slicemax+1):
      Binaryzation(i)
      print("")

print("Hexa Değerler")
for i in range(slicemin,slicemax+1):
      print(hex(i))

print("1 den" +str(limit) +" e tüm sayıları görmek için enterlayın")
input()

for onda,bina,hexa in zip(ondalıklar,binaryler,hexalar):
      print(str(onda)+"----"+str(bina)+"----"+str(hexa))

