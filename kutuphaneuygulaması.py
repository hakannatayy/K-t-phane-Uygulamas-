kitapListesi = list() 

menu = """
[1] Kitap Ekle
[2] Kitap Çıkar
[3] Kitapları Listele
[Q] Çıkış
"""

def kitapEkle(kitap,liste):
    liste += [kitap]
    print("Kitap Eklendi.")
    input("Ana Menüye dönmek için 'enter'e basın!")

def kitapCikar():
    pass

def listele(liste):
    for i in liste:
        print("Kitap Adı ---------->>>> {}".format(i))
    input("Ana Menüye dönmek için 'enter'e basın!")

def cik():
    return quit()

def cik():
    quit()

while True:
    print(menu)

    secim =input("Seçiminiz: ")

    if secim=="1":
        kitapAdi=input("Kitap Adı: ")
        kitapEkle(kitapAdi,kitapListesi)

    elif secim=="2":
        kitapCikar()

    elif secim=="3":
        listele(kitapListesi)

    elif secim=="q" or "Q":
        cik()

    else:
        print("Hatalı Girdiniz!")
        input("Ana menuye dönmek için 'enter'e basın!")