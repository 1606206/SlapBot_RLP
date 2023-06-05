import visio
import cv2
from keras.models import load_model

#"imatge.jpg" és el path de la imatge que es vol passar
# en el cas del programa es salta la següent linia i es passa el frame a la funció
img = cv2.imread("imatge.jpg")

retorn=visio.funcVisio(img, load_model("modelV.h5"))
#retorn és el valor de la carta