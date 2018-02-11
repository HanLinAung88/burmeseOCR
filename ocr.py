# import the necessary packages
from PIL import Image
import pytesseract
import argparse
import cv2
import os
#from tesserocr import PyTessBaseAPI

#Based on https://www.pyimagesearch.com/2017/07/10/using-tesseract-ocr-python/ for preprocessing

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image to be OCR'd")
ap.add_argument("-p", "--preprocess", type=str, default="thresh",
	help="type of preprocessing to be done")
args = vars(ap.parse_args())

# load the example image and convert it to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# check to see if we should apply thresholding to preprocess the
# image
gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# make a check to see if median blurring should be done to remove
# noise
gray = cv2.medianBlur(gray, 3)

# write the grayscale image to disk as a temporary file so we can
# apply OCR to it
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)

# load the image as a PIL/Pillow image, apply OCR, and then delete
# the temporary file
image = Image.open(filename)
#text = tesserocr.image_to_text(image)  # print ocr text from image
text = pytesseract.image_to_string(Image.open(filename), 'mya')
os.remove(filename)

#print out the text on the command line and writes it to the file called Output.txt
text_file = open("Output.txt", "w")
text_file.write(text.encode('utf8'))
text_file.close()
print(text)
