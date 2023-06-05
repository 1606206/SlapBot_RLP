import random
import glob
import time as time
import numpy as np
import roboflow as Roboflow
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import serial
import pyCardDeck
from playsound import playsound


#connectar la raspberry pi i l'arduino
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
ser.reset_input_buffer()

#carregar API roboflow
rf = Roboflow.Roboflow(api_key="7amu8FnEjKxcYScY98i3")
project = rf.workspace("h-pv33i").project("carddetpokerdeck")
model = project.version(1, local="http://localhost:9001/").model

#obrir la càmera
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
time.sleep(2)
   
N_JUGADORS = 3
POSSIBLES_NUMS = ["1", "2", "3","4","5","6","7","8","9","10","J","Q","K"]
POSSIBLES_PALS = ["picas","cors","trebols","diamants"]
cartesEspecials =	{
    'J': 1,
    'Q': 2,
    'K': 3,
    'A': 4
}

def pasarTorn(torn):
    torn =torn + 1
    if(torn == N_JUGADORS):
        torn = 0
    return torn
    
def trobarCombinacio(pila_de_cartes):
    trobat = False
    
    if len(pila_de_cartes[0].split()[0]) == 3:
        num0='10'
    else:
        num0 = pila_de_cartes[0].split()[0][0]
        
    if len(pila_de_cartes[1].split()[0]) == 3:
        num1='10'
    else:
        num1 = pila_de_cartes[1].split()[0][0]
        
    if len(pila_de_cartes[2].split()[0]) == 3:
        num2='10'
    else:
        num2 = pila_de_cartes[2].split()[0][0]
        
        
        
    if(num0==num1):
        trobat = True
        print("DOS IGUAAALS")
        
    if(num0==num2):
        trobat = True
        print("SANDWIIICH")
    return trobat


# When everything done, release the capture

prev_frame=None
ret, frame = cap.read()
while(True):
    data=0
    pila_de_cartes=["re de res1", "re de res2", "re de res3"]
    torn = 0
    carta_especial = False
    num_a_tirar = 1
    nova_carta = "re de res1"
    ronda_activa = True
    data=0
    ser.reset_input_buffer()
    while ronda_activa:
        print("Es el torn del jugador", torn+1)
        if(torn==0):
            time.sleep(2)
            ser.write(b"T\n")
            print("tira la carta el robot")
            if ser.inWaiting()>0:
                ronda_activa = False
                break
        if ronda_activa!=False:
            venim=False
            while(nova_carta==pila_de_cartes[0] and ronda_activa!=False):
                ret, frame = cap.read()
                t0=time.time()
                cv2.imshow('frame', frame[0:430, 100:450])
                if cv2.waitKey(1) == ord('q'):
                    break
                if prev_frame is not None:
                    diff = np.abs(frame.astype(np.float32)- prev_frame.astype(np.float32))/255   
                    if ((diff>0.25).any()):
                        venim=True
                    else:
                        if(venim):
                            t0=time.time()
                            retorn=model.predict(frame[0:430, 100:450], confidence=30, overlap=30).json()
                            t1=time.time()
                            if(len(retorn['predictions'])>0):
                                nova_carta = retorn["predictions"][0]['class']
                        venim=False      
                prev_frame=frame
                if ser.inWaiting()>0:
                    ronda_activa = False
                    break                  
        if ronda_activa!=False:
            all_words = nova_carta.split()
            num_carta = all_words[0]
            print(nova_carta)
            print("#################################################")
            num_a_tirar = num_a_tirar - 1

            pila_de_cartes.insert(0, nova_carta)
            pila_de_cartes.pop(3)
            combinacio = trobarCombinacio(pila_de_cartes)
            if(combinacio): 
                ser.write(b"A\n")
                print("ATACAAAAAAAAA")
                playsound('audios/audio1.mp3')
                ronda_activa = False
            else:
                if(num_carta[0] in cartesEspecials):
                    print("es unacarta especial")
                    torn = pasarTorn(torn)
                    carta_especial = True
                    num_a_tirar = cartesEspecials[num_carta[0]]
                else:
                    if(num_a_tirar==0):
                        if(carta_especial==True):
                            
                            carta_especial = False
                            ronda_activa = False
                            printatorn = torn
                            if(printatorn==0):
                                printatorn=1
                            print("Se les emporta el jugador ", printatorn)
                        else:
                            torn = pasarTorn(torn)
                            carta_especial = False
                    else:
                        if(carta_especial == False):
                            torn = pasarTorn(torn)
    while ser.inWaiting()==0:
        pass
    data=ser.readline().decode('utf-8').rstrip()
    if(data==1):
        print("Ha guanyat el robot")
    elif(data==2):
        print("Han guanyat els humans")  
    print("S'HA ACABAT LA RONDA")
    time.sleep(20) #temps per recarregar les cartes el robot en cas que hagi guanyat
    
cap.release()
cv2.destroyAllWindows()