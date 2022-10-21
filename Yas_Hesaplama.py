import datetime
simdiki_zaman= datetime.datetime.now()
simdiki_yıl=datetime.datetime.strftime(simdiki_zaman,'%Y')
while True:
 def yasHesapla(dogumyili):
    return int(simdiki_yıl)-dogumyili  
 yıl=int(input("Lütfen doğum yılınızı giriniz:"))
 name=str(input("Lütfen isminizi giriniz:"))
 gender=str(input("Lütfen cinsiyetinizi giriniz:"))
 date=yasHesapla(yıl)
 if gender=="Erkek":
      appeal='Bey'   
 else:
    appeal='Hanım'
 print(f"Merhabalar {name} {appeal} .Yaşınız {date}")