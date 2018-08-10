from __future__ import print_function
import keras
from keras.datasets import cifar10
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.optimizers import adagrad, adadelta, rmsprop, adam
from keras.utils import np_utils
from keras.regularizers import l2, activity_l2
from sklearn.cross_validation import StratifiedKFold
import numpy as np
import pandas as pd
import random
import math
import cv2
from keras.applications.inception_v3 import InceptionV3
from keras.preprocessing import image
from keras.models import Model, load_model
from keras.layers import Dense, GlobalAveragePooling2D
from keras import backend as K



if __name__ == '__main__':
    colormode = 'rgb'
    channels = 3
    batchsize = 25
    trainingsamples = 20000
    model_name = '27_class_inception_color_10'

    model = load_model('D:\\models\\27_class_inception_color_9.h5')
    model.compile(optimizer='adagrad', loss='categorical_crossentropy',  metrics=['accuracy'])


    train_datagen = ImageDataGenerator(horizontal_flip=True, vertical_flip=True)
    test_datagen = ImageDataGenerator()

    train_generator = train_datagen.flow_from_directory(
            "G:\\data\\train",
            target_size=(150, 150),
            batch_size=batchsize,
            color_mode=colormode)

    validation_generator = test_datagen.flow_from_directory(
            "G:\\data\\val",
            target_size=(150, 150),
            batch_size=batchsize,
            color_mode=colormode)

    history = model.fit_generator(
            train_generator,
            samples_per_epoch=trainingsamples,
            nb_epoch=200,
            validation_data=validation_generator,
            nb_val_samples=10000,
            class_weight='auto')

    hist = history.history
    hist = pd.DataFrame(hist)

    hist.to_csv('D:\\results\\'+model_name+'.csv')
    model.save('D:\\models\\'+model_name+'.h5')