import random

populasyon = []
kotuler=[]
iyiler=[]


def populasyonolustur():
    for a in range(9):
        birey = []
        for b in range(6):
            rastgelesayi=random.randint(0, 9)
            birey.append(rastgelesayi)
        populasyon.append(birey)
        print(populasyon)


def elitsecim():
    elitgen=[]
    eniyigen=0
    uygunlukdegeri=0
    global elitsayi
    for a in range(len(populasyon)):
        for b in range(len(populasyon[0])):
            uygunlukdegeri=uygunlukdegeri+populasyon[a][b]
        if(eniyigen<uygunlukdegeri):
            eniyigen=uygunlukdegeri
            uygunlukdegeri=0
            elitgen=populasyon[a]
            elitsayi=a
        else:
            uygunlukdegeri=0
    print(elitgen)
    print("En iyi kromozom uygunluk degeri: " , eniyigen)
    

def elitcikar():
    populasyon.remove(populasyon[elitsayi])
    print(populasyon)
#öncekiler 12 ve 13.07
uygunluk=[]
uygunlukliste=[]

#14.07.2020-15
def uygunlukbelirleme():
    while(len(iyiler)<4):
        
        for a in range(0,len(populasyon),2):
            uygunluk1=0
            uygunluk2=0
            for b in range(len(populasyon[0])):

                    uygunluk1+=populasyon[a][b]
                    uygunluk2+=populasyon[a+1][b]

            if(uygunluk1>uygunluk2):
                iyiler.append(populasyon[a])
                kotuler.append(populasyon[a+1])
            else:
                iyiler.append(populasyon[a+1])
                kotuler.append(populasyon[a])
        print("############")
        print("uygulukbelirleme-iyiler",iyiler)
        print("uygulukbelirleme-kotuler",kotuler)
        print("############")

    else:

        '''
        print("-")
        print("Tum populasyon: ")
        for p in range(len(populasyon)):
            ud=0
            for i in range(len(populasyon[0])):
                ud+=populasyon[p][i]
            print(populasyon[p],"uygunluk degeri:", ud)
        
        print("-")
        print("İyiler: ")
        for i in range(len(iyiler)):
            iud=0
            for ii in range(len(iyiler[0])):
                iud+=iyiler[i][ii]
            print(iyiler[i],"uygunluk degeri:", iud)
        
        print("-")
        print("Kötuler: ")
        for k in range(len(kotuler)):
            kud=0
            for ki in range(len(kotuler[0])):
                kud+=kotuler[k][ki]
            print(kotuler[k],"uygunluk degeri:", kud)
        print("-")
        '''

        for ii in range(len(iyiler)):
            iyilerud=0
            kotulerud=0
            for kk in range(len(kotuler)):
                iyilerud=0
                kotulerud=0
                for kki in range(len(kotuler[0])):
                    iyilerud+=iyiler[ii][kki]
                    kotulerud+=kotuler[kk][kki]

                if(kotulerud>iyilerud):
                    iyiler.append(kotuler[kk])
                    kotuler.append(iyiler[ii])
                    kotuler.remove(kotuler[kk])
                    iyiler.remove(iyiler[ii])

        print("***")
        print("-")
        print("İyiler: ")
        for i in range(len(iyiler)):
            iud=0
            for ii in range(len(iyiler[0])):
                iud+=iyiler[i][ii]
            print(iyiler[i],"uygunluk degeri:", iud)
        
        print("-")
        print("Kötuler: ")
        for k in range(len(kotuler)):
            kud=0
            for ki in range(len(kotuler[0])):
                kud+=kotuler[k][ki]
            print(kotuler[k],"uygunluk degeri:", kud)
        print("***")
    
#iyiler arasında caprazlama, kucuklerde de mutasyon yapılacak

def iyilericaprazla():
    gecici1=[]
    gecici2=[]
    for i in range(len(iyiler)-2):
        
        gecici1=iyiler[i][3:6]
        gecici2=iyiler[i+2][3:6]
        iyiler[i][3:6]=gecici2
        iyiler[i+2][3:6]=gecici1
    print("Caprazlama sonrası iyiler:",iyiler)

def kotulermutasyon():
    for km in range(len(kotuler)):
        a=random.randint(0,5)
        b=random.randint(0,5)
        if(a==b):
            b=(b+1)%6
        sayi1=kotuler[km][a]
        kotuler[km][a]=kotuler[km][b]
        kotuler[km][b]=sayi1
    print("Mutasyon sonrası kotuler: ",kotuler)



populasyonolustur()
elitsecim()
elitcikar()
uygunlukbelirleme()
iyilericaprazla()
kotulermutasyon()

















# her bir kumedeki sayılar toplanıp en iyi uygunluga sahip olan kume kaydedilip, digerleri caprazlamaya alinacak

























'''
gen1=[1,2,1,0,0,0]
def en iyi gen 
ilktoplam=0
for ilk in gen1:
    ilktoplam=ilktoplam+ilk
gen2=gen1
sontoplam=0
for a in range(0,len(gen2)):
    gen2[a]=random.randint(0,9)
    print(gen2[a])
    sontoplam=sontoplam+gen2[a]
if (sontoplam>ilktoplam):
    gen1=gen2

print(sontoplam)
rastgelesayi=random.randint(0,9)
print("rastgele sayi",rastgelesayi)
'''