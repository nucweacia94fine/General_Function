#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import time as T_module
import datetime

IP = '203.66.91.161' #example'
os.system('chcp 65001') # Switch to unicode (UTF-8)
response = os.system("ping -w 1 -n 1 " + IP + '> pingRecord_temp.txt')

f_temp = open('pingRecord_temp.txt','r')
response_string = f_temp.read()
f_temp.close()

#print(response_string) 
response_split = response_string.replace("\n"," ").replace(", "," ").replace(" = "," ").split(" ")
while '' in response_split:
    response_split.remove('')
#print(response_split)

i = 0
while response_split[i] != 'Received' or i == len(response_split):
    i = i+1
socket_receive = int(response_split[i+1]) > 0
j = 0
while response_split[j] != 'Lost' or j == len(response_split):
    j = j+1
socket_lost = int(response_split[j+1]) > 0

print(response_string) 
print("============================================")
print(f"Socket receive: {socket_receive}")
print(f"Socket lost: {socket_lost}")
T_now = datetime.datetime.now() 
T_today_str = '{:04d}{:02d}{:02d}'.format(T_now.year,T_now.month,T_now.day) 

if not socket_receive and socket_lost:    
    if ping_Err_count >= 3:
        print(T_now)
        print("Ping Error Occur!!!")
        f_ping = open('pingError_' + T_today_str + '.txt','a', encoding = 'utf-8')
        print(T_now, file = f_ping)
        print(response_string, file = f_ping)
        print("--------------------------------------------", file = f_ping)
        print(f"Socket receive: {socket_receive}", file = f_ping)
        print(f"Socket lost: {socket_lost}", file = f_ping)
        print("============================================", file = f_ping)
        f_ping.close()
        print("System sleep for 1 minute")
        T_module.sleep(60)                
    else:                
        print(T_now)
        print("Ping Error Occur!!!")
        ping_Err_count = ping_Err_count + 1
else:            
    f_ping = open('pingRecord.txt','w', encoding = 'utf-8')
    print(T_now, file = f_ping)
    print(response_string, file = f_ping)
    print("--------------------------------------------", file = f_ping)
    print(f"Socket receive: {socket_receive}", file = f_ping)
    print(f"Socket lost: {socket_lost}", file = f_ping)
    print("============================================", file = f_ping)
    f_ping.close()
    ping_Err_count = 0

