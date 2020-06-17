import numpy
import tensorflow

# 텐서 홀더 설정
X = tensorflow.placeholder(tensorflow.float32, shape=[None, 4])
Y = tensorflow.placeholder(tensorflow.float32, shape=[None, 1])

W = tensorflow.Variable(tensorflow.random_normal([4, 1]), name="weight")
b = tensorflow.Variable(tensorflow.random_normal([1]), name="bias")

# 가설을 정의
hypothesis = tensorflow.matmul(X, W) + b

# 학습한 모델 불러오기
saver = tensorflow.train.Saver()
model = tensorflow.global_variables_initializer()

# 4가지 변인 입력
avg_temp = float(input('평균 온도: '))
min_temp = float(input('최저 온도: '))
max_temp = float(input('최고 온도: '))
rain_fall = float(input('강수량: '))

with tensorflow.Session() as sess:
    sess.run(model)
    save_path = "./saved.cpkt"
    saver.restore(sess, save_path)

    data = ((avg_temp, min_temp, max_temp, rain_fall), (0, 0, 0, 0))
    arr = numpy.array(data, dtype=numpy.float32)

    x_data = arr[0:4]
    dict = sess.run(hypothesis, feed_dict={X: x_data})
    print('고추의 예측 가격은',dict[0][0],'원')