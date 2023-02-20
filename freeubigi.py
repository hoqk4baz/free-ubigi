import requests
import json, time
import random
import os, sys


harf="abcdefghijklmnoprstuvyz"
rakam="0123456789"

karistir=harf + rakam
uzunluk=10
uzunluk2=6
ksonuc="".join(random.sample(karistir,uzunluk))
ksonuc2="".join(random.sample(karistir,uzunluk2))
ksonuc3="".join(random.sample(karistir,uzunluk2))





print("  _____             _      ______                ")
print(" |  __ \           | |    |  ____|               ")
print(" | |  | | __ _ _ __| | __ | |__   _ __  ______ _ ")
print(" | |  | |/ _` | '__| |/ / |  __| | '_ \|_  / _` |")
print(" | |__| | (_| | |  |   <  | |____| | | |/ / (_| |")
print(" |_____/ \__,_|_|  |_|\_\ |______|_| |_/___\__,_|")
print(" ‎Merhaba! Ben Python kullanıyorum.  TG: dark_enza")
print("")
print("Kodun Çalışması için Ubigi ağında olmalısın")
print("**eSIM'i yenilediyseniz Kodu Kapatın")
print("Ardından Lütfen Şu komutu kullanın!")
print("Komut: rm -r userid.txt")
print("Koddan Çıkmak İçin CTRL + c veyahut ^c yapınız")





if os.path.isfile('userid.txt'):
	with open('userid.txt', 'r') as r:
		data = r.readlines()
		user = str(data[0])
		
		url2="https://ubigi.me/scapi/lines/"+user+"/subscriptions"
		headers2={
			"Host": "ubigi.me",
			"Origin": "ionic://ubigi.me",
			"Content-Type": "application/json",
			"Accept": "application/json",
			"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
			"Pragma": "no-cache",
			"Connection": "keep-alive",
			"Content-Lenght": "269",
			"Accept-Encoding": "gzip",
			}
		data2="""{"productId":"WW_901O_STACK_ONEOFF_EU_1GB_30D","source":"SFC_APP","paymentProvider":"external","parentSubscriptionId":null,"shopperPaymentMethodRef":null,"template":{"reference":"UBI-APP","locale":"en_US"},"voucherCode":null}"""
		
		headers2["Content-Length"]=str(len(data2))
		res2=requests.post(url2,headers=headers2,data=data2)
		while True:
			try:
				sonuc55=res2.json()["paymentKey"]["customerId"]
				print("[=]Bağlantı Açıldı[=]")
				time.sleep(40)
				if res2.status_code == 200:
					print("[=]Bağlantı Başarılı[=]")
				else:
					print("[=]Bağlantı Başarısız[=]")
			except:
				print("Kota Doldu Bağlanılamıyor")
		
			
else:
	url1="https://ubigi.me/scapi/accounts"
	headers1={
		"Host": "ubigi.me",
    "Origin": "ionic://ubigi.me",
    "Content-Type": "application/json",
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
    "Pragma": "no-cache",
    "Connection": "keep-alive",
    "Content-Lenght": "269",
    "Accept-Encoding": "gzip",
	}
	data1={"password":"adebb65e40fac0d2a23fdb37e13428bf","email":ksonuc+"@dark-enza.club","firstName":ksonuc2,"lastName":ksonuc3,"countryOfResidence":"TR","language":"en-US","source":"SFC_APP"}
	headers1["Content-Length"]=str(len(data1))
	res1=requests.post(url1,headers=headers1,json=data1)
	try:
		sonuc1=res1.json()["slrId"]
		with open('userid.txt', 'w') as a:
			a.write(str(sonuc1))
		print("")
		print("")
		print("User ID Çekildi Kodu Yeniden Başlat")
	except:
		print("")
		print("")
		print("User ID Çekilemedi")
		print("Muhtemelen Ubigi ağında değilsin")
		print("Veyahut Wifi ile Kodu Çalıştırıyorsun")
		print("Veyada Ubigi ağındasın fakat userid.txt")
		print("Dosyasını silmiş olabilirsin")
		print("Unutma rm -r userid.txt Ubigiyi kullanıp")
		print("Yeni eSIM aldığında kullanılması gerekir")
		raise SystemExit()
