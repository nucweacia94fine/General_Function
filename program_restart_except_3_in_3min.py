#!/usr/bin/env python
# coding: utf-8

# In[25]:


import datetime
import time as T_module
import win32api

import sys
import traceback 
import test

def nest2():
    test.run()

def main():
    nest2()
    
record_filename = "Error_record_file.txt"

if __name__=="__main__":
    sys_error_count = 0  
    DT_error2 = datetime.datetime.now()
    while True:
        try:
            main()
        except Exception as e:
            cl, exc, tb = sys.exc_info() #取得Call Stack
            DT_error = datetime.datetime.now()
            print("")       
            print(f"This error occurred time: {DT_error.replace(microsecond = 0)}")
            print(f"Last error occurred time: {DT_error2.replace(microsecond = 0)}")
            print("---------------------------------------------------------------------")
            print(f"main() error due to: {type(e)}")
            #print(e)
            #print("")
            #print(traceback.extract_tb(tb))
            
            f_rcd = open(record_filename, "a", encoding='utf-8')
            print("", file = f_rcd)
            print(f"This error occurred time: {DT_error.replace(microsecond = 0)}", file = f_rcd)
            print(f"Last error occurred time: {DT_error2.replace(microsecond = 0)}", file = f_rcd)
            print("---------------------------------------------------------------------", file = f_rcd)
            print(f"main() error due to: {type(e)}", file = f_rcd)
            
            #lastCallStack = traceback.extract_tb(tb)[-1] #取得Call Stack的最後一筆資料
            for lastCallStack in traceback.extract_tb(tb): # 依序取得Call Stack的所有資料
                err_fileName = lastCallStack[0] #取得發生的檔案名稱
                err_lineNum = lastCallStack[1] #取得發生的行號
                err_funcName = lastCallStack[2] #取得發生的函數名稱
                err_Msg = f"\nFile \"{err_fileName}\",\n--> line {err_lineNum}, in {err_funcName}:"
                # Ref.[1]     
                print(err_Msg)
                print(err_Msg, file = f_rcd)
            print(f"[{type(e)}]: {e.args[0]}")
            print(f"[{type(e)}]: {e.args[0]}", file = f_rcd)
            f_rcd.close()
            
            if sys_error_count == 2: 
                print("\n!!!   Error occurred too many times in 3 minutes. !!!\n")
                print("=====================================================================")
                
                f_rcd = open(record_filename, "a", encoding='utf-8')
                print("\n!!!   Error occurred too many times in 3 minutes. !!!\n", file = f_rcd)
                print("=====================================================================", file = f_rcd)
                f_rcd.close()
                raise;
            else:
                print("=====================================================================")
                f_rcd = open(record_filename, "a", encoding='utf-8')
                print("=====================================================================", file = f_rcd)
                f_rcd.close()               
                if e.args[0] == 28: # 硬碟容量不足
                    win32api.ShellExecute(0, 'open', '釋放C槽空間.bat', '','',1)
                
                if DT_error2 + datetime.timedelta(minutes = 3) < DT_error:
                    sys_error_count = 0
                else:
                    sys_error_count = sys_error_count + 1  
                DT_error2 =  DT_error
                T_module.sleep(5)
            

# Ref: 
# [1]. https://dotblogs.com.tw/caubekimo/2018/09/17/145733

