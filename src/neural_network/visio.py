import numpy as np
import cv2
import tensorflow as tf

gpus = tf.config.list_physical_devices('GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)
np.warnings.filterwarnings('ignore', category=np.VisibleDeprecationWarning)

diccionari={
            0:'6D',
            1:'6C',
            2:'6S',
            3:'6H',
            4:'7D',
            5:'7C',
            6:'7S',
            7:'7H',
            8:'AD',
            9:'AC',
            10:'AS',
            11:'AH',
            12:'8D',
            13:'8C',
            14:'8S',
            15:'8H',
            16:'10C',
            17:'10S', 
            18:'10H',
            19:'10D',
            20:'2D',
            21:'2C',
            22:'2S',
            23:'2H',
            24:'9D',
            25:'9C',
            26:'9S',
            27:'9H',
            28:'3D',
            29:'3C',
            30:'3S',
            31:'3H',
            32:'5D',
            33:'5C',
            34:'5S',
            35:'5H',          
            36:'4D',
            37:'4C',
            38:'4S',
            39:'4H',
            40:'QD',
            41:'QS',
            42:'QH',
            43:'QC',
            44:'JD',
            45:'JS',
            46:'JH',
            47:'JC',
            48:'KD',
            49:'KS',
            50:'KH',
            51:'KC',
            }

def funcVisio(img, model):
    abc=[]
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (180, 180))
    imgs = img.reshape((1, img.shape[0], img.shape[1], 1))
    data_generator = tf.keras.preprocessing.image.ImageDataGenerator(rotation_range=90, brightness_range=(0.5, 1.5), shear_range=15.0, zoom_range=[.3, .8])
    data_generator.fit(imgs)
    image_iterator = data_generator.flow(imgs)

    img_transformed=image_iterator.next()[0].astype('int')/255
    abc.append([img_transformed, 0])
    np.save('carta.npy',abc)
    carta = np.load('carta.npy', allow_pickle=True)


    cartaX=[]
    for x in carta:
        cartaX.append(x[0]) 
    cartaX=np.array(cartaX)

    
    predictions=model.predict(cartaX)

    return diccionari[np.argmax(predictions, axis=1)[0]]