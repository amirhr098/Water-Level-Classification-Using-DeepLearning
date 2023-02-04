import cv2
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import tensorflow as tf
import numpy as np
import serial

##############################################
##############################################
##############################################

def Sobel(gray):
    scale = 1
    delta = 0
    ddepth = cv2.CV_16S
    gray = cv2.GaussianBlur(gray, (7, 7), 0)
    grad_y = cv2.Sobel(gray, ddepth, 0, 1, ksize=3, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)
    abs_grad_y = cv2.convertScaleAbs(grad_y)
    return np.array(abs_grad_y)

def Degree(image):
    c = Sobel(image)
    high = []
    for line in c:
        high.append(sum(line))
    return np.array(high)

def Predict(image,model):
    x1 = np.array([np.array(Sobel(image))])
    x2 = np.array([np.array(Degree(image))])
    a = model.predict_on_batch([x1,x2])
    return np.argmax(a)

##############################################
##############################################
##############################################

ser = serial.Serial(port = "COM4", baudrate=9600, parity = serial.PARITY_NONE)
print(ser.name)
print(ser.baudrate)
print(ser.parity)

model = tf.keras.models.load_model("H:\Codes\Water Level Classification\Model_3.h5")

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame1 = vc.read()
else:
    rval = False

frame1 = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)

while rval:

    rval, frame2 = vc.read()
    frame2 = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)

    if((np.sum(frame1-frame2)/1000000)>37):

        rval, t1 = vc.read()
        rval, t2 = vc.read()
        rval, t3 = vc.read()
        var = 0

        for im in [t1,t2,t3]:
            im = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
            temp = cv2.Laplacian(im, cv2.CV_64F).var()
            if(var<temp):
                frame2 = im
                var = temp

        label = Predict(frame2,model)

        ser.write(label)
        print("Sent to serial: " + str(label))
        t = 3000

    else:
        t = 0


    frame1 = frame2
    cv2.imshow("preview", frame2)
    key = cv2.waitKey(20+t)
    if key == 27: # exit on ESC
        break
    

vc.release()
cv2.destroyWindow("preview")
ser.close()