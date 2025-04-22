from colorama import Fore
import pywifi
import time
wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]
x = 0
while True:


    iface.scan()
    x = x + 1
    time.sleep(0.5)
    if x == 1:
        break
time.sleep(0.5)
print(Fore.GREEN + "=====%25=====")
time.sleep(1)
print(Fore.GREEN + "===========%50==========")
time.sleep(1)
print(Fore.GREEN + "===============%75===============")
time.sleep(1)
print(Fore.GREEN + "====================PWNED!====================")
results = iface.scan_results()


for i in results:
    
    bssid = i.bssid