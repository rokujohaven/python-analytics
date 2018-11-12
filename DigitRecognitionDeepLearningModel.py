#using a small training subset of MNIST data of only 2500 images. 

from keras.models import Sequential
from keras.layers import Dense

#Create the model: model
model = Sequential()

# Add the first Dense hidden layer of 50 units to the model with 'relu' activation. For this data, the input_shape is (784,).
model.add(Dense(50, activation='relu', input_shape=(784,)))

# Add the second Dense hidden layer of 50 units with relu activation
model.add(Dense(50, activation='relu'))

# Add the output layer. The # of nodes is 10, since there are 10 digits (categories). The activation is softmax 
model.add(Dense(10, activation='softmax'))

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics = ['accuracy'])

# Fit the model using 30% of data as test set 
model.fit(X,y, validation_split=.3)

