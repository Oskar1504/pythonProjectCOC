import pyautogui
import debug

debug = debug.Debug()


def checkTh():
    debug.info("analysing th level")
    for lvl in range(6, 9):
        pos = checkThLvl(lvl)
        if pos:
            return {"lvl": lvl, "pos": pos}


def checkThLvl(lvl):
    imageName = "images/th/th_" + str(lvl) + ".png"
    confidence = 0.9
    scan = list(pyautogui.locateAllOnScreen(imageName, confidence=confidence))

    if len(list(scan)) == 0:
        return False
    else:
        return scan[0]


def checkAd():
    debug.info("analysing AD level")
    output = []
    for lvl in range(1, 7):
        ads = checkAdLvl(lvl)
        temp = {}
        if ads:
            temp['lvl'] = lvl
            temp['chords'] = []
            temp['chords'].append(ads[0])

            # kills double found pictures and append it on temp object which  is added to output
            for ad in ads:
                for i in range(0, len(temp['chords'])):
                    if ad.left > temp['chords'][i].left + temp['chords'][i].width or ad.left < temp['chords'][i].left:
                        if ad.top > temp['chords'][i].top + temp['chords'][i].height or ad.top < temp['chords'][i].top or  ad.top == temp['chords'][i].top:
                            if i == len(temp['chords']) - 1:
                                temp['chords'].append(ad)

            output.append(temp)
    return output


def checkAdLvl(lvl):
    imageName = "images/ad/ad_" + str(lvl) + ".png"

    scan = list(pyautogui.locateAllOnScreen(imageName, confidence=0.825))

    if len(list(scan)) == 0:
        return False
    else:
        return scan
