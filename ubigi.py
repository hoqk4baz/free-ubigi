import requests
import json, time
import random


harf="abcdefghijklmnoprstuvyz"
rakam="0123456789"

karistir=harf + rakam
uzunluk=10
uzunluk2=6
ksonuc="".join(random.sample(karistir,uzunluk))
ksonuc2="".join(random.sample(karistir,uzunluk2))
ksonuc3="".join(random.sample(karistir,uzunluk2))



print("""
________              ______              
___  __ \_____ __________  /__ 
__  / / /  __ `/_  ___/_  //_/ 
_  /_/ // /_/ /_  /   _  ,<   
/_____/ \__,_/ /_/    /_/|_|""")
print("")

print("                        ENZA")

print("T4KL!TL3R 4SL1N1 YÜC3LT!R mOrUq")
print("")



print("TG Channel: @dwstoree")
print("TG: @dark_enza")
print("")



print("Ubigi VPN'siz Free İnternet")
print("🇹🇷Lütfen Sadece Ubigi ağında kullanın ")
print("🌍Only Use Ubigi Network 📶")
print("")
time.sleep(2)
headers = {
			"Host": "ubigi.me",
			"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
			"Content-Type": "application/json"
			}
	
print("[+]Üyelik Kontrolu Yapılıyor")

#---- kullanıcı kaydı yapılır
#---- Eğer kullanıcı ztn kayıtlıysa esgeçilir
url1="https://ubigi.me/scapi/accounts"

data1={"password":"adebb65e40fac0d2a23fdb37e13428bf","email":ksonuc+"@dark-enza.club","firstName":ksonuc2,"lastName":ksonuc3,"countryOfResidence":"PK","language":"en-US","source":"SFC_APP"}
res1=requests.post(url1,headers=headers,json=data1)
try:
	kayıt = res1.json()["slrId"]
	print("[+]Kayıt Yapıldı")
except:
	print("[+]Kullanıcı kayıtlıymış")


#----- kullanıcı id çeker
url = "https://ubigi.me/scapi/accounts/me"
res = requests.get(url, headers=headers)
try:
	user = res.json()["slrId"]
	print("[+]Userid Çekildi")
	print("")
except:
	print("[-]Ubigi ağında değilsin !!")
	print("[-]Sadece Ubigi ağı Wifi kullanma !")
	raise SystemExit()

#----- internet erişimini açar
url2="https://ubigi.me/scapi/lines/"+str(user)+"/subscriptions"
data2="""{"productId":"WW_901O_STACK_ONEOFF_EU_1GB_30D","source":"SFC_WEB","paymentProvider":"external","parentSubscriptionId":null,"shopperPaymentMethodRef":null,"template":{"reference":"UBI-APP","locale":"en_US"},"voucherCode":null}"""

res2=requests.post(url2,headers=headers,data=data2)

while True:
	try:
		istek = res2.json()["paymentKey"]["customerId"]
		if res2.status_code == 200:
			print("[+]Bağlantı Başarılı[+]")
			time.sleep(60)
	except:
		print("[-]Kota Doldu Bağlanılamıyor")
		raise SystemExit()
