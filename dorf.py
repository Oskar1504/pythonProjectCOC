
import pyautogui
import debug

debug = debug.Debug()

def checkTh():

    debug.info("analysing th level")

    for lvl in range(6,9):
        th = checkThLvl(lvl)
        if th:
            debug.debug("TH pos x:"+str(th.left)+" | y:"+str(th.top))
            return lvl



def checkThLvl(lvl):
    imageName = "images/th/th_"+str(lvl)+".png"
    confidence = 1
    # lowering detail filter as soon as more than 0 objects found it marks them
    # i added this so the filter is dynamic
    #  if the filter is to low it would multi find the same structure
    while len(list(pyautogui.locateAllOnScreen(imageName,confidence=confidence))) == 0 and confidence >= 0.9:
        confidence -= 0.025

    scan = list(pyautogui.locateAllOnScreen(imageName,confidence=confidence))

    if len(list(scan)) == 0:
        return False
    else:
        return scan[0]

def checkAd():

    debug.info("analysing AD level")

    for lvl in range(1,7):
        ads = checkAdLvl(lvl)
        if ads:
            debug.debug("AD lvl: " + str(lvl))
            for ad in ads:
                debug.debug("AD pos x:"+str(ad.left)+" | y:"+str(ad.top))


def checkAdLvl(lvl):
    imageName = "images/ad/ad_"+str(lvl)+".png"
    confidence = 1
    # lowering detail filter as soon as more than 0 objects found it marks them
    # i added this so the filter is dynamic
    #  if the filter is to low it would multi find the same structure
    while len(list(pyautogui.locateAllOnScreen(imageName,confidence=confidence))) == 0 and confidence >= 0.85:
        confidence -= 0.025

    scan = list(pyautogui.locateAllOnScreen(imageName,confidence=confidence))

    if len(list(scan)) == 0:
        return False
    else:
        return scan