import os
import socket
import platform
import psutil
from subprocess import check_output
import wmi
import sys

file_path = 'Report.txt'
sys.stdout = open(file_path , "w")
print('#'*50)
print('[+] Loading OPERATING SYSTEM DETAILS...')
print('#'*50)

print(f"Username : {os.getlogin()}")
print(f"Computer Name: {socket.gethostname()}")
print(f"Operating System: {platform.system()}")
print(f"Platform Version : {platform.platform()}")

print('-'*50)

print('#'*50)
print('[+] Loading  DLL DETAILS..')
print('#'*50)
p = psutil.Process(os.getpid())
for dll in p.memory_maps():
    print(dll.path)

print('-' *50)
print('#'*50)
print('[+] Loading  Environment...')
print('#'*50)
for k,v in sorted(os.environ.items()):
    print(k+':',v)
print('\n')
print('-' *50)
print('#'*50)
print('[+] Loading  ARP CACHE...')
print('#'*50)
try:
    lines = os.system('arp -a')
    for line in lines:
        print (line)
except:
    print("[*] WARNING NO LINE TO ITERATE")


print('#'*50)
print('[+] Loading  ACTIVE LOGONS...')
print('#'*50)
get_result = check_output("wmic netlogin get name,fullname,lastlogon",shell=True, stderr=False)
print(get_result)
clean_result = str(get_result).lstrip("b'").rstrip("'").replace("\\r\\r\\n", "\n").replace('\n\n', '\n').split('\n')[2:-1]
for items in clean_result:
    print(items.lstrip().rstrip())

print('-' *50)
print('#'*50)
print('[+] Loading  PID...')
print('#'*50)
# Initializing the wmi constructor
f= wmi.WMI()
print("pid     Process name  ")
for process in f.Win32_Process():
    print(f"{process.ProcessId:<10}  {process.Name} ")





