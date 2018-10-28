import os
from io import BytesIO
from PIL import Image
import cv2 as cv
import numpy as np
from base64 import b64encode
import random

def detectFaces(img):
    gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    cascade = os.path.join(os.path.dirname(__file__), 'cascade.xml')
    face_cascade = cv.CascadeClassifier(cascade)
    return face_cascade.detectMultiScale(gray, 1.3, 5)

def pasteAlpaca(o_img, x, y, w, h):
    alpacadir = os.path.join(os.path.dirname(__file__), 'alpacas')
    img_path = os.path.join(alpacadir, random.choice(os.listdir(alpacadir)))
    a_img = cv.resize(np.array(Image.open(img_path)), (w, h))
    y1, y2 = y, y+a_img.shape[0]
    x1, x2 = x, x+a_img.shape[1]
    alpha_a = a_img[:, :, 3] / 255.0
    alpha_o = 1.0 - alpha_a
    for c in range(0,3):
        o_img[y1:y2, x1:x2, c] = (alpha_a * a_img[:, :, c] +
                                  alpha_o * o_img[y1:y2, x1:x2, c])


def alpacify(data):
    sbuf = BytesIO()
    sbuf.write(data)
    img = Image.open(sbuf)
    format = img.format
    mode = img.mode
    img = np.array(img)
    faces = detectFaces(img)
    for (x,y,w,h) in faces:
        pasteAlpaca(img,x,y,w,h)
    out = Image.fromarray(img, mode)
    outp = BytesIO()
    out.save(outp, format=format)
    return b64encode(outp.getvalue()).decode('utf-8'), (len(faces) != False)
