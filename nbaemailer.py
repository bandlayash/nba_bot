import csv
import pyautogui
import time

time.sleep(2)

with open('teamemails.csv', newline='') as csvfile:
    emails = list(csv.reader(csvfile))

with open('teamnames.csv', newline='') as csvfile:
    names = list(csv.reader(csvfile))
    
x = 0 #startine
i = 499 #endline
while x <= i:
    time.sleep(1)
    pyautogui.click(x= , y= ) #FILL IN X,Y values of compose button from position.py click on compose
    time.sleep(0.3)
    pyautogui.write(emails[x][0]) #write name into receipient field
    time.sleep(0.3)
    pyautogui.press('enter')
    pyautogui.press('tab') #tab to subject line
    time.sleep(0.3)
    pyautogui.write("An Odd Request for the ") #Writing on subject line
    pyautogui.write(names[x][0]) #Writing on subject line
    pyautogui.write(" today") #Writing on subject line
    time.sleep(0.3)
    pyautogui.press('tab') #tab to email body
    time.sleep(0.3)
    pyautogui.write("Hi there, my name is ENTER_NAME and I am a fan from ENTER_CITY, ENTER_STATE. I have been a big fan of the ") #Writing on email body
    pyautogui.write(names[x][0]) #Writing on email body
    pyautogui.write(" for a while now. Honestly, I think they are my favorite team right now! I'm sure you get a lot of these requests, but I was wondering if there is any chance I could receive a sticker, flag, shirt or really anything you guys are able to offer me! I would love to start representing my team pride as early as possible. If you guys are able to help me out, my address is ENTER_ADDRESS I am looking forward to seeing them playing again!") #Writing on email body
    time.sleep(0.3)
    pyautogui.press('enter') #paragraph break
    time.sleep(0.3)
    pyautogui.press('enter') #paragraph break
    time.sleep(0.3)
    pyautogui.write("All the best, ENTER_NAME.") #Writing on email body
    pyautogui.hotkey('ctrl', 'enter') #hotkey send email
    x = x + 1
