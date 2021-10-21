import tensorflow as tf
(x_train,y_train),(x_test,y_test) = tf.keras.datasets.mnist.load_data()
print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)

import matplotlib.pyplot as plt
fig,axs=plt.subplots(4,4,figsize = (10,10))
plt.gray()
for i ,ax in enumerate(axs.flat):
    ax.matshow(x_train[i])
    ax.axis('off')
    ax.set_title('Number{}'.format(y_train[i]))
fig.show()

#Preprocess
x_train = x_train.reshape(x_train.shape[0],28,28,1)

x_test = x_test.reshape(x_test.shape[0],28,28,1)
input_shape = (28,28,1) #here 1 is for grey scale images

x_train = x_train.astype('float32')

x_test = x_test.astype('float32')
x_test /= 255
x_train /= 255
print('x-train shape : ', x_train.shape)
print('no of images in x_train : ', x_train.shape[0])
print('no of images in x_test : ', x_test.shape[0])


#Building the Convolutional Neural network
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Dropout, Flatten, MaxPooling2D
modle = Sequential()
modle.add(Conv2D(28, kernel_size=(2, 2), input_shape=input_shape))
modle.add(MaxPooling2D(pool_size=(2, 2)))
modle.add(Flatten())
modle.add(Dense(128, activation=tf.nn.relu))
modle.add(Dropout(0.2))
modle.add(Dense(128, activation=tf.nn.softmax))

#compiling and Training
modle.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
modle.fit(x=x_train,y = y_train,epochs=2)

#Evaluationn
modle.evaluate(x_test,y_test)