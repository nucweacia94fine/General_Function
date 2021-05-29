# -*- coding: utf-8 -*-
"""
Created on Sat May 29 17:18:51 2021

@author: NtRdeMtrX
"""

#######################################################################################################
def isexist(var_str:str): # only global varaible
    try: 
        type(eval(var_str)) 
    except: 
        #print(f"{var_str} is NOT exist.")
        return False
    else: 
        #print(f"{var_str} is exist.")
        return True 

#######################################################################################################    
import datetime
from datetime import timedelta
def date_range(start:datetime ,stop:datetime ,step:timedelta):
    while start < stop :        
        yield start
        start += step

#######################################################################################################
import os
import win32api
def Process_EXEing(ProcName):
    from win32com.client import GetObject
    WMI = GetObject("winmgmts:")
    process = WMI.InstancesOf('Win32_Process')
    ProcNames = []
    #print len(process) #將註解打開的話，就會列印出本機正在執行的Process數量 。
    for p in process:
        #print(p.Properties_('Name').Value) #將註解打開的話，就會列印出每個Process 的檔案名稱。
        ProcNames.append(p.Properties_('Name').Value)
 
    if (ProcName in ProcNames):
        return True
    else:
        return False
    
#######################################################################################################
if __name__ == "__main__": 
    print(Process_EXEing("NTPClock.exe"))
    print(list(date_range(datetime.date(2021, 5, 20), datetime.date(2021, 5, 29), timedelta(days=1))))
    print(isexist(""))