#импортирование модулей
import map
#import translator
import pyttsx3
import speech_recognition as sr
import os
from fuzzywuzzy import fuzz
import subprocess 
import sys
import datetime
import win32com.client as wincl
import site
import calculator
import anekd
import webbrowser
import time
import re

import random
import sit
# import weth

#все опции васи
opts = {
    "namin": ('вася', 'василий', 'васька', 'вась'),
    "comns": ('скажи','работает', 'до скольки','до скольки работает',  'проложи','расскажи','покажи','сколько','произнеси', 'сколько', 'включи' , 'как' ,'переведи', 'засеки', 'запусти' ,'сколько', 'будет','открой'),
 
    "cmds": {
       # "wor": ('ворд','редактор','word'),
    #"calc": ('калькулятор','кальк'),
        "ctime": ('текущее время','сейчас времени','который час'),
        "radio": ('включи музыку','воспроизведи радио','включи радио'),
        "anekdot": ('расскажи анекдот','рассмеши меня','ты знаешь анекдоты'),
         'startStopwatch': ('запусти секундомер', "включи секундомер", "засеки время"),
         'func': ('функции',"функцию"),
         'stopStopwatch': ('останови секундомер', "выключи секундомер", "останови"),
          "calc": ('прибавить','умножить','разделить','степень','вычесть','поделить','х','+','-','/'),
             "shutdown": ('выключи', 'выключить', 'отключение', 'отключи', 'выключи компьютер'),
              "video": ('открой разные видео', 'открой видео'),
             "internet": (   "сайт", 'мага','супе', 'торг', 'здан', 'мфц','граф','в интернете'),
              "translator": ("переводчик",'перевод',"пере"),
             "deals": ("дела","делишки", 'как сам', 'как дела'),
             "photo": ('покажи фото', 'фото'),
             "weather": ('погоду', 'покажи погоду'),
             "prob": ('пробки','пробка'),
             "maps": ("открой на карте",'на карте', 'карта ')
            
             
    }  
}
# функции
def speak(what):
    print( what )
    speak_engine.say( what )
    speak_engine.runAndWait()
    speak_engine.stop()

def callback(recognizer, audio):
    try:
        global voice
        voice = recognizer.recognize_google(audio, language = "ru-RU").lower()
        print("[log] Распознано: " + voice)
    
        if voice.startswith(opts["namin"]):
            # обращение к васе
            cmd = voice
            
            for x in opts['namin']:
                cmd = cmd.replace(x, "").strip()
            
            for x in opts['comns']:
                cmd = cmd.replace(x, "").strip()
            
            
           # распознание и выполнение команды
            cmd = recognize_cmd(cmd)
            execute_cmd(cmd['cmd'])
            time.sleep(10.0)
            os.startfile(r'C:\\voi\st.bat')
            
           
        #Ошибки, их нет)
    except sr.UnknownValueError:
        print("[log] Скажи нормально! ")
    except sr.RequestError as e:
        print("[log] Неизвестная ошибка, проверьте интернет!")
 
def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c,v in opts['cmds'].items():
 
        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt
    
    return RC
    
def execute_cmd(cmd):
    if  cmd == 'ctime':
        # сказать текущее время
        now = datetime.datetime.now()
        speak("Сейчас " + str(now.hour) + ":" + str(now.minute))
    
    
    elif cmd == 'radio':
        import webbrowser
        # воспроизвести радио
        webbrowser.open_new_tab('https://newradio.ru/')
    
    elif cmd == 'anekdot':
        # расскаiзать анекдот
        speak("Деревня. Вечер. На краю деревни на лавке сидят дед и внук. Пролетел самолет, выбросил парашутиста. Дед покуривая папироску, задумчиво:– Сапёр летитВнук:– Деда, а почему ты думаешь, что это сапёр? Дед:– Ну кто ж еще будет на минном поле приземляться.")
    elif cmd == 'shutdown':
        os.system('shutdown -s')
        speak("Выключаю...")
    #elif cmd == 'calc':
       # os.startfile(r'C:\\voi\s.bat')
       # speak("открываю  ")
   # elif cmd == 'wor':
       # os.startfile(r'C:\Program Files (x86)\SoftMaker FreeOffice 2018C:\Program Files (x86)\SoftMaker FreeOffice 2018\TextMaker.exe')    
       # speak("открываю")
    elif cmd == 'deals':
        speak("Пока отлично.")

    elif cmd == 'internet':
            sit.sit()
          

    elif cmd == 'translator':
        
        os.startfile(r'C:\\voi\translator.py')

    elif cmd == 'calc':
        calculator.calculator()

    elif cmd == 'weather':
        import webbrowser
        webbrowser.open_new_tab('https://weather.com/ru-RU/weather/today/l/RSXX0063:1:RS?Goto=Redirected')

    elif cmd == 'video':
        import webbrowser
        webbrowser.open_new_tab('https://www.youtube.com/ ')

    elif cmd == 'startStopwatch':
        # Отображаем инструкцию для пользователя
        print('Нажмите клавишу Enter, чтобы начать. После этого нажмите клавишу Enter, чтобы "нажать" на секундомер. Нажмите комбинацию клавиш Ctrl-C для останова секундомера и выхода из программы.')
        input()
        print('Начали.')
        startTime = time.time() # стартовое время первого круга
        lastTime = startTime
        lapNum = 1

        # Начало отслеживание круга
        try:
            while True:
                input()
                lapTime = round(time.time() - lastTime, 2)
                totalTime = round(time.time() - startTime, 2)
                print('Круг #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
                lapNum += 1
                lastTime = time.time() # сброс времени последнего круга
        except KeyboardInterrupt:
            # Обработать исключение Ctrl-C, чтобы не отображалось сообщение об ошибке
            print('\nГотово.')
        
    elif cmd == 'karta':
        import webbrowser
        webbrowser.open_new('https://www.google.com/maps/@55.7301395,38.0321694,10.75z?hl=RU')

    elif cmd == "maps":
        #import map
        import webbrowser
        
        cur = voice[20:]
        cur = str(cur)
        print(cur)
    
       
        url = (f'https://www.google.ru/maps/place/ + {cur}' )
        webbrowser.open_new_tab(url)
    


    elif cmd == "prob":
        import webbrowser

        webbrowser.open('https://yandex.ru/maps/213/moscow/?l=trf%2Ctrfe&ll=37.777663%2C55.770168&z=12')

    elif cmd == 'func':
         os.startfile(r'C:\voi\funcit.txt')
         
         
      

                     
    

# запуск
r = sr.Recognizer()
m = sr.Microphone(device_index = 1)
 
with m as source:
    r.adjust_for_ambient_noise(source)
 
speak_engine = pyttsx3.init()

# Только если у вас установлены голоса для синтеза речи!
voices = speak_engine.getProperty('voices')
speak_engine.setProperty('voice', voices[0].id)

print("если хочешь посмотреть все функции ассистента,тогда скажи вася открой функции")
speak("Хай, я твой личный ассистент")
speak("чаго  хотел?")

stop_listening = r.listen_in_background(m, callback)

while True:
    time.sleep(0.1)

