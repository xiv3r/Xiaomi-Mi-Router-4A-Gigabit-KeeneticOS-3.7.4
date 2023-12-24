import sys
import telnetlib
import ftplib

import gateway
router_ip_address=gateway.get_ip_address()

try:	
	ftp=ftplib.FTP(router_ip_address)
except:
	print ("ftp сервер не запущен")
	print ("Запустите 1 - Connect to router ещё раз")
	sys.exit(1)
try:	
	file=open('data/x_Breed_Xiaomi_4ag.bin', 'rb')
except:
	print ("x_Breed_Xiaomi_4ag.bin не найден")
	sys.exit(1)
print ("Загружаю x_Breed_Xiaomi_4ag.bin в роутер")
ftp.storbinary(f'STOR /tmp/x_Breed_Xiaomi_4ag.bin', file)
file.close()
ftp.quit()
print ("Загрузка завершена")

tn = telnetlib.Telnet(router_ip_address)
tn.read_until(b"login:")
tn.write(b"root\n")
tn.read_until(b"root@XiaoQiang:~#")
print ("Записываю загрузчик Breed")
tn.write(b"mtd -e Bootloader write /tmp/x_Breed_Xiaomi_4ag.bin Bootloader\n")
tn.read_until(b"root@XiaoQiang:~#")
tn.write(b"reboot\n")
tn.read_until(b"root@XiaoQiang:~#")
print ("Запись загрузчика завершена")
print ("")
print ("Роутер перезапускается в загрузчик Breed, подождите 15 секунд")
print ("")
print ("Заходим в браузере по адрессу 192.168.1.1")


