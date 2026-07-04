#!/usr/bin/env python3
import subprocess
import os
from os import system,name
import sys
import tempfile
import json
import time
import pkg_resources
PYTHON=sys.executable
PREFIX=" "+sys.argv[1]if len(sys.argv)>1 else ""
tmp=tempfile.NamedTemporaryFile(delete=False)
print("Menjalankan Bot....")
print("Hindari menyimpan password pada file settings.json demi keamanan....")
try:
 if name=="nt":
  required={"requests","colorama","websocket-client","websockets","keyboard"}
 else:
  required={"requests","colorama","websocket-client"}
 installed={pkg.key for pkg in pkg_resources.working_set}
 missing=required-installed
 if missing:
  try:
   print("Upgrade PIP...")
   subprocess.check_call([PYTHON,"-m","pip","install","--upgrade","pip"])
   print("Install missing module...")
   subprocess.check_call([PYTHON,"-m","pip","install",*missing])
  except KeyboardInterrupt:
   sys.exit()
  except:
   print("Silahkan install PIP terlebih dahulu")
   sys.exit()
except KeyboardInterrupt:
 sys.exit()
except Exception as e:
 print("Terjadi kesalahan, pesan error: "+str(e))
 sys.exit()
from colorama import Fore,Back,Style
import requests
r=requests.session()
obx={"License":"xxxxxxxxxxxx","Account":{"Username":"xxxxxxxxxxxx","Password":"xxxxxxxxxxxx"},"Play Game":{"Mode":"dice","Demo Mode":"ON","Currency":"btt","Show Price":"ON","Delay Bet(ms)":"0",},"Target":{"Profit (amt)":"0","Profit (%)":"1","Balance":"0","Lose":"0"},"Stopwin":{"On Profit":"True","If Maxbet":"0","If Balance Drop (%)":"0","After LS":"0",},"Repeat Play":{"Status":"OFF","Delay (sec)":"600"},"Auto Vault":{"Status":"OFF","Trigger Balance":"12000","Amount Vault":"10000",},"Auto Remove History":{"Status":"ON","Size Limit (MB)":"5"},"Reset Seed":{"Status":"OFF","Start Game":"False","After Bet":"1200","After Play (min)":"60",},"Bet Roll":{"Random":"False","Bet High":"False","Hi / Low":{"Toggle":"OFF","If Lose":"1","If Win":"1"},},"Bet Amount":{"Base":"0.1","Preroll Bet":"0.1","Shoot Bet":"1","Auto Shoot":{"Status":"OFF","After WS":"0","After LS":"0"},"Balance Divider":{"Status":"OFF","Divider":"5000000"},},"Betset":{"Sicepat":{"Toggle":"OFF","Profit Reset":"0.00000001","Chance Win":{"Min":"90","Max":"93"},"Chance Lose":{"Min":"7","Max":"20"},},"Sigesit":{"Toggle":"OFF","Profit Reset":"0.0085","Cut Lose":"2","Preroll":"0","Multipler":"2","Chance Win":{"Min":"90","Max":"91"},"Chance Lose":{"Min":"90","Max":"91"},},"Marti":{"Toggle":"ON","Chance":{"Min":"44","Max":"47"},"If Win":"1.08","If Lose":"1.7","Reset if profit":"0.001","Reset if win":"0","Reset if lose":"0","Reset if maxbet":"0",},"Preroll":{"Toggle":"OFF","Profit Reset":"0.00000001","Preroll":"3","Chance":{"Min":"30","Max":"33"},"If Win":"1","If Lose":"1.652",},"DAlembert Wannabe":{"Toggle":"OFF","Profit Reset":"0.0000001","Chance":{"Min":"32","Max":"36"},},"Fibonacci":{"Toggle":"OFF","Chance":{"Min":"32","Max":"36"},"Reset if profit":"0.0000001","Reset if win":"0","Reset if lose":"0","Reset if maxbet":"0",},"Labouchere":{"Toggle":"ON","Profit Reset":"0.0000001","Chance":{"Min":"32","Max":"37"},},"Wageran":{"Toggle":"OFF","Target Wager":"500","Wager":{"Base":"0.1","CHMin":"94.1","CHMax":"94.7"},"Recovery":{"Base":"0.001","CHMin":"20.1","CHMax":"24.5","If Win":"1","If Lose":"1.4","Preroll":"5","Reset if profit":"0.0000001",},},"Autobot":{"Toggle":"OFF","Payout":{"Min":"1.15","Max":"5"},"Risk (%)":"0.8","Reverse Logic":"False","Auto Calc":{"Status":"ON","Multipler":"1.35","Balance Divider":"500000",},},"Autobot-X":{"Toggle":"OFF","Bet Divider":"10000","Stopwin If Baldrop (%)":"50","Big Chance":{"Min":"80","Max":"90"},"Small Chance":{"Min":"5","Max":"15"},},"Autobot-S":{"Toggle":"OFF","Chance":"19.2","Multi Factor":"135","Balance Risk":"0.01"},"MinSa":{"Toggle":"OFF","Chance":{"Min":"47.5","Max":"92"},"Marti":"2.2"},"Stepstone":{"Toggle":"OFF","Chance Win":{"Min":"33","Max":"55","If Win":"1.106"},"Chance Lose":{"Min":"79","Max":"80","If Lose":"1.311"},"Reset if Profit":"0.00005"},"JumpJack":{"Toggle":"OFF","Reset Jump if Profit":"0","Reset Jump if Win":"0","Continuous Bet":"False","Mode":[{"Name":"Satu","Status":"ON","Base":"0.1","Balance Divider":{"Status":"OFF","Divider":"1000000","Recalculate on Play":"False",},"If Win":"1","If Lose":"1","Reset if profit":"0","Reset if win":"0","Reset if lose":"0","Reset if maxbet":"0","Chance":{"Min":"95","Max":"95"},"Kondisi Jump":{"After Bet":"100","Win Streak":"0","Lose Streak":"0","After Profit":"0","Next Win After Bet":"0",},},{"Name":"Dua","Status":"ON","Base":"0.1","Balance Divider":{"Status":"ON","Divider":"100000","Recalculate on Play":"True",},"If Win":"1","If Lose":"2.1","Reset if profit":"0.0000001","Reset if win":"0","Reset if lose":"0","Reset if maxbet":"0","Chance":{"Min":"49.5","Max":"49.5"},"Kondisi Jump":{"After Bet":"0","Win Streak":"0","Lose Streak":"0","After Profit":"0","Next Win After Bet":"50",},},],},},}
try:
 with open("settings.json","r",encoding="utf-8")as filesetup:
  data=filesetup.read()
except FileNotFoundError:
 print("File settings.json berhasil dibuat, silahkan ubah konfirgurasi")
 with open("settings.json","w",encoding="utf-8")as createsetting:
  json.dump(obx,createsetting,indent=4,sort_keys=False)
 sys.exit()
try:
 ob=json.loads(data)
except Exception as e:
 print("Kesalahan pada file settings.json, clue: "+str(e))
 sys.exit()
if ob["Auto Remove History"]["Status"].upper()=="ON":
 try:
  history_size=int(os.path.getsize("history_bet.txt"))
  history_limit=int(ob["Auto Remove History"]["Size Limit (MB)"])*1024*1024
  if history_size>=history_limit:
   os.unlink("history_bet.txt")
   print("File history_bet.txt telah dihapus")
   time.sleep(2)
 except:
  pass
with open("settings.json","w",encoding="utf-8")as updateconfig:
 obx["License"]=ob["License"]
 obx["Account"]=ob["Account"]
 obx["Play Game"]=ob["Play Game"]
 obx["Target"]=ob["Target"]
 obx["Stopwin"]=ob["Stopwin"]
 obx["Repeat Play"]=ob["Repeat Play"]
 obx["Auto Vault"]=ob["Auto Vault"]
 obx["Auto Remove History"]=ob["Auto Remove History"]
 obx["Reset Seed"]=ob["Reset Seed"]
 obx["Bet Roll"]=ob["Bet Roll"]
 obx["Bet Amount"]=ob["Bet Amount"]
 obx["Betset"]["Sicepat"]=ob["Betset"]["Sicepat"]
 obx["Betset"]["Sigesit"]=ob["Betset"]["Sigesit"]
 obx["Betset"]["Marti"]=ob["Betset"]["Marti"]
 obx["Betset"]["Preroll"]=ob["Betset"]["Preroll"]
 obx["Betset"]["DAlembert Wannabe"]=ob["Betset"]["DAlembert Wannabe"]
 obx["Betset"]["Fibonacci"]=ob["Betset"]["Fibonacci"]
 obx["Betset"]["Labouchere"]=ob["Betset"]["Labouchere"]
 obx["Betset"]["Wageran"]=ob["Betset"]["Wageran"]
 obx["Betset"]["Autobot"]=ob["Betset"]["Autobot"]
 obx["Betset"]["Autobot-X"]=ob["Betset"]["Autobot-X"]
 obx["Betset"]["Autobot-S"]=ob["Betset"]["Autobot-S"]
 obx["Betset"]["MinSa"]=ob["Betset"]["MinSa"]
 obx["Betset"]["Stepstone"]=ob["Betset"]["Stepstone"]
 obx["Betset"]["JumpJack"]=ob["Betset"]["JumpJack"]
 json.dump(obx,updateconfig,indent=4)
curr_file_name=os.path.basename(os.path.realpath(sys.argv[0]))
if str(PREFIX)!=" rmdrey":
 if curr_file_name!="main.py":
  os.unlink(curr_file_name)
RESET=Style.RESET_ALL
PUTIH=Style.BRIGHT+Fore.WHITE
BGRED=Style.BRIGHT+Back.RED+Fore.WHITE
try:
 if str(PREFIX)!=" rmdrey":
  getdata=r.get("https://raw.githubusercontent.com/updater9112/vrhhbhtmeps/main/cbxzjnspzzcrlals.py",stream=True,)
 else:
  getdata=r.get("http://127.0.0.1/dev.py",stream=True)
 req_status=getdata.status_code
 if str(req_status)!="200":
  print("Gagal menghubungi server, silahkan coba beberapa saat lagi.")
  sys.exit()
 tmp.write(getdata.content)
 tmp.seek(0)
 while True:
  if str(PREFIX)!=" rmdrey":
   subprocess.check_call([PYTHON,tmp.name])
  else:
   subprocess.check_call([PYTHON,tmp.name,PREFIX])
  try:
   IS_REPEAT=True if ob["Repeat Play"]["Status"].upper()=="ON" else False
   delay=int(ob["Repeat Play"]["Delay (sec)"])
   if IS_REPEAT is True:
    try:
     print("\n")
     for remaining in range(delay,0,-1):
      sys.stdout.write("\r")
      sys.stdout.write(RESET+BGRED+PUTIH+"Mulai bet lagi dalam {:2d} detik.".format(remaining)+RESET)
      sys.stdout.flush()
      time.sleep(1)
     print("\n")
     continue
    except KeyboardInterrupt:
     print("\n")
     print("Batal mengulang Bet")
     break
   break
  except:
   break
except KeyboardInterrupt:
 sys.exit()
except:
 sys.exit()
finally:
 tmp.close()
 os.unlink(tmp.name)
 getdata.close()
