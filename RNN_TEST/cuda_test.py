import os

import tensorflow as ts
import numpy as np
import matplotlib.pyplot as plt

from tensorflow import keras

import torch
import torch.nn as nn
import torch.optim as optim

import torchvision
from torchvision import datasets, models, transforms

import numpy as np
import time

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu") # device 객체

# CUDA Toolkit 10.2 로 해야 하나? -> Pytorch 에서 지원하지 않음. 
# 11.7 설치해도 안되네...
#  

# 11.3 으로 다시 해보자
# https://pytorch.org/get-started/locally/
### pytorch : 1.12.1, cuda : 11.3 환경은 맞다고 하는데 실행은 되지 않음. (nvcc --version)
### pytorch : 1.12.1, cuda : 11.6 으로 다시 해보자..
### cuda 11.6.2 재설치 
### cudnn 8.5.0 -> 역시나 되지 않음. ???

# https://normal-engineer.tistory.com/163
# # Graphic Driver 재설치

print(device)
print(torch.cuda.is_available())