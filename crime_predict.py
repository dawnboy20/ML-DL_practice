# 20200512_fregic crimepredictor
# 기본적인 선형회귀
# tensorflow 없음!

import numpy as np
import matplotlib.pyplot as plt

x = np.array([10,15,16,1,4,6,18,12,14,7])   # 경찰 수 데이터
y = np.array([5,2,1,9,7,8,1,5,3,6])         # 범죄수 데이터

w= np.random.uniform(-10,10)    # 선형회귀의 기울기 (-10 ~ 10)
b=np.random.uniform(-10,10)     # 선형회귀의 y절편 (-10 ~ 10)
learning_rate =0.001

for i in range(100000):
    y_predict=w*x+b
    error = np.square(y_predict-y).mean()   # 손실값 : 평균제곱오차 square (제곱) mean (평균)
    w=w-learning_rate*((y_predict-y)*x).mean()
    b=b-learning_rate*(y_predict-y).mean()
    if i % 10000==0:
        print("error : {0:.6f}, w={0:.6f},b={0:.6f}".format(error,w,b)) # 에러값 , 기울기, y절편 출력

cop_num = int(input("경찰 수는 ? : ")) # 경찰 수 입력

plt.scatter (x,y,color='r') # scatter => 점 찍기
plt.plot(x,w*x+b,color='b') # plot => 직선 , 선형회귀의 선
plt.scatter(cop_num,w*cop_num+b, color='g') # 예측하고 싶은 값
plt.show()

result=w*cop_num+b
print("경찰 수가 {0}일때 : ".format(cop_num), result, "건의 범죄 예상")