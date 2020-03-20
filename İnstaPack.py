import os
import time

print("""
  ____ ______     _______  _  _   
 |  _ \___ \ \   / /  __ \| || |  
 | |_) |__) \ \_/ /| |  | | || |_ 
 |  _ <|__ < \   / | |  | |__   _|
 | |_) |__) | | |  | |__| |  | |  
 |____/____/  |_|  |_____/   |_|  

Yapımcı : B3YD4
Yapım Tarihi : 06.01.2020
THT - B3YD4
Sistem Başlatılıyor...
""")

print ("[==========                    ]%0")
time.sleep(1)
print ("[===============               ]%25")
time.sleep(1)
print ("[====================          ]%50")
time.sleep(1)
print ("[=========================     ]%75")
time.sleep(1)
print ("[==============================]%100")

print("""İnstaPack UYgulamasına Hoşgeldiniz!

[1]HiddenEye(Ngrok ile Sahte Siteler Kurar)
[2]Black List(Kişiye Özel Şifre Listesi)
[3]BruteForce(Kişiye Özel Şifre Listesi İle Saldırı Yapar)
[99]Çıkış

Önemli Not!:HiddenEye programını kurmaya başladıktan sonra kurulum fazla uzun sürebilir!!

Bruteforce kullanımı : 
1-pip3 install -r requirements.txt
2- python3 instagram.py <uinstagram kullanıcı adı> <Şİfre Listesi -m 0

""")

while 99:

    dsoru = input("Hangisini İstersin? : ")

    if dsoru == "1":
        print("Kurulum Gerçekleştiriliyor...")
        os.chdir("/data/data/com.termux/files/home/")
        os.system("git clone https://github.com/DarkSecDevelopers/HiddenEye.git")

    if dsoru == "2":
        print("Kurulum Gerçekleştiriliyor...")
        os.chdir("/data/data/com.termux/files/home/")
        os.system("git clone https://github.com/BayDS/BlackList.git")

    if dsoru == "3":
        print("Kurulum Gerçekleştiriliyor...")
        os.chdir("/data/data/com.termux/files/home/")
        os.system("git clone https://github.com/Pure-L0G1C/Instagram.git")
        
    if dsoru == "99":
        print("Çıkış Yapılıyor...")
        time.sleep(2)
        quit()
        break

