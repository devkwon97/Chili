import numpy
import tensorflow
from pandas.io.parsers import read_csv
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

model = tensorflow.global_variables_initializer();

data = read_csv('amount.csv', sep=',')

xy = numpy.array(data, dtype=numpy.float32)

x_data = xy[:, 1:-1]
y_data = xy[:, [-1]]

X = tensorflow.placeholder(tensorflow.float32, shape=[None, 4])
Y = tensorflow.placeholder(tensorflow.float32, shape=[None, 1])

W = tensorflow.Variable(tensorflow.random_normal([4, 1]), name="weight")
b = tensorflow.Variable(tensorflow.random_normal([1]), name="bias")

# 가설설정
hypothesis = tensorflow.matmul(X, W) + b

# 비용 함수 정의
cost = tensorflow.reduce_mean(tensorflow.square(hypothesis - Y))

# 옵티마이저로 내려가는 경사값 알고리즘구현
optimizer = tensorflow.train.GradientDescentOptimizer(learning_rate=0.000005)
train = optimizer.minimize(cost)

sess = tensorflow.Session()

sess.run(tensorflow.global_variables_initializer())

# 학습실행
for step in range(100001):
    cost1, hypo_, _ = sess.run([cost, hypothesis, train], feed_dict={X: x_data, Y: y_data})
    if step % 500 == 0:
        print("#", step, " 손실 비용: ", cost1)
        print("- 고추 가격: ", hypo_[0][0], "원")

saver = tensorflow.train.Saver()
save_path = saver.save(sess, "./saved.cpkt")
print('학습 완료.')