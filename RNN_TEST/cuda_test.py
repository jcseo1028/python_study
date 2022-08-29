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
print(device)
print(torch.cuda.is_available())