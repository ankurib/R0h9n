#Itzz Rohan Singh 
#It's A Tool For Send Comments To Any Post
#Let's Start With Rohan 
from platform import system
import sys
def testPY():
    if(sys.version_info[0] < 3):
        print ('\n\t [+] You have Python 2, Please Clear Data Termux And Reinstall Python ... \n')
        sys.exit()
        #Agya Madarchod Copy Past Kr Ne 
#Tohar Maya Ke Sanga Chor Madarchod
#Kr Le Copy Mera Loda Auqhad Lega Ky Tu


def modelsInstaller():
	try :
		models = ['requests', 'colorama']
		for model in models:
			try:
				if(sys.version_info[0] < 3):
					os.system('cd C:\Python27\Scripts & pip install {}'.format(model))
				else :
					os.system('python -m pip install {}'.format(model))
				print (' ')
				print (' [+] {} has been installed successfully, Restart the program.'.format(model))
				sys.exit()
				print (' ')
			except:
				print (' [-] Install {} manually.'.format(model))
				print (' ')
	except:
		pass
#Samja Ata Bhi Python Jo Chala Tool Bana Ke 
#Decode To Kr Leya Ab Mera Loda Chuss Lechor

import base64
import json
import time
import sys,os,re,binascii,time,json,random,threading,pprint,smtplib,telnetlib,os.path,hashlib,string,glob,sqlite3,urllib,argparse,marshal
from platform import system
from datetime import datetime

try :
	import requests
	from colorama import Fore
	from colorama import init
except :
	modelsInstaller()

requests.packages.urllib3.disable_warnings()

def cls():
	if system() == 'Linux':
		os.system('clear')
	else:
		if system() == 'Windows':
			os.system('cls')
cls()
CLEAR_SCREEN = '\033[2J'
RED = '\033[31m'   # mode 31 = red forground
RESET = '\033[0m'  # mode 0  = reset
BLUE  = "\033[34m"
WHITE = "\u001b[37m",
YELLOW = "\u001b[33;1m",
CYAN  = "\033[36m"
MAGENTA = "\u001b[35m",
GREEN = "\033[32m"
RESET = "\033[0m"
BOLD = '\033[1m'
REVERSE = "\033[m"
def logo():
		clear = "\x1b[0m"
		colors = [35,33,36 ]
#Agar Koi Line Cut Kare Ga To Kuch Nahi Chale Ga Gawaree Randi Ke Bache Itx Rohan Kr Ab Cut 
		x = """

 $$$$$$\  $$\                                     
$$  __$$\ $$ |                                    
$$ /  $$ |$$ | $$$$$$\  $$$$$$$\   $$$$$$\        
$$$$$$$$ |$$ |$$  __$$\ $$  __$$\ $$  __$$\       
$$  __$$ |$$ |$$ /  $$ |$$ |  $$ |$$$$$$$$ |      
$$ |  $$ |$$ |$$ |  $$ |$$ |  $$ |$$   ____|      
$$ |  $$ |$$ |\$$$$$$  |$$ |  $$ |\$$$$$$$\       
\__|  \__|\__| \______/ \__|  \__| \_______|      
                                                                                                
$$$$$$$\            $$\                           
$$  __$$\           $$ |                          
$$ |  $$ |$$\   $$\ $$ | $$$$$$\  $$\   $$\       
$$$$$$$  |$$ |  $$ |$$ |$$  __$$\ \$$\ $$  |      
$$  __$$< $$ |  $$ |$$ |$$$$$$$$ | \$$$$  /       
$$ |  $$ |$$ |  $$ |$$ |$$   ____| $$  $$<        
$$ |  $$ |\$$$$$$  |$$ |\$$$$$$$\ $$  /\$$\       
\__|  \__| \______/ \__| \_______|\__/  \__|      
___________________________________________________________

-=[ Facebook Tool Pool Ka Super Hero By Alone Rulex ]=-
-=[ Contact Us :: https://facebook.com/groups/411040537413366/]=-
___________________________________________________________
"""
		for N, line in enumerate(x.split("\n")):
			sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
			time.sleep(0.001)
logo()
testPY()
#Chalo Heder Include Kr Leta Ha Thoda Sa 
headers = {'Connection': 'keep-alive',
			'Cache-Control': 'max-age=0',
			'Upgrade-Insecure-Requests': '1',
			'User-Agent': 'Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			'Accept-Encoding': 'gzip, deflate',
			'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
			'referer': 'www.google.com'}
			
newt = datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')
newtt = newt
ysd = "aHR0cHM6Ly9wYXN0ZWJpbi5jb20vcmF3L2hQbTZLYXh1"
yss = base64.b64decode(ysd)
yff = yss.decode('utf-8', 'ignore')
y = requests.get(yff)
z = y.text
ch=z
print(BOLD+GREEN+"[#] Start Time ==> ",newtt)
print(BOLD+GREEN+'[#] _ Alone Boiis ==> '+ch+'\n\n')


#For Get Details Of User
asd = "aHR0cHM6Ly9wYXN0ZWJpbi5jb20vcmF3L3VocnR2NXAz"
ass = base64.b64decode(asd)
aff = ass.decode('utf-8', 'ignore')
a = requests.get(aff)
r = a.text
#All Dn Itz Tera Baap Rohan Singh Here
#Tohar Maya Ko Chodu 

def comment_on_posts(posts):
		try:
			rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : user, "pass" : password, "login" : "submit"}, headers = { "user-agent" : "Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115;]"})
			xo = rex.content
			x = 'mbasic_logout_button'
			y = 'save-device'
			if x in xo or y in xo:
				print (BOLD+GREEN+' [+] Sahii Haii .. | ')
				
			else:
				if 'checkpoint' in xo:
					print(BOLD+RED+' [x] Galat Haii .. |')
					
		except Exception as e:
			print(e)
			
			
			
				
							   
def get_posts(): 
	try:
		url = "https://mbasic.facebook.com"
	except HTTPError as e:
		print("HTTP Error")
	except URLError as e:
		print("URL Error")
		
qqq = "aHR0cHM6Ly9wYXN0ZWJpbi5jb20vcmF3L2prOXZhQW5Y"
www = base64.b64decode(qqq)
eee = www. decode("utf-8")
rrr = requests.get(eee)
for linee in rrr:
	mmm = linee.decode("utf-8")
	mmm = mmm.split(',')
inn = input(BOLD+CYAN+"[+] Mobile Number :: ")
if inn in mmm:
	user = input(BOLD+CYAN+"[+] User D :: ")
	password = input(BOLD+CYAN+"[+] Add Text File :: ")
	load = ('\n'+"________All Done....Loading Profile Info.....!"+'\n')
	for loa in load:
		sys.stdout.write(BOLD+BLUE+loa)
		sys.stdout.flush()
		time.sleep(0.001)
	for i in range(1):
		posts = get_posts()
		comment_on_posts(posts)

else:
	print(BOLD+RED+'[-] <==> Your Number Is Wrong Please Take Approval From Owner')

#Abb Samaj Gaya Hoga To Tu Appni Maa Chudva Le Chor Madarchod ke Bache