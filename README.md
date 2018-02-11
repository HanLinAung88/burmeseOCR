# burmeseOCR
OCR for Burmese

Based on https://www.pyimagesearch.com/2017/07/10/using-tesseract-ocr-python/ and Tesseract. 

Applies preprocessing using OpenCV and then uses Tesseract for OCR (works for version 3.05)

To OCR an image(example.jpg):

Command line: python ocr.py --i example.jpg

The text will be written out on the terminal and will also be outputed to a file named Output.txt
