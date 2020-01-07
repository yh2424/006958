import tensorflow as tf

# x, y의 데이터 값
data = [[2, 81], [4, 93], [6, 91], [8, 97]]
x_data = [x_row[0] for x_row in data]
y_data = [y_row[1] for y_row in data]

# 기울기 a와 y 절편 b의 값을 임의로 정한다.
# 단, 기울기의 범위는 0 ~ 10 사이이며 y 절편은 0 ~ 100 사이에서 변하게 한다.
a = tf.Variable(tf.random.uniform([1], 0, 10, dtype = tf.float64, seed = 0))
b = tf.Variable(tf.random.uniform([1], 0, 100, dtype = tf.float64, seed = 0))

# Loss function
def loss():
    # y에 대한 일차 방정식 ax+b의 식을 세운다.
    y = a * x_data + b

    # 텐서플로 RMSE 함수
    rmse = tf.sqrt(tf.reduce_mean(tf.square(y - y_data)))
    return rmse

# 학습률 값
learning_rate = 0.1

# RMSE 값을 최소로 하는 값 찾기
opt = tf.keras.optimizers.SGD(learning_rate)
for step in range(2001):
    opt.minimize(loss, var_list=[a, b])
    loss_result = loss()
    if step % 200 == 0:
        print("Epoch: %.f, RMSE = %.04f, 기울기 a = %.4f, y 절편 b = %.4f"
              % (step, loss_result.numpy(), a.numpy(), b.numpy()))


#Graph
import matplotlib.pyplot as plt
import numpy as np
plt.plot(x_data, y_data, 'o')
x_train = (np.arange(min(x_data)-1.0, max(x_data)+1.0, 0.1))
plt.plot(x_train, a.numpy()*x_train+b.numpy())
plt.plot()