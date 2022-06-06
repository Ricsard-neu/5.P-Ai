import cv2
from cv2 import triangulatePoints
import numpy as np
from matplotlib import pyplot as plt

ismert = ""
talalt = False


img = cv2.imread('images/triangle.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

i = 0

for contour in contours:


	approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)

	if len(approx) == 3:
		ismert = "haromszog"
		talalt = True

	elif len(approx) == 4:
		ismert = "Négyszog"
		talalt = True
	elif len(approx) == 5:
		ismert = ""
		talalt = False
	elif len(approx) == 6:
		ismert = ""
		talalt = False
	else:
		ismert = "Kör"
		talalt = True

print(len(approx))

if talalt == True:
	print("A talált forma egy:",ismert)
else:
	print("Ezt a formát jelenleg nem ismerem fel")



