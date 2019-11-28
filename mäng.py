from random import *
import time
from math import *

# mängija statsid
playerHP = 20
playerSTR = 10

# mängija mant
reisipaun = []
varustus = {'mõõk' : 0, 'kilp' : 0, 'tervendav mõgin' : 6}
käed = {'paremas käes': 0, 'vasakus käes': 0}

# muu mant

mõõk = 5
kilp = 3
tolm = 0
laegas = [mõõk, kilp, tolm]

# randint eri funktsioonide tarvis

a = randint(1, 10)

# list luku-funktsiooni jaoks

nähtavad_lukud = [1]

# gaas, mis vallandub, kui eksid luku-ülesandes

def gaas():
    global playerHP
    global a
    global nähtavad_lukud
    print("Laegast kaunistavate golemite suist ja sõõrmeist immitseb lillakat gaasi.\nSul läheb silme eest mustaks ja kaotad teadvuse.")
    time.sleep(4)
    valed_vastused = 0
    playerHP -= 4
    if playerHP <= 0:
        print("Gaas mõjus sulle surmavalt.")
    else:
        print("Tõused üles, kõhus veidi keerab ja nõrk on olla. Sul on " + str(playerHP) + " elupunkti järel")
        nähtavad_lukud = [1]
        a = randint(1, 10)
    
# laekal on neli lukku, iga luku avamiseks on vaja lahendada matemaatikatehe.
# matemaatikatehe on kas liitmine, lahutamine, korrutamine, jagamine, astendamine või jäägi leidmine kahe väärtuse vahel

# funktsioon kontroll teeb luku-funktsiooni lihtsamaks
# võrdleb luku matemaatikatehte väärtust mängija vastusega.
# õige vastuse korral 'teeb järgmise luku nähtavaks', eksimuse korral kutsub esile funktsiooni gaas.
# see, mida kontroll nähtavad_lukud järjendisse lisab, pole oluline. 'a' on valitud lihtsalt selle pärast, et ta on olemas
def kontroll(vastus, a):
    if vastus == a:
        print("Õige vastus!")
        nähtavad_lukud.append(a)
    else:
        gaas()
                
def lukk():
    a = randint(1, 10)                           # a on üks kahest väärtusest matemaatikatehtes, esimene a on juhuslik. Iga järgmine a on eelmise tehte vastus.
    tehted = ['+', '-', 'x', '/', '**', '%']     # siit hulgast valib funktsioon küsimusse ühe tehte
    global nähtavad_lukud
    
    while len(nähtavad_lukud) <= 4:
        b = randint(1,10)                        # b on teine kahest väärtusest matemaatikatehtes, iga kord 1 <= b <= 10, v.a astendamistehte puhul.
        
        if playerHP == 0:                        # juhuks, kui gaas() mängija elupunktid nullitab
            break
            
        if tehted[randint(0, 5)] == '+':
            try:
                vastus = float(input("Lukul number " + str(len(nähtavad_lukud)) + " seisab: " + str(a) + " + " + str(b) + " = ?\nSina vastad: ")) 
            except:
                return
            a += b
            kontroll(vastus, a)
                
        elif tehted[randint(0,5)] == '-':
            try:
                vastus = float(input("Lukul number " + str(len(nähtavad_lukud)) + " seisab: " + str(a) + " - " + str(b) + " = ?\nSina vastad: "))
            except:
                return
            a -= b
            kontroll(vastus, a)
            
        elif tehted[randint(0,5)] == 'x':
            try:
                vastus = float(input("Lukul number " + str(len(nähtavad_lukud)) + " seisab: " + str(a) + " x " + str(b) + " = ?\nSina vastad: "))
            except:
                return
            a *= b
            kontroll(vastus, a)
            
        elif tehted[randint(0,5)] == '/' and a % b == 0:
            # teine tingimus on lisatud selleks, et lahendamine lihtsam ja ettearvatavam oleks
            try:
                vastus = float(input("Lukul number " + str(len(nähtavad_lukud)) + " seisab: " + str(a) + " / " + str(b) + " = ?\nSina vastad: "))
            except:
                return
            a /= b
            kontroll(vastus, a)
            
        elif tehted[randint(0,5)] == '**':
            b = randint(1,3)
            if a**b >= 1000:
                b -= 1
            try:
                vastus = float(input("Lukul number " + str(len(nähtavad_lukud)) + " seisab: " + str(a) + "**(" + str(b) + ") = ?\nSina vastad: "))
            except:
                return
            a **= b
            kontroll(vastus, a)
            
        elif tehted[randint(0,5)] == '%':
            vastus = float(input("Lukul number " + str(len(nähtavad_lukud)) + " seisab: " + str(a) + " / " + str(b) + " jääk = ?\nSina vastad: "))
            a %= b
            if 'ahku' in vastus:
                break
            kontroll(vastus, a)
            
    if laegas == [tolm]:
        print("Laegas avaneb, aga see on seest tühi.")
        nähtavad_lukud = [1]
        a = randint(15, 10)
    else:    
        print("Laegas avaneb ning selle põhjas seisavad sätendav mõõk ja vahva kilp. Pistad mõõga tuppe ja kilbi seljale.")
        varustus['mõõk'] = laegas.pop(0)
        varustus['kilp'] = laegas.pop(0)
        nähtavad_lukud = [1]
        a = randint(1, 10)

def dice10():
    tulemus = randint(0, 10)/10
    return tulemus

def dice6():
    tulemus = randint(1, 6)
    return tulemus     
        
def koletis():
    global playerHP
    global playerSTR
    HP = 20
    
    varustuse_järjend = []
    for asi in varustus:
        if varustus[asi] > 0:
            varustuse_järjend.append(asi)
    print("Sind ründab koletis!")
    if varustuse_järjend == []:
        print("Astud koletisele vastu paljaste kätega.\nVäljavaated pole just suurepärased.")
    else:
        haare = input("Kobad oma varustuse järgi ja leiad järgnevad esemed: " + str(varustuse_järjend)  + ". Mida soovid enesekaitseks haarata? ")
        if 'mõõ' in haare:
            käed['paremas käes'] = varustus['mõõk']
        if 'kil' in haare:
            käed['vasakus käes'] = varustus['kilp']
        if 'mõg' in haare:
            print("Mõgin sind koletise eest ei kaitse.")
            
    while True:
        tegevus = input("Mida teha soovid? Kas 'võitled', 'põgened' või 'jood' tervendavat mõginat? ")
        time.sleep(0.5)
        
        if "joo" in tegevus:
            if varustus['tervendav mõgin'] == 0:
                print("Oo ei! Mõgin on otsas.")
            else:
                playerHP += varustus['tervendav mõgin']
                varustus['tervendav mõgin'] = 0
                print("Jood ja sul on nüüd " + str(playerHP) + " elupunkti")
        
        elif "õitle" in tegevus:
            löök = round(abs(randint(0, 6) - käed['vasakus käes']))
            playerHP -= löök
            print("\nKoletis lööb sulle " + str(löök) + " punkti dämmi.\nSul säilib " + str(playerHP) + " elupunkti.")
            time.sleep(1)
            
            if playerHP <= 0:
                quit()
              
            playerLÖÖK = round(randint(0, 4) + käed['paremas käes'])
            HP -= playerLÖÖK
            print("\nLööd koletisele " + str(playerLÖÖK) + " punkti dämmi.\nKoletisel säilib " + str(HP) + " elupunkti.")
            time.sleep(1)
            
            if HP <= 0:
                print("Purustasid koletise kolju ja hukutasid ta igaveseks Tartarosse.")
                reisipaun.append('merikarp')
                print("Leiad koletise kõrva kiilunud merikarbi. Pistad igaks juhuks reisipauna\n")
                quit()
                
        elif "õgene" in tegevus:
            break

def sfinks():
    mõistatused = {'kapsas' : 'Lipp lipi peal, lapp lapi peal, ilma nõela pistma.', 'sibul' :  'Seest siiru-viiruline, pealt kulla-karvaline.', 'kurk' : 'Tare täis rahvast, ei ole ust ega akent ees?', 'humal' : 'Keerleb ja veerleb, kui otsa saab, siis muneb?'}
    vastused = list(mõistatused.keys())
    if 'merikarp' in reisipaun:
        s = 0
        print("Sfinks avab enda suu ning merikarp su paunas kumiseb.\nSa tõstad merikarbi oma kõrva äärde ning sealt kostub:")
    else:
        print("Sinu ees kõrgub müütiline Sfinks, halastamatu mõistatuseküsija. Ta avab oma suu ja sealt kostub:")
        s = randint(1,10)
    a = randint(0, 1)
    vastus = input(krüpteeri(("Mõista, mõista, mis see on! " + mõistatused[vastused[a]] + " "), s)).lower()
    if 'ahku' in vastus:
        return
    elif vastus == vastused[a]:
        print('Vastad "' + vastus + '" ja Sfinks kummardab tõrksalt, laseb su mööda, kuna vastus on sul õige.\nSfinksist mõõdudes kirgatab su ees Päikse pimestav valgus - oled vaba.')
        quit()
    else:
        print('Vastad "' + vastus + '" ja Sfinks surmab su silmapilk, kuna vastus on sul vale.')
        quit()
        
def krüpteeri(tekst, võti):
    väljund = ""
    for i in range(len(tekst)):
        sümbol = tekst[i]
        väljund += chr(ord(sümbol) + võti)
    return väljund

esimene = 0
teine = 0
kolmas = 0
while playerHP >= 0:
    if playerHP == 0:
        quit()
    if esimene == 0 and teine == 0 and kolmas == 0:
        valik = input("Sa popsatad eksistentsi toas, mille põrand on tolm ja seinadeks kivine müür.\nTuba valgustab laest langev õlilamp.\nSinu ees, paremal ja vasemal käel mustendavad portaalid.\nVasema kohal on kirjas '1', paremal '2' ja eesmisel '3'.\n'Mis siin ikka', mõtled sa ning astud läbi portaali number: ")
    
    if valik == '1':
        print("Su ees seisab laegas, millel on neli lukku.")
        time.sleep(1)
        print("Lukkude kohal on hõbedased plaadid, millel viirastuvad tabamatud numbrikombinatsioonid.")
        time.sleep(1)
        print("Vaid esimese luku plaat annab endast aimu: ")
        lukk()
    if valik == '2':
        koletis()
    if valik == '3':
        sfinks()