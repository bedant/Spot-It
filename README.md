# Spot-It
An application to find a word or phrase in the images of hard copies. 

## Some of the instances where "Spot It" will be useful
- Searching for a particular information in the hard copy of a long document. 
- Looking for the Mfg Date and other stuffs on the wrapper of food products.

## Steps to run the code
- $ pip install pillow
- $ pip install pytesseract
- install tesseract according to OS (refer this : https://python-forum.io/Thread-Convert-text-from-an-image-to-a-text-file)
- put ocr.py and find_single_word.py in a directory
- $ python ocr.py --image \<path to image\> --search \<query\>
