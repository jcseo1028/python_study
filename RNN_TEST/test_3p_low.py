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

def imshow(input, title):
    # torch.Tensor를 numpy 객체로 변환
    input = input.numpy().transpose((1, 2, 0))
    # 이미지 정규화 해제하기
    mean = np.array([0.485, 0.456, 0.406])
    std = np.array([0.229, 0.224, 0.225])
    input = std * input + mean
    input = np.clip(input, 0, 1)
    # 이미지 출력
    plt.imshow(input)
    plt.title(title)
    plt.show()

# 아래 블로그 링크들 참고
# https://blog.naver.com/eeeeeeeeemh/222439130459
# https://3months.tistory.com/465?category=756964

# 이 코드 베이스
# https://github.com/ndb796/CNN-based-Celebrity-Classification-AI-Service-Using-Transfer-Learning/blob/main/Celebrity%20Classifier%20Service%20Using%20Crawling%20and%20Transfer%20Learning.ipynb
# https://ainote.tistory.com/14

# 이 양반은 뭔가 혼자 열심히 하는 듯? - 시간날 때 카페 게시글들 함 보자.
# https://cafe.naver.com/opencv?iframe_url_utf8=%2FArticleRead.nhn%253Fquery%3Dpython%2520%25EB%25B0%25B0%25EC%2597%25B4%2520%25ED%2581%25AC%25EA%25B8%25B0%2526where%3Dsearch%2526tc%3Dnaver_search%2526clubid%3D11534583%2526articleid%3D57326%2526where%3Dsearch

# cuda 를 쓰려면... 아래 링크 참고
# https://blog.naver.com/youyeon9500/222845508179
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu") # device 객체

# 데이터셋을 불러올 때 사용할 변형(transformation) 객체 정의
transforms_train = transforms.Compose([
    transforms.Resize((224, 224)), # 추후 원본 사이즈로 테스트 필요함.
    transforms.RandomHorizontalFlip(), # 데이터 증진(augmentation)
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]) # 정규화(normalization)
])

transforms_test = transforms.Compose([
    transforms.Resize((224, 224)), # 추후 원본 사이즈로 테스트 필요함.
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

data_dir = './custom_dataset_3p'
train_datasets = datasets.ImageFolder(os.path.join(data_dir, 'train'), transforms_train)
test_datasets = datasets.ImageFolder(os.path.join(data_dir, 'test'), transforms_test)

# num_workers 변화 : 4->2->1->0  0 이외에는 에러 발생 -> GPU 활성화가 되지 않아서 그런듯.
train_dataloader = torch.utils.data.DataLoader(train_datasets, batch_size=2, shuffle=True, num_workers=0) 
test_dataloader = torch.utils.data.DataLoader(test_datasets, batch_size=2, shuffle=True, num_workers=0)

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

inputs, classes = next(iterator)
out = torchvision.utils.make_grid(inputs)
imshow(out, title=[class_names[x] for x in classes])

model = models.resnet34(pretrained=True)
num_features = model.fc.in_features
# 전이 학습(transfer learning): 모델의 출력 뉴런 수를 2개로 교체하여 마지막 레이어 다시 학습
model.fc = nn.Linear(num_features, 2)
model = model.to(device)

criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)

num_epochs = 50
model.train()
start_time = time.time()

# 전체 반복(epoch) 수 만큼 반복하며
for epoch in range(num_epochs):
    running_loss = 0.
    running_corrects = 0

    # 배치 단위로 학습 데이터 불러오기
    for inputs, labels in train_dataloader:
        inputs = inputs.to(device)
        labels = labels.to(device)

        # 모델에 입력(forward)하고 결과 계산
        optimizer.zero_grad()
        outputs = model(inputs)
        _, preds = torch.max(outputs, 1)
        loss = criterion(outputs, labels)

        # 역전파를 통해 기울기(gradient) 계산 및 학습 진행
        loss.backward()
        optimizer.step()

        running_loss += loss.item() * inputs.size(0)
        running_corrects += torch.sum(preds == labels.data)

    epoch_loss = running_loss / len(train_datasets)
    epoch_acc = running_corrects / len(train_datasets) * 100.

    # 학습 과정 중에 결과 출력
    print('#{} Loss: {:.4f} Acc: {:.4f}% Time: {:.4f}s'.format(epoch, epoch_loss, epoch_acc, time.time() - start_time))

model.eval()
start_time = time.time()

with torch.no_grad():
    running_loss = 0.
    running_corrects = 0

    for inputs, labels in test_dataloader:
        inputs = inputs.to(device)
        labels = labels.to(device)

        outputs = model(inputs)
        _, preds = torch.max(outputs, 1)
        loss = criterion(outputs, labels)

        running_loss += loss.item() * inputs.size(0)
        running_corrects += torch.sum(preds == labels.data)

        # 한 배치의 첫 번째 이미지에 대하여 결과 시각화
        print(f'[예측 결과: {class_names[preds[0]]}] (실제 정답: {class_names[labels.data[0]]})')
        imshow(inputs.cpu().data[0], title='예측 결과: ' + class_names[preds[0]])

    epoch_loss = running_loss / len(test_datasets)
    epoch_acc = running_corrects / len(test_datasets) * 100.
    print('[Test Phase] Loss: {:.4f} Acc: {:.4f}% Time: {:.4f}s'.format(epoch_loss, epoch_acc, time.time() - start_time))


torch.save(model.state_dict(), './RNN_TEST/test_3p_low_model.pt')
print('state_dict format of the model: {}'.format(model.state_dict()))

