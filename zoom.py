import time
import pyautogui
import datetime
from env import schedule

def getClassDuration(startTime, endTime):
    return ((int(endTime[0])-int(startTime[0]))*60 + (int(endTime[1])-int(startTime[1])))*60

def prepareForClass(startTime, classID, classDuration):
    print("Aguardo o horário da aula ("+startTime[0]+":"+startTime[1]+")...")
    while True:
        if int(datetime.datetime.now().hour) == int(startTime[0]) and int(datetime.datetime.now().minute) == int(startTime[1]):
            print("Entrando na aula...")
            autozoom(classID, classDuration)
            print("Saindo da aula...")
            break
        else:
            time.sleep(30)

def autozoom(classID, classDuration):
    pyautogui.hotkey('alt', 'f2')
    time.sleep(5)
    pyautogui.write('zoom')
    pyautogui.press('enter', interval=0.5)
    time.sleep(5)
    x_c, y_c = pyautogui.locateCenterOnScreen('img/join.png', confidence=0.9)
    time.sleep(5)
    pyautogui.click(x_c, y_c)
    time.sleep(5)
    x_s, y_s = pyautogui.locateCenterOnScreen('img/s3.png', confidence=0.9)
    pyautogui.click(x_s, y_s)
    pyautogui.write(classID)
    time.sleep(5)
    x_s, y_s = pyautogui.locateCenterOnScreen('img/s2.png', confidence=0.9)
    pyautogui.click(x_s, y_s)
    time.sleep(5)
    x_s, y_s = pyautogui.locateCenterOnScreen('img/s1.png', confidence=0.9)
    pyautogui.click(x_s, y_s)
    pyautogui.press('enter', interval=5)
    print('Hold (Ctrl+c) to exit the program ')
    time.sleep(classDuration)
    pyautogui.hotkey('alt', 'f4')
    time.sleep(0.5)
    pyautogui.hotkey('alt', 'f4')

if input("Executar em modo único? (y/n)\n").lower() == "y":
    classID = input("Insira o ID da aula: \n")
    startTime = input('Insira o horário de início da aula "HH:MM": \n').split(":")
    endTime = input('Insira o horário de término da aula "HH:MM": \n').split(":")
    prepareForClass(startTime, classID, getClassDuration(startTime, endTime))
else:
    while True:
        weekday = datetime.datetime.today().weekday()
        while True:
            for scheduledClass in schedule[weekday]:
                if (int(scheduledClass[1][0]) > int(datetime.datetime.now().hour)) or (int(scheduledClass[1][0]) == int(datetime.datetime.now().hour) and int(scheduledClass[1][1]) > int(datetime.datetime.now().minute)):
                    nextClass = scheduledClass
                    break
            if nextClass != None:
                prepareForClass(nextClass[1], nextClass[0], getClassDuration(nextClass[1], nextClass[2]))
            else:
                weekday += 1
                if weekday >= 7:
                    weekday -= 7