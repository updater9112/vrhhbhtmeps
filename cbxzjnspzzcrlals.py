import json
import time
import sys
import random
import os
import tempfile
import math
import getpass
import datetime as dt
import hashlib
import http.client
import ssl
from decimal import Decimal
from datetime import datetime
from os import system,name
import websocket
import colorama
from colorama import Fore,Back,Style
import requests
if name=="nt":
 import keyboard as hotkey
colorama.init(autoreset=True)
wsocket=websocket.WebSocket()
c=requests.Session()
is_global=True
global_url="api.pasino.io"
local_url="api.pasino.com"
header={"content-type":"application/json","x-requested-with":"XMLHttpRequest",}
app_header={"token":"Sa5z6EpdMBwLDJ3AQXhyxrVqRgGW2c3ZkPN7btm8UFT9CnYHue",}
with open("settings.json","r",encoding="utf-8")as filesetup:
 data_setting=filesetup.read()
ob=json.loads(data_setting)
RESET=Style.RESET_ALL
PUTIH=Style.BRIGHT+Fore.WHITE
HITAM=Style.BRIGHT+Fore.BLACK
HIJAU=Style.BRIGHT+Fore.GREEN
MERAH=Style.BRIGHT+Fore.RED
BIRU=Style.BRIGHT+Fore.BLUE
BG_HIJAU=Style.BRIGHT+Back.GREEN+Fore.WHITE
BG_MERAH=Style.BRIGHT+Back.RED+Fore.WHITE
BG_PUTIH=Style.BRIGHT+Back.WHITE+Fore.BLACK
NORMAL=Style.NORMAL+Fore.BLACK
KUNING=Style.BRIGHT+Fore.YELLOW
BG_HITAM=Style.BRIGHT+Back.BLACK+Fore.WHITE
def banner():
 bot_flag="\n"+BIRU
 bot_flag=bot_flag+"_________                __ ________  .__              \n"
 bot_flag=(bot_flag+"\\_   ___ \\_____  _______/  |\\______ \\ |__| ____  ____  \n")
 bot_flag=(bot_flag+"/    \\  \\/\\__  \\ \\____ \\   __\\    |  \\|  |/ ___\\/ __ \\ \n")
 bot_flag=(bot_flag+"\\     \\____/ __ \\|  |_> >  | |    `   \\  \\  \\__\\  ___/ \n")
 bot_flag=bot_flag+" \\______  (____  /   __/|__|/_______  /__|\\___  >___  >\n"
 bot_flag=(bot_flag+"    Dice\\/Limbo\\/|__|Pasino.com     \\/        \\/    \\/ \n")
 bot_flag=bot_flag+"\n"
 bot_flag=bot_flag+PUTIH+"Developer : "
 bot_flag=bot_flag+BIRU+"@apryaldy\n"
 bot_flag=bot_flag+PUTIH+"Contact   : "
 bot_flag=(bot_flag+BIRU+"@SafarSyam\n")
 bot_flag=bot_flag+PUTIH+"Version   : "
 bot_flag=bot_flag+BIRU+"P4.5.3\n\n"+RESET
 bot_flag=(bot_flag+BG_MERAH+PUTIH+" BOT ini GRATIS, tidak diperjual belikan !!!. \n"+RESET)
 bot_flag=(bot_flag+PUTIH+"Aktifkan 2FA untuk keamanan dan ganti password secara berkala. \n"+RESET)
 bot_flag=(bot_flag+PUTIH+"Hati-hati bagi pengguna RDP/VPS terhadap oknum yang tidak bertanggung jawab!!!. \n"+RESET)
 bot_flag=(bot_flag+PUTIH+"DICEBot untuk pasino, bisa di download disini: https://download.wanikere.com/db/DICEBot.1.0.7.1.zip \n"+RESET)
 print(bot_flag)
def clear():
 if name=="nt": 
  _=system("cls")
 else: 
  _=system("clear")
def do_refresh():
 clear()
 banner()
def chance_ui(hc):
 check=len(str(hc))
 result=str(hc)
 if check==2:
  result=" "+str(hc)+"    "
 if check==3:
  result=" "+str(hc)+"   "
 if check==4:
  result=" "+str(hc)+"  "
 if check==5:
  result=" "+str(hc)+" "
 return result
def cuan_api(url_,payload_):
 payload=json.dumps(payload_)
 cuan=http.client.HTTPSConnection("api.wanikere.com",context=ssl._create_unverified_context())
 try:
  cuan.request("POST",url_,payload,app_header)
  data=cuan.getresponse()
  data=data.read().decode("utf-8")
  data=json.loads(data)
 finally:
  cuan.close()
 return data
def pasino_api(url_,payload_,method_="POST",rt=True):
 global is_global
 payload=json.dumps(payload_)
 if(is_global):
  URL=global_url
 else:
  URL=local_url
 cuan=http.client.HTTPSConnection(URL)
 try:
  cuan.request(method_,url_,payload,header)
  data=cuan.getresponse()
  data=data.read().decode("utf-8")
  data=json.loads(data)
 except Exception as e:
  if(rt):
   is_global=False
   print("Mencoba pindah ke server Indonesia")
   return pasino_api(url_,payload_,method_,False)
  print("Sepertinya kamu butuh VPN!")
  sys.exit()
 finally:
  cuan.close()
 return data
def get_connection():
 global token
 global socket_token
 global wsocket
 token,socket_token=user_token(loginuser,loginpass,licensi_key)
 connection()
def connection(rt=True):
 global wsocket
 global is_global
 try:
  if(is_global):
   url="wss://socket.pasino.io/dice/"
   setcookie=c.get("https://www.pasino.io").cookies
  else:
   url="wss://socket.pasino.com/dice/"
   setcookie=c.get("https://www.pasino.com").cookies
  wsocket.connect(url,headers=header,cookie=setcookie)
 except Exception as e:
  if(rt):
   is_global=False
   return connection(False)
  print("Terjadi masalah teknis: "+str(e))
  sys.exit()
def pasino_ws(payload_):
 payload=json.dumps(payload_)
 try:
  wsocket.send(payload)
  result=wsocket.recv()
 except(websocket.WebSocketConnectionClosedException,Exception):
  return False
 return json.loads(result)
def betset_used(bs):
 betset={1:"Sicepat",2:"Marti",3:"Preroll",4:"DAlembert Wannabe",5:"Fibonacci",6:"Wageran",7:"JumpJack",8:"Autobot",9:"Sigesit",10:"MrBOT",11:"Labouchere",12:"Autobot-X",13:"Minsa",14:"Stepstone",15:"Autobot-S",}
 return betset.get(bs,"nothing")
def mrbot_api(balance_,algo_,target_):
 hd={"content-type":"application/x-www-form-urlencoded","cache-control":"no-cache",}
 payload=("balance="+str(balance_)+"&betset="+str(algo_)+"&target_profit="+str(target_))
 mrbot=http.client.HTTPSConnection("mrbotx.com")
 try:
  mrbot.request("POST","/counter.php",payload,hd)
  data=mrbot.getresponse()
  data=data.read()
  data=data.decode("utf-8")
  result=json.loads(data)
  if "balance" in result:
   return result
 except:
  print("Sepertinya https://mrbotx.com sedang tidak dapat diakses")
  sys.exit()
 finally:
  mrbot.close()
def resetseed():
 url="/dice/get-seed"
 payload={"token":token}
 result=pasino_api(url,payload)
def get_wdinfo():
 url="/withdraw/get-coin-information"
 payload={"coin":coin,"token":token}
 result=pasino_api(url,payload)
 if result["success"]is False:
  print(MERAH+"Pasino berkata: "+result["message"]+RESET)
  sys.exit()
 else:
  return result
def save_vault(am):
 url='/vault/transfer-in'
 data={"language":"en","amount":format8(str(am)),"coin":coin,"token":token,}
 result=pasino_api(url,data)
 return result['message']
def place_wd(am,md,adr,fp):
 if int(md)==8:
  url="/withdraw/place-withdrawal"
  data={"coin":coin,"method":"FAUCETPAY" if fp=="TRUE" else "DIRECT","address":adr,"amount":format8(str(am)),"token":token,}
 if int(md)==12:
  url="/transfer/send-transfer"
  data={"coin":coin,"user_name":adr,"amount":format8(str(am)),"token":token,}
 result=pasino_api(url,data)
 return result["message"]
def tip_opit(am):
 am=int(am/3)
 url="/transfer/send-transfer"
 data1={"language":"en","coin":coin,"user_name":"devpas91","amount":format8(str(am)),"token":token,}
 data2={"language":"en","coin":coin,"user_name":"buaya912","amount":format8(str(am*2)),"token":token,}
 pasino_api(url,data1)
 time.sleep(0.01)
 pasino_api(url,data2)
def user_token(user,password,license):
 url="/v3/cdice/"
 payload={"username":user,"password":password,"license":license,"platform":"capt","site":"pasino"}
 try:
  hasil=cuan_api(url,payload)
 except Exception as e:
  print(str(e))
  sys.exit()
 if "is_2fa" in hasil:
  is_2fa=hasil["is_2fa"]
  if int(is_2fa)==0:
   print(hasil["message"])
   code_2fa=input("Masukan Kode Google Auth:")
   payload={"username":user,"password":password,"code":code_2fa,"license":license,"platform":"capt","site":"pasino"}
   hasil=cuan_api(url,payload)
 if int(hasil["error"])==1:
  print(str(hasil["message"]))
  sys.exit()
 return hasil["token"],hasil["socket"]
def get_user():
 data={"method":"initialization","socket_token":socket_token}
 info_user=pasino_ws(data)
 if info_user is False:
  print("Reconnecting")
  time.sleep(3)
  get_connection()
  return get_user()
 infouser=info_user
 infouser["email"]=loginuser
 return info_user
def get_balance():
 data={"method":"get_balance","coin":coin}
 return pasino_ws(data)
def get_betinfo(game):
 url="/"+game+"/get-configuration"
 payload={}
 get_data=pasino_api(url,payload,"GET")
 get_data=get_data["coins"]
 for i,v in enumerate(get_data):
  if v["coin"]==coin:
   minbet=int(float(v["minimum_bet"])*(10**8))
   maxbet=int(float(v["maximum_bet"])*(10**8))
   return minbet,maxbet
def coingecko():
 coinid={"BTC":"bitcoin","ETH":"ethereum","LTC":"litecoin","DOGE":"dogecoin","NANO":"nano","TRX":"tron","USDT":"tether","FEY":"feyorra","BTT":"bittorrent","BNB":"binancecoin","SOL":"solana","FLOKI":"floki-inu","AVAX":"avalanche-2","HTR":"hathor","MATIC":"matic-network","ADA":"cardano","CAKE":"pancakeswap-token",}
 cek_harga=coinid.get(coin,"")
 if cek_harga=="":
  harga=0
 else:
  hd={"cache-control":"no-cache"}
  gecko=http.client.HTTPSConnection("api.coingecko.com")
  try:
   gecko.request("GET","/api/v3/simple/price?ids="+str(cek_harga)+"&vs_currencies=idr",headers=hd,)
   harga=gecko.getresponse()
   harga=harga.read().decode("utf-8")
   harga=json.loads(harga)
   harga=float(harga[cek_harga]["idr"])
  except:
   harga=0
  finally:
   gecko.close()
 return harga
def get_time():
 sekarang=datetime.now()
 return sekarang.strftime("%d/%m/%y %H:%M:%S")
def timeprocess(sec):
 minutes,seconds=divmod(sec,60)
 hours,minutes=divmod(minutes,60)
 days,hours=divmod(hours,24)
 stopwatchx=(days,hours,minutes,seconds)
 return stopwatchx
def format8(num):
 plus="" if(Decimal(num)>=0)else "-"
 num=str(abs(int(Decimal(num))))
 if len(num)<8:
  panjang_nol=int(8-len(num))
  num=(panjang_nol*"0")+str(num)
  result="0."+num
 if len(num)==8:
  panjang_nol=int(8-len(num))
  num=(panjang_nol*"0")+str(num)
  result="0."+num
 else:
  len_num=len(num)
  end=num[-8:]
  first=num[:len_num-8]
  result=first+"."+end
 return plus+result
def format5(num):
 if len(num)<5:
  panjang_nol=int(5-len(num))
  num=(panjang_nol*"0")+str(num)
  result="0."+num
 if len(num)==8:
  panjang_nol=int(5-len(num))
  num=(panjang_nol*"0")+str(num)
  result="0."+num
 else:
  len_num=len(num)
  end=num[-5:]
  first=num[:len_num-5]
  result=first+"."+end
 return result
def decimal5(num):
 digit,first=math.modf(num)
 digit5=int(digit*(10**5))
 digit5=format5(str(digit5))
 cek_digit=digit5[-4:]
 if cek_digit=="9999":
  result=round(int(first)+float(digit5),2)
 else:
  result=str(int(first))+digit5
 return result
def fibocal(n):
 if n<=1:
  return n+1
 return fibocal(n-1)+fibocal(n-2)
def paylosecalc(ch,tlose,tmplose,basebet,minbet):
 payout=95/float(ch)
 npfb=int(float(payout))-1
 if npfb>tlose:
  return minbet
 else:
  payback=int(tmplose/int(float(payout)))
  divbase=int(basebet/int(float(payout)))
  callpayout=divbase+payback
  if callpayout<minbet:
   divbase=minbet-payback
   callpayout=divbase+payback
  else:
   callpayout=divbase+payback
  return callpayout
def autobotcalc(ch,bals,minimal):
 if ch>49:
  po=95/ch
  marti=po/(po-1)
  maxls=po*15.15
  auto_base=(bals*(marti-1))/marti**maxls
  base=max(auto_base,minimal)
 else:
  po=95/ch
  marti=po/(po-1.1)
  maxls=po*15.85
  auto_base=(bals*(marti-1))/marti**maxls
  base=max(auto_base,minimal)
 return base,marti
def random_chance(minc,maxc):
 if minc==maxc:
  hasil_chance=float(minc)
 else:
  hasil_chance=random.uniform(float(minc),float(maxc))
 if playgame=="DICE":
  return round(float(94.99),2)if hasil_chance>=95 else round(max(hasil_chance,0.01),2)
 else:
  return round(hasil_chance,5)
def placebet_limbo(am,po,cs,ty):
 databet={"language":"en","client_seed":cs,"bet_amt":am,"coin":coin,"target_payout":str(po),"token":token,}
 url="/limbo/play"
 betting=pasino_api(url,databet)
 if betting["success"]is True:
  return betting
 if betting["message"].find("balance is not sufficient")!=-1:
  print("\n"+str(betting["message"]))
  sys.exit()
 if ty>2:
  print("\n"+str(betting["message"]))
  sys.exit()
 ty=ty+1
 return placebet_limbo(am,po,cs,ty)
def placebet_demo(am,rt,py,ch,pf1,pf2,cs,ty):
 if int(ty)==1:
  lenpay=len(pf1)
  fixpay=lenpay-5
  pay=pf1[0:fixpay]
 else:
  pay=pf2
 databet={"token":token,"bet_amt":am,"coin":coin,"client_seed":cs,"type":rt,"payout":py,"winning_chance":str(ch),"profit":pay,}
 url="/dice/play"
 betting=pasino_api(url,databet)
 if "success" in betting:
  if betting["success"]is True:
   return betting
  if betting["message"].find("balance is not sufficient")!=-1:
   print("\n"+str(betting["message"]))
   sys.exit()
  if ty>2:
   print("\n"+str(betting["message"]))
   sys.exit()
 ty=ty+1
 return placebet_demo(am,rt,py,ch,pf1,pf2,cs,ty)
def placebet_dice(am,rt,py,ch,pf1,pf2,cs,ty,retry_count=0):
 if int(ty)==1:
  lenpay=len(pf1)
  fixpay=lenpay-5
  pay=pf1[0:fixpay]
 else:
  pay=pf2
 databet={"method":"place_bet","bet_amt":am,"coin":coin,"client_seed":cs,"type":int(rt),"payout":py,"winning_chance":str(ch),"profit":pay,}
 result=pasino_ws(databet)
 if "win" in result:
  return result
 if "error" in result:
  if result["error"].find("balance is not sufficient")!=-1:
   print("\n"+str(result["error"]))
   sys.exit()
  if ty>2:
   print("\n"+str(result["error"]))
   sys.exit()
  if result["error"].find("Please select the game configuration")!=-1:
   return placebet_dice(am,rt,py,ch,pf1,pf2,cs,2)
  ty=ty+1
  return placebet_dice(am,rt,py,ch,pf1,pf2,cs,ty)
 time.sleep(0.5)
 return placebet_dice(am,rt,py,ch,pf1,pf2,cs,1)
def play_stats(bal,prof,mbet,mlose,tls,twg,pcent,waktu,pesan):
 do_refresh()
 warna_profit=HIJAU if prof>0 else MERAH
 print(RESET+BG_MERAH+" "+pesan+" "+RESET)
 print(" ")
 print(PUTIH+"  Saldo         : "+RESET+HIJAU+format8(str(bal))+RESET+" "+str(coin))
 print(PUTIH+"  Profit        : "+RESET+warna_profit+format8(str(prof))+" ("+str("{:.3%}".format(pcent))+" )"+RESET)
 print(PUTIH+"  Max Bet       : "+RESET+HIJAU+format8(str(mbet))+RESET)
 print(PUTIH+"  Max Lose      : "+RESET+HIJAU+format8(str(tls))+RESET)
 print(PUTIH+"  Total Wager   : "+RESET+HIJAU+format8(str(twg))+RESET)
 print(PUTIH+"  Total LS      : "+RESET+HIJAU+str(mlose)+RESET)
 print(PUTIH+"  Total Bet     : "+RESET+HIJAU+str(rollcount)+RESET)
 print(PUTIH+"  Waktu Process : "+RESET+BIRU+waktu+RESET)
 print(" ")
 if prof>0:
  print(PUTIH+"Dukung developer untuk pengembangan SC:"+RESET)
  print(PUTIH+"TRX        : TTtGDWyET9kCAN53S51ZnKoZoYsKkNF4Pi"+RESET)
  print(PUTIH+"DOGE       : DAHZDfLKFpGmyxVhUM7aNxoarAn1HhWRrH"+RESET)
  print(PUTIH+"x!!! Salam Opit !!!x"+RESET)
 else:
  print(PUTIH+"Silahkan cek file "+RESET+MERAH+"history_bet.txt"+RESET+" dan sesuaikan kembali betsetnya."+RESET)
 if jatah_total>0:
  tip_opit(jatah_total)
 if sent=="Go 2":
  errr_pesan=("Start Bals: "+format8(str(startbals))+" PF: "+str(round(float(pcent*100),2)))
  error_report(betmode,errr_pesan)
 wsocket.close()
def changemode(curr,total):
 toggle=curr+1
 if toggle==total:
  toggle=0
 if(ob["Betset"]["JumpJack"]["Mode"][toggle]["Status"]).upper()=="ON":
  return toggle
 curr=toggle
 return changemode(curr,total)
def calculate_base(mode_,balance_):
 basebet=int(float(ob["Betset"]["JumpJack"]["Mode"][mode_]["Base"])*(10**8))
 use_baldiv=ob["Betset"]["JumpJack"]["Mode"][mode_]["Balance Divider"]["Status"].upper()
 baldiv=int(ob["Betset"]["JumpJack"]["Mode"][mode_]["Balance Divider"]["Divider"])
 result=int(balance_/baldiv)if use_baldiv=="ON" else basebet
 return max(result,min_bet)
def check_bet(am):
 if am>max_bet:
  do_refresh()
  print("Maximum Bet untuk currency "+coin+" adalah: "+format8(str(max_bet)))
  print("Bet saat ini: "+format8(str(am)))
  time.sleep(5)
  sys.exit()
 if am<min_bet:
  do_refresh()
  print("Minimum Bet untuk currency "+coin+" adalah: "+format8(str(min_bet)))
  print("Bet saat ini: "+format8(str(am)))
  time.sleep(5)
  sys.exit()
jatah_total=0
def gogo(target_profit,target_percent,target_balance,target_lose,swmaxbet,swdbl,swls,):
 global tip_percent
 global jatah
 global jatah_total
 global sent
 global betmode
 global rollcount
 global min_bet
 global max_bet
 toggle_base=1
 stopwin=False
 bethigh=True
 stopwin_baldrop=int(startbals-((swdbl/100)*startbals))if swdbl>0 else 0
 stopwin_ls=swls
 target_percent=(target_percent/100)if target_percent>0 else 0
 target_lose=(startbals-target_lose)if target_lose>0 else 0
 profit=0
 temp_profit=0
 total_profit=0
 ws=0
 ls=0
 roltoggle=0
 wd=0
 profit_percent=0
 current_strike=0
 lose_amount=0
 win_count=0
 lose_count=0
 roll_win=0
 roll_lose=0
 max_win=0
 max_lose=0
 largest_bet=0
 largest_lose=0
 amount=0
 nextbet=0
 previousbet=0
 ch_toggle=0
 wager=0
 betprofit=0
 betlose=0
 betwin=0
 betcount=0
 jumpprofit=0
 stopmsg=""
 pesan=""
 min_bet,max_bet=get_betinfo(playgame.lower())
 start_time=time.time()
 rollcount=0
 if coin!="GEM" and ob["Account"]["Username"]!="apryaldy@sukalupa.com":
  tip_percent=9/1000
  jatah=0
  jatah_total=0
 else:
  tip_percent=0
  jatah=0
  jatah_total=0
 global_divider=float(ob["Bet Amount"]["Balance Divider"]["Divider"])
 divider_status=ob["Bet Amount"]["Balance Divider"]["Status"].upper()
 global_base=int(float(ob["Bet Amount"]["Base"])*(10**8))
 global_base=(int(startbals/global_divider)if divider_status=="ON" else global_base)
 global_base=max(global_base,min_bet)
 global_preroll=int(float(ob["Bet Amount"]["Preroll Bet"])*(10**8))
 global_preroll=max(global_preroll,min_bet)
 global_shoot=int(float(ob["Bet Amount"]["Shoot Bet"])*(10**8))
 auto_shoot=ob["Bet Amount"]["Auto Shoot"]["Status"].upper()
 shoot_onls=int(ob["Bet Amount"]["Auto Shoot"]["After LS"])
 shoot_onws=int(ob["Bet Amount"]["Auto Shoot"]["After WS"])
 if(ob["Bet Roll"]["Hi / Low"]["Toggle"]).upper()=="ON":
  toggle_win=int(Decimal(ob["Bet Roll"]["Hi / Low"]["If Win"]))
  toggle_lose=int(Decimal(ob["Bet Roll"]["Hi / Low"]["If Lose"]))
  roltoggle=1
 else:
  bethigh=True if((ob["Bet Roll"]["Bet High"]).upper()=="TRUE")else False
 if(ob["Betset"]["Sicepat"]["Toggle"]).upper()=="ON":
  betmode=1
  playmode="Sicepat"
  base=global_base
  preset=int(float(ob["Betset"]["Sicepat"]["Profit Reset"])*(10**8))
  ch_min1=Decimal(ob["Betset"]["Sicepat"]["Chance Win"]["Min"])
  ch_min2=Decimal(ob["Betset"]["Sicepat"]["Chance Lose"]["Min"])
  ch_max1=Decimal(ob["Betset"]["Sicepat"]["Chance Win"]["Max"])
  ch_max2=Decimal(ob["Betset"]["Sicepat"]["Chance Lose"]["Max"])
  chance=random_chance(ch_min1,ch_max1)
  tmplose=0
 elif(ob["Betset"]["Marti"]["Toggle"]).upper()=="ON":
  betmode=2
  playmode="Martingale"
  base=global_base
  b2base_profit=int(float(ob["Betset"]["Marti"]["Reset if profit"])*(10**8))
  b2base_maxbet=int(float(ob["Betset"]["Marti"]["Reset if maxbet"])*(10**8))
  b2base_win=int(ob["Betset"]["Marti"]["Reset if win"])
  b2base_lose=int(ob["Betset"]["Marti"]["Reset if lose"])
  ch_min=Decimal(ob["Betset"]["Marti"]["Chance"]["Min"])
  ch_max=Decimal(ob["Betset"]["Marti"]["Chance"]["Max"])
  if_win=Decimal(ob["Betset"]["Marti"]["If Win"])
  if_lose=Decimal(ob["Betset"]["Marti"]["If Lose"])
 elif(ob["Betset"]["Preroll"]["Toggle"]).upper()=="ON":
  betmode=3
  playmode="Preroll"
  base=global_base
  preset=int(float(ob["Betset"]["Preroll"]["Profit Reset"])*(10**8))
  preroll=int(ob["Betset"]["Preroll"]["Preroll"])
  ch_min=Decimal(ob["Betset"]["Preroll"]["Chance"]["Min"])
  ch_max=Decimal(ob["Betset"]["Preroll"]["Chance"]["Max"])
  if_win=Decimal(ob["Betset"]["Preroll"]["If Win"])
  if_lose=Decimal(ob["Betset"]["Preroll"]["If Lose"])
  passcount=preroll-1
 elif(ob["Betset"]["DAlembert Wannabe"]["Toggle"]).upper()=="ON":
  betmode=4
  playmode="DAlembert"
  dlevel=0
  base=global_base
  preset=int(float(ob["Betset"]["DAlembert Wannabe"]["Profit Reset"])*(10**8))
  ch_min=Decimal(ob["Betset"]["DAlembert Wannabe"]["Chance"]["Min"])
  ch_max=Decimal(ob["Betset"]["DAlembert Wannabe"]["Chance"]["Max"])
 elif(ob["Betset"]["Fibonacci"]["Toggle"]).upper()=="ON":
  betmode=5
  playmode="Fibonacci"
  base=global_base
  fibocount=0
  ch_min=Decimal(ob["Betset"]["Fibonacci"]["Chance"]["Min"])
  ch_max=Decimal(ob["Betset"]["Fibonacci"]["Chance"]["Max"])
  b2base_profit=int(float(ob["Betset"]["Fibonacci"]["Reset if profit"])*(10**8))
  b2base_maxbet=int(float(ob["Betset"]["Fibonacci"]["Reset if maxbet"])*(10**8))
  b2base_win=int(ob["Betset"]["Fibonacci"]["Reset if win"])
  b2base_lose=int(ob["Betset"]["Fibonacci"]["Reset if lose"])
 elif(ob["Betset"]["Wageran"]["Toggle"]).upper()=="ON":
  betmode=6
  playmode="Wageran"
  ch_toggle=1
  wbase=int(float(ob["Betset"]["Wageran"]["Wager"]["Base"])*(10**8))
  wch_min=Decimal(ob["Betset"]["Wageran"]["Wager"]["CHMin"])
  wch_max=Decimal(ob["Betset"]["Wageran"]["Wager"]["CHMax"])
  rbase=int(float(ob["Betset"]["Wageran"]["Recovery"]["Base"])*(10**8))
  rch_min=Decimal(ob["Betset"]["Wageran"]["Recovery"]["CHMin"])
  rch_max=Decimal(ob["Betset"]["Wageran"]["Recovery"]["CHMax"])
  rif_win=Decimal(ob["Betset"]["Wageran"]["Recovery"]["If Win"])
  rif_lose=Decimal(ob["Betset"]["Wageran"]["Recovery"]["If Lose"])
  rpreroll=int(ob["Betset"]["Wageran"]["Recovery"]["Preroll"])
  rpreset=int(float(ob["Betset"]["Wageran"]["Recovery"]["Reset if profit"])*(10**8))
  target_wager=int(float(ob["Betset"]["Wageran"]["Target Wager"])*(10**8))
  base=wbase if ch_toggle==1 else rbase
  chance=random_chance(wch_min,wch_max)
 elif(ob["Betset"]["JumpJack"]["Toggle"]).upper()=="ON":
  betmode=7
  mode=ob["Betset"]["JumpJack"]["Mode"]
  jump_reset_profit=int(float(ob["Betset"]["JumpJack"]["Reset Jump if Profit"])*(10**8))
  jump_reset_ws=int(ob["Betset"]["JumpJack"]["Reset Jump if Win"])
  continues_bet=ob["Betset"]["JumpJack"]["Continuous Bet"].upper()
  total_mode=len(mode)
  mode_toggle=changemode(total_mode-1,total_mode)
  jump_name=mode[mode_toggle]["Name"]
  base=calculate_base(mode_toggle,startbals)
  if_win=Decimal(mode[mode_toggle]["If Win"])
  if_lose=Decimal(mode[mode_toggle]["If Lose"])
  profit_reset=int(float(mode[mode_toggle]["Reset if profit"])*(10**8))
  win_reset=int(mode[mode_toggle]["Reset if win"])
  lose_reset=int(mode[mode_toggle]["Reset if lose"])
  maxbet_reset=int(float(mode[mode_toggle]["Reset if maxbet"])*(10**8))
  ch_min=Decimal(mode[mode_toggle]["Chance"]["Min"])
  ch_max=Decimal(mode[mode_toggle]["Chance"]["Max"])
  jump_abet=int(mode[mode_toggle]["Kondisi Jump"]["After Bet"])
  jump_awin=int(mode[mode_toggle]["Kondisi Jump"]["Win Streak"])
  jump_alose=int(mode[mode_toggle]["Kondisi Jump"]["Lose Streak"])
  jump_aprofit=int(float(mode[mode_toggle]["Kondisi Jump"]["After Profit"])*(10**8))
  jump_abetwin=int(int(mode[mode_toggle]["Kondisi Jump"]["Next Win After Bet"]))
 elif(ob["Betset"]["Autobot"]["Toggle"]).upper()=="ON":
  betmode=8
  playmode="Autobot"
  po_min=Decimal(ob["Betset"]["Autobot"]["Payout"]["Min"])
  po_max=Decimal(ob["Betset"]["Autobot"]["Payout"]["Max"])
  risk=Decimal(ob["Betset"]["Autobot"]["Risk (%)"])
  reverse=ob["Betset"]["Autobot"]["Reverse Logic"].upper()
  autocalc=ob["Betset"]["Autobot"]["Auto Calc"]["Status"].upper()
  m_baldiv=Decimal(ob["Betset"]["Autobot"]["Auto Calc"]["Balance Divider"])
  m_marti=Decimal(ob["Betset"]["Autobot"]["Auto Calc"]["Multipler"])
  maxls=po_max*Decimal(15.15)
  marti=(po_max/(po_max-Decimal(1.1)))if autocalc=="ON" else m_marti
  baldiv=((marti**maxls)*(maxls/(maxls*(marti-1)))if autocalc=="ON" else m_baldiv)
  base=max(min_bet,(startbals/baldiv))
  risk_level=startbals*(risk/100)
  bet_level=0
  po_new=po_max if reverse=="TRUE" else po_min
  po_prev=po_new
  chance=(9500/po_new)/100
  chance=round(chance,2)
 elif(ob["Betset"]["Sigesit"]["Toggle"]).upper()=="ON":
  betmode=9
  playmode="Sigesit"
  base=global_base
  profit_reset=int(float(ob["Betset"]["Sigesit"]["Profit Reset"])*(10**8))
  passroll=int(ob["Betset"]["Sigesit"]["Preroll"])
  cut_lose=int(ob["Betset"]["Sigesit"]["Cut Lose"])
  multiplier=float(ob["Betset"]["Sigesit"]["Multipler"])
  ch_min1=Decimal(ob["Betset"]["Sigesit"]["Chance Win"]["Min"])
  ch_max1=Decimal(ob["Betset"]["Sigesit"]["Chance Win"]["Max"])
  ch_min2=Decimal(ob["Betset"]["Sigesit"]["Chance Lose"]["Min"])
  ch_max2=Decimal(ob["Betset"]["Sigesit"]["Chance Lose"]["Max"])
  chance=random_chance(ch_min1,ch_max1)
  passcount=passroll
  gocount=0
  tmplose=0
 elif(ob["Betset"]["Labouchere"]["Toggle"]).upper()=="ON":
  betmode=11
  playmode="Labouchere"
  base=global_base
  profit_reset=int(float(ob["Betset"]["Labouchere"]["Profit Reset"])*(10**8))
  ch_min=Decimal(ob["Betset"]["Labouchere"]["Chance"]["Min"])
  ch_max=Decimal(ob["Betset"]["Labouchere"]["Chance"]["Max"])
  array_bet=[]
 elif(ob["Betset"]["Autobot-X"]["Toggle"]).upper()=="ON":
  betmode=12
  playmode="Autobot-X"
  if target_profit>0 or target_percent>0 or target_balance>0:
   auto_target=max(target_profit,(target_percent*startbals),target_balance)
  else:
   print("Mode Autobot-X memberlukan Target Profit / Percent / Balance untuk diset.")
   sys.exit()
  autostop=False
  auto_step=float(ob["Betset"]["Autobot-X"]["Bet Divider"])
  auto_stopwin=float(ob["Betset"]["Autobot-X"]["Stopwin If Baldrop (%)"])/100
  ch_min1=float(ob["Betset"]["Autobot-X"]["Big Chance"]["Min"])
  ch_max1=float(ob["Betset"]["Autobot-X"]["Big Chance"]["Max"])
  ch_min2=float(ob["Betset"]["Autobot-X"]["Small Chance"]["Min"])
  ch_max2=float(ob["Betset"]["Autobot-X"]["Small Chance"]["Max"])
  divider=auto_target/auto_step
  basebet=startbals
  roltoggle=0
  chance=random_chance(ch_min1,ch_max1)
  auto_cx=random.uniform(ch_min2,ch_max2)
  auto_dd=0
  auto_dc=0
  base=global_base
 elif(ob["Betset"]["MinSa"]["Toggle"].upper()=="ON"):
  betmode=13
  playmode="MinSa"
  ch_min=Decimal(ob["Betset"]["MinSa"]["Chance"]["Min"])
  ch_max=Decimal(ob["Betset"]["MinSa"]["Chance"]["Max"])
  ch_min=round(max(ch_min,0.01),2)
  ch_max=round(min(ch_max,94.99),2)
  marti=float(ob["Betset"]["MinSa"]["Marti"])
  chance=ch_max
  bethigh=True
  base=global_base
  pofactor=95 if playgame=="DICE" else 97
 elif(ob["Betset"]["Stepstone"]["Toggle"].upper()=="ON"):
  betmode=14
  playmode="Stepstone"
  ch_min1=Decimal(ob["Betset"]["Stepstone"]["Chance Win"]["Min"])
  ch_max1=Decimal(ob["Betset"]["Stepstone"]["Chance Win"]["Max"])
  ch_min2=Decimal(ob["Betset"]["Stepstone"]["Chance Lose"]["Min"])
  ch_max2=Decimal(ob["Betset"]["Stepstone"]["Chance Lose"]["Max"])
  if_win=float(ob["Betset"]["Stepstone"]["Chance Win"]["If Win"])
  if_lose=float(ob["Betset"]["Stepstone"]["Chance Lose"]["If Lose"])
  preset=int(float(ob["Betset"]["Stepstone"]["Reset if Profit"])*(10**8))
  chance=random_chance(ch_min1,ch_max1)
  base=global_base
  bethigh=True
 elif(ob["Betset"]["Autobot-S"]["Toggle"].upper()=="ON"):
  betmode=15
  playmode="Autobot-S"
  chance=Decimal(ob["Betset"]["Autobot-S"]["Chance"])
  percentf=float(ob["Betset"]["Autobot-S"]["Multi Factor"])
  playrisk=float(ob["Betset"]["Autobot-S"]["Balance Risk"])
  balancerisk=startbals*playrisk
  base=global_base
  offense=True
  off_value=float(1)
  calc_maxls=float(1)
  percent=float(max(percentf,1))
 else:
  betmode=1
  playmode="Sicepat"
  base=global_base
  preset=int(float(ob["Betset"]["Sicepat"]["Profit Reset"])*(10**8))
  ch_min1=Decimal(ob["Betset"]["Sicepat"]["Chance Win"]["Min"])
  ch_min2=Decimal(ob["Betset"]["Sicepat"]["Chance Lose"]["Min"])
  ch_max1=Decimal(ob["Betset"]["Sicepat"]["Chance Win"]["Max"])
  ch_max2=Decimal(ob["Betset"]["Sicepat"]["Chance Lose"]["Max"])
  chance=random_chance(ch_min1,ch_max1)
  tmplose=0
 amount=base if betmode not in[3,9]else global_preroll
 amount=max(amount,min_bet)
 try:
  while True:
   rollcount+=1
   betcount+=1
   if betmode in[2,3,4,5,7,10,11]:
    chance=random_chance(ch_min,ch_max)
   if roltoggle==1:
    if ws>=toggle_win:
     bethigh=not bethigh
     ws=0
    if ls>=toggle_lose:
     bethigh=not bethigh
     ls=0
   if(ob["Bet Roll"]["Random"]).upper()=="TRUE":
    bethigh=True if random.randint(1,2)==1 else False
   condition=1 if bethigh is True else 2
   rolebet=" H " if condition==1 else " L "
   bet_amt=format8(str(amount))
   v_odds=float(95/chance)
   v_odds=str(decimal5(v_odds))
   cal_profit1="{:.13f}".format(float((Decimal(bet_amt)*Decimal(v_odds))-Decimal(bet_amt)))
   cal_profit2=(Decimal(bet_amt)*Decimal(v_odds))-Decimal(bet_amt)
   win_profit1=str(cal_profit1)
   win_profit2=str(cal_profit2)
   randomseed=hashlib.md5(getpass.getuser().encode())
   client_seed=randomseed.hexdigest()
   if playgame=="DICE":
    chancegui=chance_ui(chance)
    if coin=="GEM":
     betting=placebet_demo(bet_amt,condition,v_odds,chance,win_profit1,win_profit2,client_seed,1,)
    else:
     betting=placebet_dice(bet_amt,condition,v_odds,chance,win_profit1,win_profit2,client_seed,1,)
   elif playgame=="LIMBO":
    v_odds=str(round((97/chance),2))
    betting=placebet_limbo(bet_amt,v_odds,client_seed,1)
    chancegui=chance_ui(v_odds)
   wager=wager+amount
   profit=betting["profit"]
   state=betting["win"]
   previousbet=amount
   current_time=time.time()
   elapsed_time=current_time-start_time
   time_played="%dD %dH %dM %dS"%timeprocess(int(elapsed_time))
   time_played_text="%d-%d:%d:%d"%timeprocess(int(elapsed_time))
   if state==1 and tip_percent>0:
    jatah=int((float(profit)*(10**8))*tip_percent)
    jatah_total=jatah_total+jatah
    profit=int(float(profit)*(10**8))-jatah
    profit=format8(str(profit))
   current_balance=int(float(betting["balance"])*(10**8))-jatah_total
   total_profit=total_profit+int(float(profit)*(10**8))
   temp_profit=temp_profit+int(float(profit)*(10**8))
   betprofit=betprofit+int(float(profit)*(10**8))
   jumpprofit=jumpprofit+int(float(profit)*(10**8))
   wdbalance=float(int(current_balance))/(10**8)
   wd="{:0,.2f}".format(marketidx*wdbalance)
   time_diff=dt.datetime.today().timestamp()-start_time
   speedbet=round(rollcount/time_diff)
   if int(float(profit)>=0):
    betInfo=(BG_HIJAU+PUTIH+str(rolebet)+RESET+HIJAU+" AM:"+format8(str(previousbet))+" PF:+"+str(profit))
   else:
    betInfo=(BG_MERAH+PUTIH+str(rolebet)+RESET+MERAH+" AM:"+format8(str(previousbet))+" PF:"+str(profit))
   if total_profit>=0:
    textTotalProfit=HIJAU+" PT:+"+format8(str(total_profit))
    profit_percent=float(Decimal(format8(str(total_profit)))/Decimal(format8(str(startbals))))
    profit_percent_text=HIJAU+"PT:"+"{:.3%}".format(profit_percent)
   else:
    textTotalProfit=MERAH+" PT:"+format8(str(total_profit))
    profit_percent=0
    profit_percent_text=MERAH+"PT:"+"{:.3%}".format(profit_percent)
   if(ob["Auto Vault"]["Status"]).upper()=="ON":
    wd_trigger=int(float(ob["Auto Vault"]["Trigger Balance"])*(10**8))
    wd_amount=int(float(ob["Auto Vault"]["Amount Vault"])*(10**8))
    if current_balance>=wd_trigger:
     autowd=save_vault(wd_amount)
     wd_mode="vault"
     with open("history_wd.txt","a+",encoding="utf-8")as x:
      x.write(str(get_time())+" "+wd_mode+" "+format8(str(wd_amount))+" "+str(autowd)+"\n")
   print(BG_PUTIH+NORMAL+chancegui+RESET+betInfo+RESET+textTotalProfit+RESET+BIRU+" BL"+RESET+":"+format8(str(current_balance))+RESET+MERAH+" ML"+RESET+":"+format8(str(largest_lose))+RESET+KUNING+" IDR"+RESET+":"+str(wd)+RESET)
   logprofit=" "+str(profit)if(int(float(profit)>=0))else str(profit)
   logtotal=(" "+format8(str(total_profit))if total_profit>=0 else format8(str(total_profit)))
   if state==1:
    ws=ws+1
    ls=0
    win_count=win_count+1
    lose_count=0
    lose_amount=0
    current_strike=HIJAU+"CS:"+str(win_count)
    if win_count>=max_win:
     max_win=win_count
   else:
    ws=0
    ls=ls+1
    win_count=0
    lose_count=lose_count+1
    current_strike=MERAH+"CS:"+str(lose_count)
    lose_amount=lose_amount+previousbet
    max_lose=max(max_lose,lose_count)
    largest_lose=max(largest_lose,lose_amount)
    if lose_count>=stopwin_ls>0:
     stopwin=True
     stopmsg="LS"
   if current_balance<=stopwin_baldrop>0:
    stopwin=True
    stopmsg="BalDrop"
   with open("history_bet.txt","a+",encoding="utf-8")as f:
    f.write(str(rollcount)+" "+str(get_time())+" "+"CH:"+chancegui+str(rolebet)+"LS:"+str(lose_count)+" "+"AM:"+format8(str(amount))+" "+"PF:"+logprofit+" "+"LB:"+format8(str(largest_bet))+" "+"LL:"+format8(str(largest_lose))+" "+"PT:"+logtotal+" "+"BL:"+format8(str(current_balance))+"\n")
   if state==1 and stopwin is True:
    if stopmsg=="Limit Streak":
     pesan="Bot berhenti karena Max LS telah tercapai"
     play_stats(current_balance,total_profit,largest_bet,max_lose,largest_lose,wager,profit_percent,time_played,pesan,)
     break
    if ob["Stopwin"]["On Profit"].upper()=="TRUE":
     if total_profit>0:
      if stopmsg=="Maxbet":
       pesan="Bot berhenti karena Maxbet telah tercapai"
       play_stats(current_balance,total_profit,largest_bet,max_lose,largest_lose,wager,profit_percent,time_played,pesan,)
       break
      if stopmsg=="LS":
       pesan="Bot berhenti karena telah mencapai LS "+str(stopwin_ls)
       play_stats(current_balance,total_profit,largest_bet,max_lose,largest_lose,wager,profit_percent,time_played,pesan,)
       break
      if stopmsg=="BalDrop":
       pesan=("Bot berhenti karena balance drop "+str(swdbl)+"%")
       play_stats(current_balance,total_profit,largest_bet,max_lose,largest_lose,wager,profit_percent,time_played,pesan,)
       break
      break
    else:
     if stopmsg=="Maxbet":
      pesan="Bot berhenti karena Maxbet telah tercapai"
      play_stats(current_balance,total_profit,largest_bet,max_lose,largest_lose,wager,profit_percent,time_played,pesan,)
      break
     if stopmsg=="LS":
      pesan="Bot berhenti karena telah mencapai LS "+str(stopwin_ls)
      play_stats(current_balance,total_profit,largest_bet,max_lose,largest_lose,wager,profit_percent,time_played,pesan,)
      break
     if stopmsg=="BalDrop":
      pesan="Bot berhenti karena balance drop "+str(swdbl)+"%"
      play_stats(current_balance,total_profit,largest_bet,max_lose,largest_lose,wager,profit_percent,time_played,pesan,)
      break
     break
   if betmode==1:
    tmplose+=previousbet
    if state==1:
     roll_lose=0
     if temp_profit>=preset:
      nextbet=base
      chance=random_chance(ch_min1,ch_max1)
     tmplose=0
    else:
     roll_lose+=1
     chance=random_chance(ch_min2,ch_max2)
     nextbet=paylosecalc(ch_max2,roll_lose,tmplose,base,min_bet)
   elif betmode==2:
    if state==1:
     roll_win+=1
     roll_lose=0
     if temp_profit>=b2base_profit>0:
      nextbet=base
      temp_profit=0
     else:
      nextbet=previousbet*if_win
    else:
     roll_win=0
     roll_lose+=1
     nextbet=previousbet*if_lose
    if roll_win>=b2base_win>0:
     nextbet=base
     roll_win=0
    if roll_lose>=b2base_lose>0:
     nextbet=base
     roll_lose=0
    if nextbet>=b2base_maxbet>0:
     nextbet=base
   elif betmode==3:
    if state==1:
     passcount=preroll-1
     if temp_profit>preset:
      nextbet=global_preroll
      temp_profit=0
     else:
      nextbet=previousbet*if_win
    else:
     if passcount==0:
      nextbet=base
     elif passcount<0:
      nextbet=previousbet*if_lose
     else:
      nextbet=global_preroll
     passcount-=1
   elif betmode==4:
    if state==1:
     dlevel-=1
     if temp_profit>=preset:
      temp_profit=0
      dlevel=0
     dlevel=max(dlevel,0)
    else:
     dlevel+=1
    nextbet=base+(base*dlevel)
   elif betmode==5:
    if state==1:
     roll_win+=1
     roll_lose=0
     if temp_profit>=b2base_profit:
      fibocount=0
      temp_profit=0
      nextbet=base
     else:
      fibocount-=1
      fibocount=max(fibocount,0)
      nextbet=base*fibocal(fibocount)
    else:
     roll_win=0
     roll_lose+=0
     fibocount+=1
     nextbet=base*fibocal(fibocount)
    if roll_win>=b2base_win>0:
     nextbet=base
     roll_win=0
     fibocount=0
    if roll_lose>=b2base_lose>0:
     nextbet=base
     roll_lose=0
     fibocount=0
    if nextbet>=b2base_maxbet>0:
     nextbet=base
     fibocount=0
   elif betmode==6:
    if wager>=target_wager and total_profit>0:
     pesan="Target Wager Telah Tercapai"
     play_stats(current_balance,total_profit,largest_bet,max_lose,largest_lose,wager,profit_percent,time_played,pesan,)
     break
    ch_toggle=1 if(total_profit>0)else 2
    if ch_toggle==1:
     base=wbase
     preroll=0
     chance=random_chance(wch_min,wch_max)
    else:
     base=rbase
     if_win=rif_win
     if_lose=rif_lose
     preroll=rpreroll
     preset=rpreset
     chance=random_chance(rch_min,rch_max)
    if ch_toggle==1:
     nextbet=base
    else:
     if lose_count==1:
      previousbet=base
      temp_profit=0
     if state==1:
      if temp_profit>=preset:
       temp_profit=0
       nextbet=global_preroll if preroll!=0 else base
      else:
       nextbet=previousbet*if_win
     else:
      if preroll!=0:
       if lose_count==preroll:
        nextbet=base*if_lose
       elif lose_count>preroll:
        nextbet=previousbet*if_lose
       else:
        nextbet=global_preroll
      else:
       nextbet=previousbet*if_lose
   elif betmode==7:
    if state==1:
     betwin+=1
     betlose=0
     roll_win+=1
     roll_lose=0
     nextbet=previousbet*if_win
     if betcount>=jump_abetwin>0:
      betcount=0
      betwin=0
      betlose=0
      betprofit=0
      mode_toggle=changemode(mode_toggle,total_mode)
      recalculate=mode[mode_toggle]["Balance Divider"]["Recalculate on Play"].upper()
      if recalculate=="TRUE":
       base=calculate_base(mode_toggle,current_balance)
      else:
       base=calculate_base(mode_toggle,startbals)
      nextbet=nextbet if continues_bet=="TRUE" else base
    else:
     betwin=0
     betlose+=1
     roll_win=0
     roll_lose+=1
     nextbet=previousbet*if_lose
    if betcount>=jump_abet>0:
     betcount=0
     betwin=0
     betlose=0
     betprofit=0
     mode_toggle=changemode(mode_toggle,total_mode)
     recalculate=mode[mode_toggle]["Balance Divider"]["Recalculate on Play"].upper()
     if recalculate=="TRUE":
      base=calculate_base(mode_toggle,current_balance)
     else:
      base=calculate_base(mode_toggle,startbals)
     nextbet=nextbet if continues_bet=="TRUE" else base
    if betwin>=jump_awin>0:
     betcount=0
     betwin=0
     betlose=0
     betprofit=0
     mode_toggle=changemode(mode_toggle,total_mode)
     recalculate=mode[mode_toggle]["Balance Divider"]["Recalculate on Play"].upper()
     if recalculate=="TRUE":
      base=calculate_base(mode_toggle,current_balance)
     else:
      base=calculate_base(mode_toggle,startbals)
     nextbet=nextbet if continues_bet=="TRUE" else base
    if betlose>=jump_alose>0:
     betcount=0
     betwin=0
     betlose=0
     betprofit=0
     mode_toggle=changemode(mode_toggle,total_mode)
     recalculate=mode[mode_toggle]["Balance Divider"]["Recalculate on Play"].upper()
     if recalculate=="TRUE":
      base=calculate_base(mode_toggle,current_balance)
     else:
      base=calculate_base(mode_toggle,startbals)
     nextbet=nextbet if continues_bet=="TRUE" else base
    if betprofit>=jump_aprofit>0:
     betcount=0
     betwin=0
     betlose=0
     betprofit=0
     mode_toggle=changemode(mode_toggle,total_mode)
     recalculate=mode[mode_toggle]["Balance Divider"]["Recalculate on Play"].upper()
     if recalculate=="TRUE":
      base=calculate_base(mode_toggle,current_balance)
     else:
      base=calculate_base(mode_toggle,startbals)
     nextbet=nextbet if continues_bet=="TRUE" else base
    if jumpprofit>=jump_reset_profit>0:
     mode_toggle=changemode(total_mode-1,total_mode)
     jumpprofit=0
     recalculate=mode[mode_toggle]["Balance Divider"]["Recalculate on Play"].upper()
     if recalculate=="TRUE":
      base=calculate_base(mode_toggle,current_balance)
     else:
      base=calculate_base(mode_toggle,startbals)
     nextbet=base
    if betwin>=jump_reset_ws>0:
     mode_toggle=changemode(total_mode-1,total_mode)
     betwin=0
     recalculate=mode[mode_toggle]["Balance Divider"]["Recalculate on Play"].upper()
     if recalculate=="TRUE":
      base=calculate_base(mode_toggle,current_balance)
     else:
      base=calculate_base(mode_toggle,startbals)
     nextbet=base
    jump_name=mode[mode_toggle]["Name"]
    if_win=Decimal(mode[mode_toggle]["If Win"])
    if_lose=Decimal(mode[mode_toggle]["If Lose"])
    profit_reset=int(float(mode[mode_toggle]["Reset if profit"])*(10**8))
    win_reset=int(mode[mode_toggle]["Reset if win"])
    lose_reset=int(mode[mode_toggle]["Reset if lose"])
    maxbet_reset=int(float(mode[mode_toggle]["Reset if maxbet"])*(10**8))
    jump_abet=int(mode[mode_toggle]["Kondisi Jump"]["After Bet"])
    jump_awin=int(mode[mode_toggle]["Kondisi Jump"]["Win Streak"])
    jump_alose=int(mode[mode_toggle]["Kondisi Jump"]["Lose Streak"])
    jump_aprofit=int(float(mode[mode_toggle]["Kondisi Jump"]["After Profit"])*(10**8))
    jump_abetwin=int(int(mode[mode_toggle]["Kondisi Jump"]["Next Win After Bet"]))
    pmode=(jump_name[:10]+"..")if len(jump_name)>10 else jump_name
    playmode="Set: "+str(pmode)
    ch_min=Decimal(mode[mode_toggle]["Chance"]["Min"])
    ch_max=Decimal(mode[mode_toggle]["Chance"]["Max"])
    if temp_profit>=profit_reset>0:
     temp_profit=0
     nextbet=base
    if roll_win>=win_reset>0:
     nextbet=base
     roll_win=0
    if roll_lose>=lose_reset>0:
     nextbet=base
     roll_lose=0
    if nextbet>=maxbet_reset>0:
     nextbet=base
   elif betmode==8:
    if state==1:
     bet_level=0
     po_new=po_max if reverse=="TRUE" else po_min
     po_prev=po_new
    else:
     bet_level+=1
    if bet_level==0:
     nextbet=base
    else:
     if reverse=="TRUE":
      if lose_amount<risk_level:
       nextbet=previousbet*marti
      else:
       nextbet=lose_amount/(po_new+1)
     else:
      if po_prev>=po_max:
       po_prev=po_max
       if lose_amount<risk_level:
        nextbet=previousbet*marti
       else:
        nextbet=lose_amount/(po_new-1)
      else:
       nextbet=previousbet
    po_prev=po_new
    nextbet=max(nextbet,min_bet)
    if bet_level==0:
     ch_new=(9500/po_new)/100
    else:
     po_new=(po_prev-1)if reverse=="TRUE" else(po_prev+1)
     po_new=(max(po_new,po_min)if reverse=="TRUE" else min(po_new,po_max))
     ch_new=(9500/po_new)/100
    chance=94.99 if ch_new>=95 else max(ch_new,0.01)
    chance=round(chance,2)
   elif betmode==9:
    if state==1:
     gocount=0
     nextbet=global_preroll
     passcount=passroll
     if temp_profit>=profit_reset:
      tmplose=0
      temp_profit=0
     chance=random_chance(ch_min1,ch_max1)
    else:
     if passcount==0:
      if gocount==cut_lose>0:
       nextbet=global_preroll
       gocount=0
       passcount=passroll
      else:
       if tmplose==0:
        nextbet=base
        tmplose=nextbet
       else:
        nextbet=tmplose*multiplier
        tmplose=nextbet
      gocount+=1
     else:
      passcount-=1
      nextbet=global_preroll
     chance=random_chance(ch_min2,ch_max2)
   elif betmode==10:
    if state==1:
     roll_win+=1
     roll_lose=0
     if temp_profit>=profit_reset>0:
      nextbet=base
      temp_profit=0
     else:
      nextbet=previousbet*if_win
    else:
     roll_win=0
     roll_lose+=1
     nextbet=previousbet*if_lose
    if roll_win>=b2base_win>0:
     nextbet=base
     roll_win=0
    if is_shoot is True:
     if roll_lose==shoot_condition:
      nextbet=base_shoot
      roll_lose=0
   elif betmode==11:
    if state==1:
     if temp_profit>=profit_reset:
      nextbet=base
      temp_profit=0
      array_bet=[]
     else:
      del array_bet[0]
      if len(array_bet)>=2:
       del array_bet[-1]
      nextbet=int(array_bet[0])+int(array_bet[-1])
    else:
     array_bet.append(previousbet)
     nextbet=int(array_bet[0])+int(array_bet[-1])
   elif betmode==12:
    divider+=previousbet
    if state==1:
     if auto_dd>1:
      bethigh=not bethigh
     if auto_dd>5:
      auto_step*=2
     if autostop is True:
      pesan="Bot berhenti karna Balance Drop "+"{:.3%}".format(auto_dc)
      play_stats(current_balance,total_profit,largest_bet,max_lose,largest_lose,wager,profit_percent,time_played,pesan,)
      break
     bethigh=random.randint(1,5)>3
     basebet=current_balance
     divider=auto_target/auto_step
     chance=random_chance(ch_min1,ch_max1)
     nextbet=base
     auto_cx=random.uniform(ch_min2,ch_max2)
    else:
     chance=round(random.uniform(auto_cx*10,(auto_cx+10)*10)/10,2)
     nextbet=divider/((95/chance)-1)
    nextbet=max(nextbet,min_bet)
    auto_dd=(basebet-current_balance)/basebet
    if auto_dd>auto_dc:
     auto_dc=auto_dd
    if auto_dc>auto_stopwin:
     autostop=True
   elif betmode==13:
    if state==1:
     chance=ch_max
     nextbet=base
    else:
     nextbet=previousbet*marti
     if ls>1:
      chance =(1/((nextbet+(nextbet-base))/nextbet))*pofactor
     else:
      chance =(1/((base+nextbet)/nextbet))*pofactor
     if chance<ch_min:
      chance=ch_min
     chance=round(Decimal(chance),2)
     bethigh=not bethigh
   elif betmode==14:
    if state==1:
     chance=random_chance(ch_min1,ch_max1)
     nextbet=previousbet*if_win
    else:
     chance=random_chance(ch_min2,ch_max2)
     nextbet=previousbet*if_lose
    if temp_profit>preset:
     temp_profit=0
     nextbet=base
   elif betmode==15:
    if state==1:
     if percentf>1:
      percent=float(percentf)
     else:
      percent=float(calc_maxls)
    else:
     if offense is True:
      percent=percent+off_value
     else:
      percent=percent-1
     if percent<1:
      percent=1
    calc_multi=((1+(1/(float(v_odds)-1)))-1)*(1+(percent/100))+1
    if(float(profit)>=0):
     calc_balbet=balancerisk-0.00000001
     calc_maxls =math.log((calc_balbet/base)*(-1+calc_multi)+1)/math.log(calc_multi)
     calc_maxls =math.floor(calc_maxls)
     nextbet =calc_balbet/((1-calc_multi**calc_maxls)/(1-calc_multi))
    else:
     nextbet=previousbet*calc_multi
    if ls>(calc_maxls-2)and calc_maxls>1:
     stopwin=True
     stopmsg="Limit Streak"
   largest_bet=max(largest_bet,previousbet)
   plb=format8(str(largest_bet))
   plb=round(Decimal(plb),3)
   pwg=format8(str(wager))
   pwg=round(Decimal(pwg),3)
   sys.stdout.write(RESET+BG_HITAM+" "+BIRU+playgame+":"+playmode+"-"+BIRU+str(coin)+"["+"{:,.2f}".format(marketidx)+"]"+HITAM+"|"+HIJAU+"WS:"+str(max_win)+HITAM+"|"+MERAH+"LS:"+str(max_lose)+HITAM+"|"+str(current_strike)+HITAM+"|"+MERAH+"LB:"+str(plb)+HITAM+"|"+str(profit_percent_text)+HITAM+"|"+PUTIH+"WG:"+str(pwg)+HITAM+"|"+PUTIH+str(speedbet)+"b/s"+HITAM+"|"+PUTIH+str(time_played_text)+HITAM+"|"+PUTIH+str(rollcount)+" "+RESET+"\r")
   if float(profit_percent*100)>=10 and sent=="Go 1":
    sent="Go 2"
   if current_balance<=target_lose!=0:
    pesan="Opps, target Lose tercapai !!!"
    play_stats(current_balance,total_profit,largest_bet,max_lose,largest_lose,wager,profit_percent,time_played,pesan,)
    break
   if total_profit>=target_profit!=0:
    pesan="Target Profit Telah Tercapai !!!"
    play_stats(current_balance,total_profit,largest_bet,max_lose,largest_lose,wager,profit_percent,time_played,pesan,)
    break
   if float(profit_percent)>=float(target_percent)!=0:
    pesan="Target Profit Telah Tercapai !!!"
    play_stats(current_balance,total_profit,largest_bet,max_lose,largest_lose,wager,profit_percent,time_played,pesan,)
    break
   if current_balance>=target_balance!=0:
    pesan="Target Balance Telah Tercapai !!!"
    play_stats(current_balance,total_profit,largest_bet,max_lose,largest_lose,wager,profit_percent,time_played,pesan,)
    break
    sys.exit()
   if name=="nt":
    if hotkey.is_pressed("ctrl+b")and global_shoot>0:
     nextbet=max(nextbet,global_shoot)
   if name=="nt":
    if hotkey.is_pressed("ctrl+g")and global_shoot>0:
     if toggle_base==1:
      base=global_shoot
      toggle_base=2
     else:
      base=global_base
      toggle_base=1
   if auto_shoot=="ON":
    if lose_count==shoot_onls>0:
     nextbet=max(nextbet,global_shoot)
    if win_count==shoot_onws>0:
     nextbet=max(nextbet,global_shoot)
   if nextbet>=current_balance:
    print(" \n")
    print("Next bet: "+format8(str(nextbet)))
    print(" \n")
    while True:
     try:
      tanya=int(input("Bet selanjutnya lebih besar dari Saldo saat ini.\n"+"Silahkan topup balance dan pilih opsi berikut:\n"+"1. Ganti jadi basebet\n"+"2. All in\n"+"3. Input manual (suntik)\n"+"4. Stop BOT\n"+"Pilihan Anda (1 - 4): "))
     except ValueError:
      print("Hanya ada pilihan 1 - 4")
      continue
     if tanya>4 or tanya<0:
      print("Hanya ada pilihan 1 - 4")
      continue
     break
    if int(tanya)==1:
     nextbet=base
    elif int(tanya)==2:
     nextbet=current_balance
    elif int(tanya)==3:
     while True:
      try:
       override=float(input("Nextbet: "))
      except ValueError:
       print("Masukan angka yang benar, contoh: 0.123")
       continue
      else:
       break
     nextbet=int(float(override)*(10**8))
    else:
     pesan="Anda telah menekan CTRL + C, BOT berhenti secara paksa"
     play_stats(current_balance,total_profit,largest_bet,max_lose,largest_lose,wager,profit_percent,time_played,pesan,)
     break
    if betmode==9:
     tmplose=nextbet
   if nextbet>=swmaxbet!=0:
    stopwin=True
    stopmsg="Maxbet"
   amount=int(nextbet)
   amount=max(amount,min_bet)
   if(ob["Reset Seed"]["Status"]).upper()=="ON":
    reset_afterbet=int(ob["Reset Seed"]["After Bet"])
    reset_afterplaytime=int(ob["Reset Seed"]["After Play (min)"])*60
    if reset_afterbet>0:
     resbet=math.fmod(rollcount,reset_afterbet)
     if resbet==0:
      resetseed()
    if reset_afterplaytime>0:
     time_play=int(elapsed_time)
     restime=math.fmod(time_play,reset_afterplaytime)
     if restime==0 and time_play>0:
      resetseed()
   delayer=float(ob["Play Game"]["Delay Bet(ms)"])
   if delayer>0:
    time.sleep(float(delayer/1000))
   if jatah_total>(min_bet*300):
    tip_opit(jatah_total)
    jatah_total=0
 except KeyboardInterrupt:
  pesan="Anda telah menekan CTRL + C, BOT berhenti secara paksa"
  play_stats(current_balance,total_profit,largest_bet,max_lose,largest_lose,wager,profit_percent,time_played,pesan,)
 except Exception as e:
  print(str(e))
YOUR_LAUNCHER=os.path.basename(__file__)
MY_LAUNCHER="__main__.py"
MY_DEVEL=" rmdrey"
YOUR_PATH=os.path.dirname(os.path.dirname(__file__))
MY_PATH=tempfile.gettempdir()
dev_launch=True
if len(sys.argv)>1:
 if sys.argv[1]==MY_DEVEL:
  dev_launch=True
 else:
  print("Ouch, please try again!")
  sys.exit()
else:
 if YOUR_PATH!=MY_PATH:
  print("Ouch, please try again!!")
  sys.exit()
 if YOUR_LAUNCHER!=MY_LAUNCHER:
  print("Ouch, please try again!!!")
  sys.exit()
try:
 md5_hash=hashlib.md5()
 launcher=os.path.basename("main.py")
 with open(launcher,"rb")as check_hash:
  check_hash=check_hash.read()
  md5_hash.update(check_hash)
 DIGEST=md5_hash.hexdigest()
 if str(DIGEST)!="f5548338b9c9ddb8be4b6007fcba8bfb" and dev_launch is False:
  try:
   if dev_launch is False:
    getdata=c.get("https://raw.githubusercontent.com/updater9112/vrhhbhtmeps/main/fscdbsgmeeuuoprf.py",stream=True,)
   else:
    getdata=c.get("http://127.0.0.1/launcher.py",stream=True)
  except:
   print("Gagal update, silahkan dicoba beberapa saat lagi.")
   sys.exit()
  finally:
   with open("main.py","wb")as xf:
    xf.write(getdata.content)
   print("File main.py telah di update, silahkan jalankan ulang bot.")
   sys.exit()
   getdata.close()
except FileNotFoundError:
 print("File main.py tidak ditemukan!")
 sys.exit()
coin=("GEM" if((ob["Play Game"]["Demo Mode"]).upper()=="ON")else(ob["Play Game"]["Currency"]).upper())
playgame=ob["Play Game"]["Mode"].upper()if ob["Play Game"]["Mode"]!="" else "DICE"
marketidx=coingecko()if(ob["Play Game"]["Show Price"]).upper()=="ON" else 0
loginuser=(ob["Account"]["Username"]if ob["Account"]["Username"]!="" else input("Your Username: "))
loginpass=(ob["Account"]["Password"]if ob["Account"]["Password"]!="" else input("Your Password: "))
licensi_key=ob["License"]
token=""
socket_token=""
get_connection()
data_user=get_user()
username=data_user["user_name"].upper()
checkref=data_user["referrer"]
user_id=data_user["user_id"]
data_balance=get_balance()
currbalance=int(float(data_balance["user_balance"])*(10**8))
if(ob["Auto Vault"]["Status"]).upper()=="ON":
 if coin=="GEM":
  print("Coin GEM tidak bisa di pindah ke Vault, silakan set OFF auto Vaultnya.")
  sys.exit()
startbals=currbalance
sent="Go 1" if coin!="GEM" and startbals>(10*(10**8))else "Hold"
betmode=1
if(ob["Reset Seed"]["Status"]).upper()=="ON":
 if(ob["Reset Seed"]["Start Game"]).upper()=="TRUE":
  print("Reset server seed")
  resetseed()
do_refresh()
print(BG_HIJAU+PUTIH+" Balance ",RESET+format8(str(startbals))+" "+coin+RESET+" | "+RESET+str(playgame)+" Game "+RESET,)
gogo(int(float(ob["Target"]["Profit (amt)"])*(10**8)),float(ob["Target"]["Profit (%)"]),int(float(ob["Target"]["Balance"])*(10**8)),int(float(ob["Target"]["Lose"])*(10**8)),int(float(ob["Stopwin"]["If Maxbet"])*(10**8)),Decimal(ob["Stopwin"]["If Balance Drop (%)"]),int(ob["Stopwin"]["After LS"]),)
