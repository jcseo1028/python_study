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

# 여기 블로그 글 참고
# https://blog.naver.com/eeeeeeeeemh/222439130459
# https://3months.tistory.com/465?category=756964
# https://github.com/ndb796/CNN-based-Celebrity-Classification-AI-Service-Using-Transfer-Learning/blob/main/Celebrity%20Classifier%20Service%20Using%20Crawling%20and%20Transfer%20Learning.ipynb

# 이 양반은 뭔가 혼자 열심히 하는 듯? - 시간날 때 카페 게시글들 함 보자.
# https://cafe.naver.com/opencv?iframe_url_utf8=%2FArticleRead.nhn%253Fquery%3Dpython%2520%25EB%25B0%25B0%25EC%2597%25B4%2520%25ED%2581%25AC%25EA%25B8%25B0%2526where%3Dsearch%2526tc%3Dnaver_search%2526clubid%3D11534583%2526articleid%3D57326%2526where%3Dsearch

# 데이터셋을 불러올 때 사용할 변형(transformation) 객체 정의
transforms_train = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.RandomHorizontalFlip(), # 데이터 증진(augmentation)
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]) # 정규화(normalization)
])

transforms_test = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

data_dir = './custom_dataset_3p'
train_datasets = datasets.ImageFolder(os.path.join(data_dir, 'train'), transforms_train)
test_datasets = datasets.ImageFolder(os.path.join(data_dir, 'test'), transforms_test)

train_dataloader = torch.utils.data.DataLoader(train_datasets, batch_size=4, shuffle=True, num_workers=4)
test_dataloader = torch.utils.data.DataLoader(test_datasets, batch_size=4, shuffle=True, num_workers=4)

print('학습 데이터셋 크기:', len(train_datasets))
print('테스트 데이터셋 크기:', len(test_datasets))

class_names = train_datasets.classes
print('클래스:', class_names)

# 학습 데이터를 배치 단위로 불러오기
iterator = iter(train_dataloader)

# Could not load dynamic library 'cudart64_110.dll'; 해당 에러 시 아래 링크에서 CUDA Toolkit 11.0 설치
# https://developer.nvidia.com/cuda-11.0-download-archive?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exenetwork
# 관련 링크
# https://leunco.tistory.com/13
