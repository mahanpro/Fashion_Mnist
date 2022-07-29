import tensorflow as tf
import pandas as pd
import os


# Read CSV
train = pd.read_csv("fashion-mnist_train.csv")
test = pd.read_csv("fashion-mnist_test.csv")

# Train
train_label = train.pop('label').to_numpy()
test_label = test.pop('label').to_numpy()

train_data = train.to_numpy()
test_data = test.to_numpy()
train_data = train_data/255.
test_data = test_data/255.
print(train_data.dtype, train_data.shape)
print(test_data.dtype, test_data.shape)

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.InputLayer(input_shape=[28*28]))
model.add(tf.keras.layers.Dense(150, activation=tf.keras.activations.relu))
model.add(tf.keras.layers.Dense(50, activation=tf.keras.activations.relu))
model.add(tf.keras.layers.Dense(10, activation=tf.keras.activations.softmax))

model.compile(loss=tf.keras.losses.sparse_categorical_crossentropy, optimizer=tf.keras.optimizers.SGD())
model.fit(x=train_data, y=train_label, validation_split=0.1, epochs=30)

# Test
results = model.evaluate(test_data, test_label)
print("test loss: ", results)

# Save Model
model.save('fashion_mnist' + '.h5')
