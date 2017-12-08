from keras.models import Model
from keras.layers import Input
digit_input = Input(shape=(1,28,28))
from keras.models import Sequential
from keras.layers import Dense,Activation,Conv2D,MaxPooling2D,Flatten,Dropout
model = Sequential()
model.add(Conv2D(64,(3,3),activation='relu',input_shape =(100,100,32)))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dense(256,activation='relu'))
model.add(Dropout(0.5))
model.add(Flatten)
model.add(Conv2D(32,(3,3),activation='relu',input_shape=(224,224,3)))
model.compile(loss='binary_crossentropy',optimizer='rmsprop')
from keras.optimizers import SGD
sgd = SGD(lr=0.01,decay=1e-6,momentum=0.9,nesterov=True)
model.compile(loss='categorical_crossentropy',optimizer=sgd)
model.fit(x_train,y_train,batch_size=32,epochs=10,validation_data=(x_val,y_val))