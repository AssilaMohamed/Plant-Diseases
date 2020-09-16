from flask import *

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
from keras.preprocessing import image

import functions
import os
from os.path import join as pjoin
from uuid import uuid4

from flask import Flask, request, render_template, send_from_directory


app = Flask(__name__)
# app = Flask(__name__, static_folder="images")



APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    # target = os.path.join(APP_ROOT, 'static/')
    print(target)
    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        destination = "/".join([target, filename])
        print ("Accept incoming file:", filename)
        print ("Save it to:", destination)
        upload.save(destination)
    global List
    target2 = os.path.join(APP_ROOT, 'images/',filename)
    List = functions.process(target2)
    Output = functions.input_leaf(List)
    if (Output == 0):
        result = 'apple scabe'
    elif (Output == 'a'):
        result = 'Angel man Syndrome founded'
    elif (Output == 'aa'):
        result = 'Williams Syndrome founded'
    else:
        result = 'No Syndrome founded'
    if (Output == 'aaa'):
        description = '======='
        frec = '========='
    elif (Output == 'aaaa'):
        description = '=============='
        frec = '=================='
    elif (Output == 'aaaaa'):
        description = '===========.'
        frec = '===================='
    else:
        description = '====== '
        frec = '==========='
    # return send_from_directory("images", filename, as_attachment=True)
    return render_template("final.html", name=result, desc = description, desc2 = frec, image_name=filename)

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)

if __name__ == "__main__":
    app.run(port=4555, debug=True)
