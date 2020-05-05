import platform
import os
import time
import uuid
# import time
import datetime
import socket

UUID = uuid.uuid4()
check_os = platform.system()
check_version = platform.version()

support = "www.NovaOSTechnology.com"
Referral = "www.twilio.com/referral/bFkIkX"
config_version = '3.0'
System_version = '3.0'
database = '1.0'
Developer = 'NovaOS Technology'
get_name = socket.gethostname()
ip = socket.gethostbyname(get_name)
Copy_right = ['Copyright © 2020 NovaOS',
              'Copyright © 2020 NovaOS Technology']

auto_update = "https://raw.githubusercontent.com/DJNovaTech/Nexus-Phone-bot/master/Version.txt"
SysTime = time.ctime().split(" ")

file_path = "C:/NovaOS/Modules/NexusPhoneBot"
conf_path = "C:/NovaOS/Modules/NexusPhoneBot/config.ini"
database_path = "C:/NovaOS/Modules/NexusPhoneBot/database"
log = "C:/NovaOS/Modules/NexusPhoneBot/Logs/Log.txt"
img_path = "C:/NovaOS/Modules/NexusPhoneBot/img"

database_file_path = "C:/NovaOS/Modules/NexusPhoneBot/database/System.db"
log_path = "C:/NovaOS/Modules/NexusPhoneBot/Logs"

CloseSys = ['e', 'EXIT', 'exit', 'E', 'exi', 'end', 'exi', 'b', 'B', 'BACK', 'n', 'N']

NetworkError = ['<urlopen error [Errno 11001] getaddrinfo failed>']

MenuSelection = {
    "Main_1": "[1] - SMS Attacks",
    "Main_2": "[2] - Voice Attacks",
    "Main_3": "[3] - Custom Attacks",
    "Main_4": "[4] - Beta Attacks",
    "Main_5": "[5] - Number Search",
    "Main_6": "[6] - Settings/Options",
    "Main_quit": "[E] - Exit System",

    "SMS_1": "[1] - Basic SMS Attack",
    "SMS_2": "[2] - Advanced SMS Attack",
    "SMS_3": "[3] - Emoji Attack v2",
    "SMS_4": "[4] - IRL Attack",
    "SMS_back": "[B] - Back",

    "Voice_1": "[1] - Basic Voice Attack",
    "Voice_2": "[2] - Advanced Voice Attack",
    "Voice_3": "[3] - Music Attack",
    "Voice_4": "[4] - Mad Max Attack",
    "Voice_back": "[B] - Back",

    "Custom_1": "[1] - Custom Voice Attack",
    "Custom_2": "[2] - Custom SMS Attack",
    "Custom_3": "[3] - Custom Music Attack",
    "Custom_back": "[B] - Back",

    "Settings_1": "[1] - Reset Config",
    "Settings_2": "[2] - Referral Link",
    "Settings_3": "[3] - View System Update",
    "Settings_4": "[4] - Enable/Disable Settings",
    "Settings_5": "[5] - System Restart",
    "Settings_back": "[B] - Back",

    "Beta_1": "[1] - MMS Attack-0.0.1",
    "Beta_2": "[2] - N/A",
    "Beta_3": "[3] - N/A",
    "Beta_4": "[4] - N/A",
    "Beta_back": "[B] - Back"}


system_path = [
    os.path.exists(file_path),
    os.path.exists(conf_path),
    os.path.exists(database_path),
    os.path.exists(database_file_path),
    os.path.exists(log_path),
    os.path.exists(img_path)]

check_help = ['h', 'Help', 'help', 'HELP', 'H']

console_help = """
SimpleMode Command list | v3.0.0
-----------------------------------------------
V - Voice Attacks | EX: v -attack <Attack Type>
S - SMS Attacks   | EX: S -attack <Attack Type>
C - Custom Attack | EX: C -attack <Attack Type>
B - Beta Attacks  | EX: B -attack <Attack Type>
BL - Beta Attack List - Shows all beta attacks.
AL - Attack List - Shows all attack types.

Login - Allows you to login the system.
chuser - Switch user accounts.
Settings - Change system settings (-set/-list) | EX: Settings -set <Modules> <Value>
Lock - Locks System based off pin you set (Note Admin pin can overwrite)
-----------------------------------------------"""

NexusPB = f"""
                _   __
               / | / /__  _  ____  _______
              /  |/ / _ \| |/_/ / / / ___/
             / /|  /  __/>  </ /_/ (__  )
            /_/ |_/\___/_/|_|\__,_/____/
                    (Phone Bot)
           -----------------------------                                 
   [*] Made by: Dillon Sherwood | NovaOS Technology
   [*] Support: NovaOSTechnology.come/Support
   [*] Version: - {System_version} | Config Version - {config_version}
      ({Copy_right[1]})
                                        
"""

crash_logo = f"""
              _   _                    _    ___ 
             | \ | | _____   ____ _   / \  |_ _|
             |  \| |/ _ \ \ / / _` | / _ \  | | 
             | |\  | (_) \ V / (_| |/ ___ \ | | 
             |_| \_|\___/ \_/ \__,_/_/   \_\___|             
               (A NovaOS Technology Program)
               
         Oh No the system has crashed. Those Bugs got, 
        into the wires again ! To help fix this issue 
        we created a log file ! The log can be found below
        -------------------------------------------------
        [*] ({log_path}) 
        [*] Support | (NovaOSTechnology.com/support)
        [*] Version | {System_version}
        [*] {SysTime[0]} | {SysTime[1]},{SysTime[3]} | {SysTime[4]}
"""

NovaAI = f"""
              _   _                    _    ___ 
             | \ | | _____   ____ _   / \  |_ _|
             |  \| |/ _ \ \ / / _` | / _ \  | | 
             | |\  | (_) \ V / (_| |/ ___ \ | | 
             |_| \_|\___/ \_/ \__,_/_/   \_\___|             
               (A NovaOS Technology Program)
               
         Oh No the system has crashed. Those Bugs got, 
        passed the firewall! No Log file was created. 
        NovaAI has created its own log. Please contact,
               Support to help fix this bug.
        (Please copy and paste your config to pastebin)
        -------------------------------------------------
        [*] {conf_path} | ({system_path[1]}) 
        [*] Support | (NovaOSTechnology.com/support)
        [*] Version | {System_version}
        [*] OS: {check_os}
        [*] UUID: N/A
        [*] Conf Version: {config_version}
        [*] {SysTime[0]} | {SysTime[1]},{SysTime[3]} | {SysTime[4]}
        [*] Log-Path: {log_path}
        [*] IP Address: {ip}
        [*] Hostname: {get_name}
        [*] voIP: False/Disabled
"""

MainMenu_Icon = """
  __  __      _        __  __              
 |  \/  |__ _(_)_ _   |  \/  |___ _ _ _  _ 
 | |\/| / _` | | ' \  | |\/| / -_) ' \ || |
 |_|  |_\__,_|_|_||_| |_|  |_\___|_||_\_,_|
"""
SMSMenu_Icon = """
  ___ __  __ ___   __  __              
 / __|  \/  / __| |  \/  |___ _ _ _  _ 
 \__ \ |\/| \__ \ | |\/| / -_) ' \ || |
 |___/_|  |_|___/ |_|  |_\___|_||_\_,_|
                                       """
VoiceMenu_Icon = """
 __   __   _          __  __              
 \ \ / /__(_)__ ___  |  \/  |___ _ _ _  _ 
  \ V / _ \ / _/ -_) | |\/| / -_) ' \ || |
   \_/\___/_\__\___| |_|  |_\___|_||_\_,_|
                                          """
CustomMenu_Icon = """
   ___        _               __  __              
  / __|  _ __| |_ ___ _ __   |  \/  |___ _ _ _  _ 
 | (_| || (_-<  _/ _ \ '  \  | |\/| / -_) ' \ || |
  \___\_,_/__/\__\___/_|_|_| |_|  |_\___|_||_\_,_|
  """
BetaMenu_Icon = """
  ___      _          __  __              
 | _ ) ___| |_ __ _  |  \/  |___ _ _ _  _ 
 | _ \/ -_)  _/ _` | | |\/| / -_) ' \ || |
 |___/\___|\__\__,_| |_|  |_\___|_||_\_,_|
"""
SettingsMenu_Icon = """
  ___      _   _   _              
 / __| ___| |_| |_(_)_ _  __ _ ___
 \__ \/ -_)  _|  _| | ' \/ _` (_-<
 |___/\___|\__|\__|_|_||_\__, /__/
                         |___/    
"""