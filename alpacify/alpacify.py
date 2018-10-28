import os
from io import BytesIO
from PIL import Image
import cv2 as cv
import numpy as np
import base64

def detectFaces(img):
    gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    dirname = os.path.dirname(__file__)
    cascade = os.path.join(dirname, 'cascade.xml')
    face_cascade = cv.CascadeClassifier(cascade)
    return face_cascade.detectMultiScale(gray, 1.3, 5)

def alpacify(data):
    sbuf = BytesIO()
    sbuf.write(data)
    img = Image.open(sbuf)
    format = img.format
    mode = img.mode
    img = np.array(img)
    for (x,y,w,h) in detectFaces(img):
        cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0, 255), 2)
    out = Image.fromarray(img, mode)
    outp = BytesIO()
    out.save(outp, format=format)
    return base64.b64encode(outp.getvalue()).decode('utf-8')
