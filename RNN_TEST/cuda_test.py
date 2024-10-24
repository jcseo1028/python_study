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
print(torch.__version__)
print(torch.cuda.get_arch_list())
print(torch.version.cuda)

# Pytorch 환경 출력 방법
#  > python -m torch.utils.collect_env
# 설치할 거는 다 한거 같은데... CUDA Available 이 되지 않는구먼...


# Code Project 에서 11.7 로 다시 함 해보자.
# https://www.codeproject.com/Articles/5322557/CodeProject-AI-Server-AI-the-easy-way
# 1. install the CUDA 11.7 Drivers
# 2. install CUDA Toolkit 11.7
# 3. Download and run our cuDNN install script to install cuDNN.
