import cv2
import numpy

def convertImage(frame):
    height, width = frame.shape

    ascii = ""

    row = 0
    col = 0
    while row < height:
        while col < width:
            ascii = "{}{}".format(ascii, ascii_string[int((numpy.mean(frame[row:int(row + (height / pixel_height)), col:int(col + (width / pixel_width))]) / 255) * (len(ascii_string) - 1))])
            col = int(col + (width / pixel_width))
        ascii = "{}\n".format(ascii)
        row = int(row + (height / pixel_height))
        col = 0

    return ascii

pixel_width = int(input("Image Width? :: "))
pixel_height = int(input("Image Height? :: "))
ascii_string = [" ",".",":","-","=","+","*","#","%","@","&"]

user_input = input("Image or Video? [I/V] :: ")

while user_input != "I" and user_input != "V":
    user_input = input("Input Listed Response. Image or Video? [I/V] :: ")

if user_input == "I":
    user_input = input("Enter Image Path :: ")

    frame = cv2.cvtColor(cv2.imread(user_input), cv2.COLOR_BGR2GRAY)

    print(convertImage(frame))
elif user_input == "V":
    print("Loading camera...")
    camera = cv2.VideoCapture(0)

    while True:
        _, frame = camera.read()
        
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        print(convertImage(frame))