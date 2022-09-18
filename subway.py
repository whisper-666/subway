import os
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
W='\033[1;37m'
os.system('clear')
print(f'''{B}{W}============{B}WHISPER{W}============
{G}[+] GitHub   : {B}@whisper-666
{G}[+] FaceBook : {B}@BoyFtn
{G}[+] TeleGram : {B}@WhisperIO''')
path='/sdcard/Android/data/com.kiloo.subwaysurf/files/profile/wallet.json'
try:
 whisper=str(open(path,'r').read())
except FileNotFoundError:
 exit(f'{E}[×] Please Download The Game First')
try:
 sky=whisper.split('{\\"value\\":')[1].split(',')[0]
 keys=whisper.split('{\\"value\\":')[2].split(',')[0]
 ft=whisper.split('{\\"value\\":')[3].split(',')[0]
 sb=whisper.split('{\\"value\\":')[4].split(',')[0]
 coin=whisper.split('{\\"value\\":')[5].split(',')[0]
except IndexError:
 exit(f'{E}[×] Play Some Time First')
print(f"""{B}{W}============{B}WHISPER{W}============
{G}[🗝️] Keys {S}==> {B}{keys}
{W}============{B}WHISPER{W}============
{G}[👛] Coins {S}==> {B}{coin}
{W}============{B}WHISPER{W}============
{G}[🎿] SkyBoard {S}==> {B}{sky}
{W}============{B}WHISPER{W}============
{G}[⭐] Score Booster {S}==> {B}{sb}
{W}============{B}WHISPER{W}============
{G}[🚀] Fly Thing {S}==> {B}{ft}""")
print(f'{W}============{B}WHISPER{W}============')
hack=input(f'{G}[+] Wanna Hack It ?? {S}({B}y{S}/{E}n{S}) : {S}')
print(f'{W}============{B}WHISPER{W}============')
if 'y' in hack or 'Y' in hack:
 os.system('mv wallet.json /sdcard/Android/data/com.kiloo.subwaysurf/files/profile/')
 print(f'''{G}[√] Hacked Successfully''')
else:
 exit(f'{E}[×] Okay')