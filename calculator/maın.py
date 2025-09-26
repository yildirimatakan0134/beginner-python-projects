print("""
[1]Toplama
[2]Cıkartma
[3]Carpma
[4]Bölme
[5]Üs alma

""")

secim = input("seciminizi giriniz: ")
if secim == "1":
    sayi1 = float(input("birinci sayıyı giriniz: "))
    sayi2 = float(input("ikinci sayıyı giriniz: "))
    print("sorunun cevabı: " , sayi1  + sayi2)

elif secim == "2":
    sayi1 = float(input("birinci sayıyı giriniz: "))
    sayi2 = float(input("birinci sayıyı giriniz: "))
    print("sorunun cevabı: " , sayi1 - sayi2)

elif secim == "3":
    sayi1 = float(input("birinci sayıyı giriniz: "))
    sayi2 = float(input("birinci sayıyı giriniz: "))
    print("sorunun cevabı: " , sayi1 * sayi2)

elif secim == "4":
    sayi1 = float(input("birinci sayıyı giriniz: "))
    sayi2 = float(input("birinci sayıyı giriniz: "))
    print("sorunun cevabı: " , sayi1 / sayi2)

elif secim == "5":
    sayi1 = float(input("birinci sayıyı giriniz: "))
    sayi2 = float(input("birinci sayıyı giriniz: "))
    print("sorunun cevabı: " , sayi1 ** sayi2)

else:
    print("lütfen yukarıda belırtılen sayılardan bır tanesını gırınız")
    