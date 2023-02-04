# Water Level Classification Using DeepLearning

This file contains code for a deep learning model that classifies images into three categories: "A", "B", and "C". The model uses the Sobel filter and a sum of intensity values to extract features from the input images and trains a multi-input model to classify the images based on these features.

## Requirements

+ NumPy

+ OpenCV

+ Matplotlib

+ Keras

+ TensorFlow

## Key files and functions

+ Sobel: A function that applies the Sobel filter to an image and returns the filtered image, gradient in the x-direction, and gradient in the y-direction.

+ image_to_sum_array: A function that converts an image to a 1-dimensional array that contains the sum of intensities in each row.

+ image_to_sobel: A function that converts an image to a 2-dimensional array that contains the gradient in the y-direction after applying the Sobel filter.

+ input1 and input2: Two inputs to the deep learning model, representing the gradient in the y-direction and the sum of intensities in each row, respectively.

+ tower_1 and tower_2: Two branches of the deep learning model that extract features from the inputs input1 and input2, respectively.

+ merged: A combination of the features from tower_1 and tower_2 that are then passed to the output layer to make the final prediction.

## Usage

The script assumes you have a directory named "Dataset" containing 3 subdirectories named "A", "B" and "C". These directories contain the image datasets of classes A, B and C, respectively. The dataset should be unzipped in the root directory with !unzip "/content/Dataset.zip" -d "/content".

The script starts by performing a Sobel Edge detection on each image and stores the result in two arrays, X1 and X2. X1 stores the Sobel image, while X2 stores the sum of the Sobel image for each row.

Next, it trains a neural network with two inputs, input1 and input2, that are then processed in two towers (tower_1 and tower_2) which are then concatenated and used as the final prediction. The output layer has 3 units and uses a softmax activation function. The model is then trained on the X1 and X2 arrays with their corresponding class labels Y.

The script ends by plotting the model using plot_model.

## Conclusion

This script performs a Sobel Edge detection on images, trains a neural network for image classification and plots the model architecture. It provides a starting point for further development or modifications for your own image classification tasks.
