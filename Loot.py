
import PIL.Image
import numpy as np
import pytesseract
import debug
import pyautogui

debug = debug.Debug()
THRESHOLD = 197


def imageToString(image , threshold):
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract/tesseract.exe'
    return pytesseract.image_to_string(killColor(image , threshold))

def convertToGrayscale(image):
    grayscale = image.convert("L")
    return grayscale

def killColor(image,threshold):
    grayImage = convertToGrayscale(image)
    arr = np.array(grayImage)

    # i make all rgb value which are higher than threshold to 255 and lower to 0
    # so the numbers which are a mixture of very white pixels get white and other shit
    # gets killed

    # this is necessary to have an nice result on the pytesseract.image_to_string function

    for i in range(0,len(arr)):
        for j in range(0,len(arr[i])):
            if(arr[i][j] >= threshold):
                arr[i][j] = 0
            else:
                arr[i][j] = 255
    return PIL.Image.fromarray(arr)

# Analyzing loot
def getLoot():
    debug.info("analysing loot")

    chords = pyautogui.locateOnScreen("images/lootStart.png", confidence=0.7)

    if chords:
        # amcht nen screenshot von den loot bereich
        im = pyautogui.screenshot(region=(chords.left + chords.width, chords.top, 150, chords.height - 95))

        # covnert  screenshot 2 array
        loot = imageToString(im, THRESHOLD).split("\n")

        # there is always an useless string at the end so i delete this when existing
        if len(loot) >= 4:
            loot.pop()

        # debug.debug(str(loot))

        # sanatizing and converting data array
        for i in range(0,len(loot)):

            #should delete empty fields in array
            if loot[i] == '':
                loot.pop(i)

            #killing whitespace so toInt works
            loot[i] = loot[i].replace(" ", "")

            #changing commen imageTOStirng porblems
            loot[i] = loot[i].replace("s", "5")
            loot[i] = loot[i].replace("S", "5")
            loot[i] = loot[i].replace("t", "5")
            loot[i] = loot[i].replace("G", "6")
            loot[i] = loot[i].replace("o", "0")
            loot[i] = loot[i].replace("O", "0")
            loot[i] = loot[i].replace("N", "11")
            loot[i] = loot[i].replace("W", "11")
            loot[i] = loot[i].replace("U", "11")
            loot[i] = loot[i].replace("°", "")
            loot[i] = loot[i].replace('"', "")
            loot[i] = loot[i].replace(".", "")
            loot[i] = loot[i].replace(",", "")
            loot[i] = loot[i].replace(":", "")
            loot[i] = loot[i].replace("-", "")
            loot[i] = loot[i].replace("©", "")
            loot[i] = loot[i].replace(")", "")
            loot[i] = loot[i].replace("(", "")
            loot[i] = loot[i].replace("}", "")
            loot[i] = loot[i].replace("{", "")
            loot[i] = loot[i].replace("!", "1")
            loot[i] = loot[i].replace("'", "1")
            loot[i] = loot[i].replace("l", "1")
            loot[i] = loot[i].replace("i", "1")
            loot[i] = loot[i].replace("a", "2")
            loot[i] = loot[i].replace("r", "2")
            loot[i] = loot[i].replace("e", "2")
            loot[i] = loot[i].replace("c", "3")
            loot[i] = loot[i].replace("E", "3")
            loot[i] = loot[i].replace("A", "")
            loot[i] = loot[i].replace("|", "")

            #covnerting to int
            loot[i] = int(loot[i])

        return loot
    else:
        debug.warning("evaluating loot not all 3 Ressources found")
        return [0,0,0]
