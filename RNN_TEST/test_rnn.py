
import tensorflow as ts
import numpy as np
import matplotlib.pyplot as plt

from tensorflow import keras
from keras.layers import Dense, Input
from keras.models import Sequential
from keras.models import Model
from keras.utils.np_utils import to_categorical
from IPython.display import Image

from keras.layers import SimpleRNN

MNIST = keras.datasets.mnist
(train_img, train_labels), (test_img, test_levels) = MNIST.load_data()

train_img = train_img / 255
test_img = test_img / 255

#plt.imshow(train_img[:5].transpose((1,0,2)).reshape(28,-1), cmap = "gray")
#plt.show()

train_noisy_image = train_img  + np.random.normal(0.5, 0.1, train_img.shape)
train_noisy_image[train_noisy_image>1.0] = 1.0
test_noisy_image = test_img + np.random.normal(0.5, 0.1, test_img.shape)
test_noisy_image[test_noisy_image>1.0] = 1.0

# 정규화, Normalization
train_labels = to_categorical(train_labels, 10)
test_levels = to_categorical(test_levels, 10)

# 상단에 아래내용 추가 필요
# from keras.layers import SimpleRNN

inputs = Input(shape=(28,28)) # 입력 데이터
X1 = SimpleRNN(64, activation="tanh")(inputs) # 은닉층 생성
X2 = Dense(10, activation="softmax")(X1) # 출력층 생성
model = Model(inputs, X2) # 모델 생성
model.summary() # 모델 정보 요약


model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
# train model 학습
hist = model.fit(train_noisy_image, train_labels, validation_data=(test_noisy_image, test_levels), epochs=3, verbose=2)

# trained model 에서 결과 예측하기
# model.predict()

model.summary()
