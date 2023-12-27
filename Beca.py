import subprocess
import subprocess as s
import sys
import os
import speech_recognition as sr
import pyttsx3
import wikipedia
import pywhatkit
from gtts import gTTS
import wikipediaapi
import requests
import datetime
import openai
import webbrowser
from playsound import playsound
from googletrans import Translator
import serial
import time

# Função para ouvir e reconhecer a fala
def ouvir_microfone():
 maquina = pyttsx3.init()
 ser = serial.Serial('COM3', 9600)  # Porta correta no IDE Arduino.
 time.sleep(2) # Tempo pra esabelecer comunicação com o Arduino
 
# voz da máquina
 maquina.say("olá, eu sou a Beca")
 maquina.say("o que vamos fazer hoje?")
 maquina.runAndWait()

# habilita o microfone do usuário
 recognizer = sr.Recognizer()
 microphone = sr.Microphone()

# usando o microfone
 with sr.Microphone() as source:
        # chama um algoritmo de redução de ruídos no som
        recognizer.adjust_for_ambient_noise(source)

        # Frase para o usuário dizer algo
        print("Ouvindo:")
        maquina.say('Pode falar, estou te ouvindo')
        maquina.runAndWait()

        # Função para converter texto em fala
        while True:
            # Armazena o que foi dito em uma variável
            audio = recognizer.listen(source)

            # passa a variável para o algoritmo reconhecedor de padrões
            try:
                frase = recognizer.recognize_google(audio, language='pt-BR')
                # Retorna a frase pronunciada
                print("Você disse: " + frase)
  
                if "procure" in frase:
                    wikipedia.set_lang('pt')
                    procurar = frase.replace('procure', ' ')
                    result = wikipedia.summary(procurar, sentences=2)
                    print(result)
                    maquina.say(result)
                    maquina.runAndWait()
 
                if "luz" in frase:
                    ser.write(b'H')  # 'H' é usado para acender o LED no sketch do Arduino.
               
                if "desligar" in frase:    
                    ser.write(b'L')  # 'L' é usado para apagar o LED no sketch do Arduino.
 
                if 'toque' in frase:
                    musica = frase.replace('toque', '')
                    result = pywhatkit.playonyt(musica)
                    maquina.say('Tocando música')
                    maquina.runAndWait()
 
                if 'horas' in frase:
                    agora = datetime.datetime.now()
                    hora = agora.strftime('%H')
                    minutos = agora.strftime('%M')
                    maquina.say('São ' + hora + ' horas e ' + minutos + ' minutos.')
                    maquina.runAndWait()
 
                if "navegador" in frase:
                    os.system("start chrome.exe")
 
                if "Excel" in frase:
                    os.system("start Excel.exe")
               
                if "Word" in frase:
                    os.system("start winword.exe")
               
                if "PowerPoint" in frase:
                    os.system("start POWERPNT.exe")
                
                if "Outlook" in frase:
                    os.system("start Outlook.exe")
               
                if "Notepad" in frase:
                    os.system("start notepad.exe")
               
                if "Xbox" in frase:
                    os.system("start XboxPcApp.exe")
 
                if "iFood" in frase:
                    webbrowser.open_new("https://www.ifood.com.br/")
 
                if "tempo" in frase:
                    API_KEY = "f41155dbb385912e720c16259cacb81a"
                    cidade = "São Paulo"
                    link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"
                    requisicao = requests.get(link)
                    requisicao_dic = requisicao.json()
                    descricao = requisicao_dic['weather'][0]['description']
                    temperatura = requisicao_dic['main']['temp'] - 273.15
                    temperatura_tratada = round(temperatura, 2)
                    Resultado_tempo = ('A previsão do tempo é: Hoje temos ' + descricao, ' E está fazendo ' + f"{temperatura_tratada} graus")
                    print(Resultado_tempo)
                    maquina.say(Resultado_tempo)
                    maquina.runAndWait()
 
                if "elogio" in frase:
                    maquina.say('Você está deslumbrante hoje')
                    maquina.runAndWait()
 
                if "conselho" in frase:
                    maquina.say('Nem todas as tempestades vêm para atrapalhar a sua vida. Algumas vêm para limpar seu caminho.')
                    maquina.runAndWait()
  
                if "piada" in frase:
                    maquina.say('Por que o menino estava falando ao telefone deitado?')
                    maquina.say('Para não cair a ligação. HAHAHA')
                    maquina.runAndWait()
 
                if "batida" in frase:
                    playsound("C://Users\caio_\AppData\Local\Microsoft\VisualStudio\Batida.mp3")
                    maquina.runAndWait()
 
 
                if "signo" in frase:
                    api_key = "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"
 
                    openai.api_key = api_key
                   
                    maquina.say("Bem-vindo ao Horóscopo Diário!")
                    maquina.runAndWait()
 
                    recognizer1 = sr.Recognizer()
                    microphone1 = sr.Microphone()
                  
                    print("Diga o seu signo :")
                    maquina.say("Diga o seu signo")
                    maquina.runAndWait()

                    with microphone1 as source1:
                            audio1 = recognizer1.listen(source1)
 
                            signo = recognizer1.recognize_google(audio1, language='pt-BR').lower()
                            print(f"Signo reconhecido: {signo}")
 
                            prompt = f"Me dê a sorte de hoje para o signo {signo}."
 
                            response = openai.Completion.create(
                            engine="text-davinci-002",
                            prompt=prompt,
                            max_tokens=150
                            )
 
                            horoscopo = response.choices[0].text.strip()
 
                            print(f"Horóscopo para {signo.capitalize()} hoje:")
                            print(horoscopo)
                            maquina.say(horoscopo)
                            maquina.runAndWait()
                         
                if "saber" in frase:
                    api_key = "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"
 
                    openai.api_key = api_key
                   
                    maquina.say("Bem vindo ao mundo do conhecimento")
                    maquina.runAndWait()
 
                    recognizer2 = sr.Recognizer()
                    microphone2 = sr.Microphone()
 
                    while True:
                        print("faça a sua pergunta")
                        maquina.say("faça a sua pergunta")
                        maquina.runAndWait()
 
                        with microphone2 as source2:
                            audio2 = recognizer2.listen(source2)
 
                            pergunta = recognizer2.recognize_google(audio2, language='pt-BR').lower()
                            print(pergunta)
                           
                            if pergunta == 'sair':
                                break
 
                            prompt1 = (pergunta)
 
                            response = openai.Completion.create(
                            engine="text-davinci-003",
                            prompt=prompt1,
                            max_tokens=150
                            )
 
                            respostpergunta = response.choices[0].text.strip()
 
                            print(f"resposta {pergunta.capitalize()}:")
                            print(respostpergunta)
                            maquina.say(respostpergunta)
                            maquina.runAndWait()            
               
                if any(agradecimento in frase for agradecimento in ["obrigado", "obrigada", "valeu", "agradecido"]):
                    maquina.say("De nada! Estou aqui para ajudar.")
                    maquina.runAndWait()
                    break
 
            except sr.UnknownValueError:
                print("Não estou entendendo")
                maquina.say('Não estou entendendo. Você pode repetir, por favor?')
                maquina.runAndWait()

            # Se não reconheceu o padrão de fala, exibe a mensagem
ouvir_microfone()