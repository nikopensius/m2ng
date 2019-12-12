from random import *
import time
from math import *
fail = "sätted.txt" # Failis on mängija ja vaenlaste statsid

# randint eri funktsioonide tarvis

a = randint(1, 10)

# list luku-funktsiooni jaoks

nähtavad_lukud = [1]

i = -1
tempint = 0
tempstr = ""
templs = []
m2ngija = {} 
vaenlased = {}
varustus = {}


def sätistamine(fail):
    f = open(fail)
    global i

    for rida in f:
        
        #Otsib üles tabeli pealkirja, et teada missuguste asjadega on tegemist
        if rida.strip() == "#M2ngija":
            i = 0
            continue
        if rida.strip() == "#Vaenlased":
            i = 1
            continue
        if rida.strip() == "#Varustus":
            i = 2
            continue
        
    #Võtab kõik atribuutid m2ngija tabeli all ja lisab need m2ngija sõnastikku
        if i == 0 and rida.strip() != "":
            templs = rida.strip().split(" = ")
            m2ngija[templs[0]] = int(templs[1].strip())
            
    #Võtab kõik vaenlased vaenlaste tabeli alt ja lisab need vaenlaste sõnastikku   
        if i == 1 and rida[0] == "-":
            vaenlased[rida.strip("-\n")] = {}
            tempstr = rida.strip("-\n")
    #Võtab vaenlaste atribuutid ja lisab need vaenlaste sõnastiku väärtusteks
        if i == 1 and rida[0] != "-" and rida.strip() != "":
            templs = rida.strip().split(" = ")
            vaenlased[tempstr][templs[0]] = int(templs[1])
            
    #Võtab kõik varustuse varustuse tabeli alt ja lisab need varustuse sõnastikku
        if i == 2 and rida[0] == "-":
            varustus[rida.strip("-\n")] = {}
            tempstr = rida.strip("-\n")
    #Võtab varustuse atribuutid ja lisab need varustuse sõnastiku väärtusteks
        if i == 2 and rida[0] != "-" and rida.strip() != "":
            templs = rida.strip().split(" = ")
            varustus[tempstr][templs[0]] = int(templs[1])
        

sätistamine(fail)

# muu mant
laegas = [choice(list(varustus.keys())), choice(list(varustus.keys())), "tolm"]

# mängija mant
reisipaun = [choice(list(varustus.keys()))]
käed = {'paremas käes': 0, 'vasakus käes': 0}

# mängija statsid
playerHP = int(m2ngija["HP"])
playerSTR = int(m2ngija["STR"])
playerDEF = int(m2ngija["DEF"])

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
            try:
                vastus = float(input("Lukul number " + str(len(nähtavad_lukud)) + " seisab: " + str(a) + " / " + str(b) + " jääk = ?\nSina vastad: "))
            except:
                return
            a %= b
            kontroll(vastus, a)
            
    if laegas == ["tolm"]:
        print("Laegas avaneb, aga see on seest tühi.")
        nähtavad_lukud = [1]

    else:
        mõõgapilt()
        print("Laegas avaneb ning selle põhjas seisavad " + laegas[0] + " ja " + laegas[1] + ". Sa võtad need ja pistad kotti.")
        reisipaun.append(laegas.pop(0))
        reisipaun.append(laegas.pop(0))
        nähtavad_lukud = [1]
        a = randint(1, 10)

def koletis():
    global playerHP
    global playerSTR
    global playerDEF
    vaenlane = choice(list(vaenlased.keys()))
    HP = int(vaenlased[vaenlane]["HP"])
    STR = int(vaenlased[vaenlane]["STR"])
    DEF = int(vaenlased[vaenlane]["DEF"])
    
    kollipilt()
    print("Sind ründab " + str(vaenlane))
    if reisipaun == []:
        print("Astud koletisele vastu paljaste kätega.\nVäljavaated pole just suurepärased.")
    else:
        haare = input("Kobad oma varustuse järgi ja leiad järgnevad esemed: " + str(reisipaun)  + ". Mida soovid enesekaitseks haarata? ")
        if str(haare) in reisipaun:
            if "DMG" in varustus[haare].keys():
                playerSTR += varustus[haare]["DMG"]
            if "DEF" in varustus[haare].keys():
                playerDEF += varustus[haare]["DEF"]
            if "HP" in varustus[haare].keys():
                playerHP += varustus[haare]["HP"]
                
    while True:
        tegevus = input("Mida teha soovid? Kas 'võitled', 'põgened' või 'jood' tervendavat mõginat? ")
        time.sleep(0.5)
        
        if "joo" in tegevus:
            if "HPpott" not in reisipaun:
                print("Oo ei! Mõgin on otsas.")
            else:
                playerHP += varustus[haare]["HP"]
                reisipaun.remove("HPpott")
                print("Jood ja sul on nüüd " + str(playerHP) + " elupunkti")
        
        elif "õitle" in tegevus:
            löök = round(abs(randint(0, 6) - playerDEF + STR))
            if löök <= 0:
                print("\nKoletis ei suutnud sulle haiget teha.")
            else:
                playerHP -= löök
                print("\nKoletis lööb sulle " + str(löök) + " punkti dämmi.\nSul säilib " + str(playerHP) + " elupunkti.")
            time.sleep(1)
            
            if playerHP <= 0:
                quit()
              
            playerLÖÖK = round(randint(0, 4) + playerSTR - DEF)
            if playerLÖÖK <= 0:
                print("\nSa ei suutnud koletisele haiget teha.")
            else:
                HP -= playerLÖÖK
                print("\nLööd koletisele " + str(playerLÖÖK) + " punkti dämmi.\nKoletisel säilib " + str(HP) + " elupunkti.")
            time.sleep(1)
            
            if HP <= 0:
                print("Purustasid koletise kolju ja hukutasid ta igaveseks Tartarosse.")
                reisipaun.append("merikarp")
                print("Leiad koletise kõrva kiilunud merikarbi. Pistad igaks juhuks reisipauna\n")
                break
                
        elif "õgene" in tegevus:
            break

def sfinks():
    mõistatused = {'kapsas' : 'Lipp lipi peal, lapp lapi peal, ilma nõela pistma.', 'sibul' :  'Seest siiru-viiruline, pealt kulla-karvaline.', 'kurk' : 'Tare täis rahvast, ei ole ust ega akent ees?', 'humal' : 'Keerleb ja veerleb, kui otsa saab, siis muneb?'}
    vastused = list(mõistatused.keys())
    
    sfinksipilt()
    time.sleep(1)
    
    if 'merikarp' in reisipaun:
        s = 0
        print("Sinu ees kõrgub müütiline Sfinks, halastamatu mõistatuseküsija.")
        time.sleep(1)
        print("Sfinks avab enda suu ning merikarp su paunas kumiseb.")
        time.sleep(1)
        print("Sa tõstad merikarbi oma kõrva äärde ning sealt kostub:")
    else:
        print("Sinu ees kõrgub müütiline Sfinks, halastamatu mõistatuseküsija.")
        time.sleep(1)
        print("Ta avab oma suu ja sealt kostub:")
        s = randint(1,10)
    a = randint(0, 3)
    vastus = input(krüpteeri(("Mõista, mõista, mis see on! " + mõistatused[vastused[a]] + " "), s)).lower()
    if 'ahku' in vastus:
        return
    elif vastus == vastused[a]:
        print('Vastad "' + vastus + '" ja Sfinks kummardab tõrksalt.')
        time.sleep(1)
        print("Ta laseb su mööda, kuna vastus on sul õige")
        time.sleep(1)
        print("Oled vaba!")
        time.sleep(1)
        loodus()
        time.sleep(3)
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

def koopapilt():
    print("""
#################################
#\_____________________________/#
# |            \__/           | #
# |                           | #
# |  <1>       <2>       <3>  | #
# | ,___,     ,___,     ,___, | #
# | |   |     |   |     |   | | #
# | |   |     |   |     |   | | #
# |_|   |_____|   |_____|   |_| #
# /                           \ #
#/                             \#
#################################
""")

def laekapilt():
    print("""
#################################
#    _______________________    #
#   /_____ _____ _____ _____\   #
#  /_| _ |_| _ |_| _ |_| _ |_\  #
# |  |___| |___| |___| |___|  | #
# |____V_____V_____V_____V____| #
# |                           | #
# |___________________________| #
# |                           | #
# |___________________________| #
#                               #
#################################
""")

def mõõgapilt():
    print("""
#################################
#  ___________________________  #
# || |\         _____________ | #
# || \ \       /            / | #
# ||  \ \     /    _       /  | #
# ||   \ \   /    (_)     /   | #
# ||    \_\ /            /    | #
# ||    <   >           /     | #
# ||      \_\__________/      | #
# ||__________________________| #
#                               #
#################################
""")
    
def kollipilt():
    print("""
#################################
#           _.------.           #
#          /         \_         #
#         |  O    O   |         #
#         |  .vvvvv.  |         #
#         /  |     |  |\        # 
#        /   `^^^^^'  | \       #
#      ./  /|         |\ \_     #
#     /   / |         \ /  \    #
#     \  /  |          |\   )   #
#      `'   |     Y    | ´''    #
#################################       
""")
    
def sfinksipilt():
    #credits sfinksipildi eest: https://ascii.co.uk/art/sphinx
    print("""
#################################
#        /_.    _-_           _:#
#       /:_ _ /'. .'\ ___    :__#
#      /__:_ /(|`/ !)\  /:__:__:#
#     /____ |  \ = /  |/ / /\:__#
#          `  ---  ./ / / /\    #
#           /--- -----\/ / / /  #
#          /---  ----- `/ / /   #
#        _/--- __ _/  ' `/ /    #
#      /     /XXX/     ! `/     #
#     |_|_|_|XXX|_|_|_'|_/      #
#################################
""")
    
def loodus():
    # https://www.asciiart.eu/nature/deserts
    print("""
    .    _    +     .  ______   .          .
 (      /|\      .    |      \      .   +
     . |||||     _    | |   | | ||         .
.      |||||    | |  _| | | | |_||    .
   /\  ||||| .  | | |   | |      |       .
__||||_|||||____| |_|_____________\__________
. |||| |||||  /\   _____      _____  .   .
  |||| ||||| ||||   .   .  .         ________
 . \|`-'|||| ||||    __________       .    .
    \__ |||| ||||      .          .     .
 __    ||||`-'|||  .       .    __________
.    . |||| ___/  ___________             .
   . _ ||||| . _               .   _________
_   ___|||||__  _ \\--//    .          _
     _ `---'    .)=\oo|=(.   _   .   .    .
_  ^      .  -    . \.|
""")

esimene = 0
teine = 0
kolmas = 0
while playerHP >= 0:
    if playerHP == 0:
        quit()
    if esimene == 0 and teine == 0 and kolmas == 0:
        koopapilt()
        time.sleep(1)
        print("Sa popsatad eksistentsi toas, mille põrand on tolm ja seinadeks kivine müür.")
        time.sleep(1)
        valik = input("Sinu ees seisab kolm ust. Trüki number, mitmendasse astuda soovid: ")
    
    if valik == '1':
        laekapilt()
        time.sleep(1)
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