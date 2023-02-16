from sense_hat import SenseHat
from sklearn.metrics import accuracy_score
import tensorflow as tf
sense = SenseHat()

# load the model from saved_model
model = tf.keras.models.load_model('saved_model/my_model')
# predict the outputs using the model
predictions = model.predict(x_test)
  # x_test : the data collected  from the accelerometer
  # predicted : the labels and the confidence level of the prediction
# print the accuracy
print("Accuracy: ", accuracy_score(y_test, predictions))
# print the confidence level and label of each prediction

correct = 0
for i in range(len(predictions)):
    print("Confidence level: ", predictions[i], "Label: ", y_test[i])
    if predictions[i] > .75: correct+=1
print("Confidence Level Accurate Percentage:", correct/len(predictions) * 100)
