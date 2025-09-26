def ikramiye_gir():
    ad = input("Çalışan ad: ")
    soyad = input("Çalışan soyad: ")
    ikram1 = input("Yaz ikramiyesi: ")
    ikram2 = input("Kış ikramiyesi: ")
    with open("ikramiye yonetım/calısanlar.txt", "a", encoding="utf-8") as file:
        file.write(ad + " " + soyad + ":" + ikram1 + "," + ikram2 + "\n")

def ort_ikramiye(satir):
    new_satir = satir.strip()
    liste = new_satir.split(":")
    calısanlar = liste[0]
    ikramiyeleri = liste[1]

    ikram1, ikram2 = map(int, ikramiyeleri.split(","))

    ortalama = (ikram1 + ikram2) / 2
    if 7000 <= ortalama <= 10000:
        duzey = "iyi calısan"
    elif 5000 <= ortalama < 7000:
        duzey = "orta calısan"
    else:
        duzey = "kotu calısan"

    return calısanlar + ": " + duzey + "\n"

def ikramiye_oku():
    with open("ikramiye yonetım/calısanlar.txt", "r", encoding="utf-8") as file:
        for satir in file:
            print(ort_ikramiye(satir))

def ikramiye_kaydet():
    with open("ikramiye yonetım/calısanlar.txt", "r", encoding="utf-8") as file:
        liste = [ort_ikramiye(i) for i in file]

    with open("ikramiye yonetım/ikramdurum.txt", "w", encoding="utf-8") as file2:
        file2.writelines(liste)

# Menü
while True:
    print("****** Menu ******")
    islem = input("1- İkramiye gir \n2- İkramiye oku\n3- İkramiye kaydet\n4- Çıkış\n")

    if islem == "1":
        ikramiye_gir()
    elif islem == "2":
        ikramiye_oku()
    elif islem == "3":
        ikramiye_kaydet()
    elif islem == "4":
        break
    else:
        print("Geçersiz seçim!")
