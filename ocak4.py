# Kullanıcıdan 5 adet tam sayı alarak listeye ekleyen ve en büyük/en küçük sayıyı bulan program

def en_buyuk_ve_kucuk():
    sayilar = []
    
    # Kullanıcıdan 5 sayı al
    for i in range(5):
        sayi = int(input(f"{i+1}. sayıyı giriniz: "))
        sayilar.append(sayi)
    
    # En büyük ve en küçük sayıyı bul
    en_buyuk = max(sayilar)
    en_kucuk = min(sayilar)
    
    # Sonuçları ekrana yazdır
    print(f"En büyük sayı: {en_buyuk}")
    print(f"En küçük sayı: {en_kucuk}")

# Fonksiyonu çağır
en_buyuk_ve_kucuk()
