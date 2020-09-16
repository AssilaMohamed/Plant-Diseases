
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers.normalization import BatchNormalization
from keras import layers
from keras import optimizers
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import ModelCheckpoint
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
from keras.preprocessing import image
import numpy as np

def input_leaf(img):

    filename = 'model1.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    result = loaded_model.predict(img)
    return(result)





def process(Filename):
    # Collecte des informations d'une seule image
    #image_path = "D:/pfe new data/test/test/PotatoHealthy1.JPG"

    new_img = image.load_img(Filename, target_size=(224, 224))
    img = image.img_to_array(new_img)
    img = np.expand_dims(img, axis=0)
    img = img / 255

    return img

