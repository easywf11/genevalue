#Name:          metric_3qv.py
#Functions:     测试基因文件的组装质量
#Parameter In： ？
#Parameter Out: 
#Remarks:       ？

#%% =========================================      import libs            ===========================================
import time
import keyboard
import mouse
import sys


#%% =========================================      ppt 1 level titile        ===========================================
#功能：    实现1级标题的格式及位置操作
#热键：    Alt +1

def ppt_title_big():
    print(' -> This function to make ppt_title_big.')    
    time.sleep(1)
    
    #fixed the box to a new position
    mouse.right_click()
    keyboard.send('z')
    
    
    1283,249
    
    print('hello!')
    
#%% =========================================      ppt 2 level titile        ===========================================
#功能：    实现1级标题的格式及位置操作
#热键：    Ctrl +1

def ppt_title_small():
    print('hello， ppt_title_small!')
    
    time.sleep(3)
    
    print('hello!')


#%% =========================================      ppt main text big format      ===========================================
#功能：    实现1级标题的格式及位置操作
#热键：    Ctrl +2

def ppt_text_big():
    print('hello，ppt_text_big !')
    
    time.sleep(3)
    
    print('hello!')

#%% =========================================      ppt main text big format      ===========================================
#功能：    实现1级标题的格式及位置操作
#热键：    Ctrl +2

def ppt_text_small():
    print('hello，ppt_text_small !')
    
    time.sleep(3)
    
    print('hello!')

#%% =========================================       main function        ===========================================
#功能：    常驻
#热键：    ctrl+0结束

while True:
    event = keyboard.read_event()   
    if keyboard.is_pressed('ctrl+1'):
        ppt_title_big()
    elif keyboard.is_pressed('ctrl+2'):
        ppt_title_small()
    elif keyboard.is_pressed('ctrl+0'):
        print('All done, Goodbye, my darling!')
        sys.exit()
    
    
    
    