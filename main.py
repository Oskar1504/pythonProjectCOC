import time

import pyautogui

import dorf
import debug
import Loot


def search():
    chords = pyautogui.locateOnScreen("images/search.png", confidence=0.7)
    if chords:
        pyautogui.click(chords.left, chords.top)


def inSearch():
    return pyautogui.locateOnScreen("images/search.png", confidence=0.7)


def cancelFight():
    chords = pyautogui.locateOnScreen("images/cancelFight.png", confidence=0.7)
    if chords:
        pyautogui.click(chords.left, chords.top)
    debug.warning("canceling fight")


def main():
    queue = 10

    for i in range(0, queue):
        debug.debug("queue: " + str(i+1) + "/" + str(queue))
        debug.info("start search")
        search()
        time.sleep(1)
        while not inSearch():
            time.sleep(1)

        debug.info("enemy found")

        loot = Loot.getLoot()

        debug.data(debug.LightYellow + "Gold: " + str(loot[0]) + debug.LightMagenta + " | Elixir: " + str(loot[1]) + debug.LightGray + " | Dark Elixir: " + str(loot[2]))

        th = dorf.checkTh()
        if th:
            debug.data("TH lvl: " + str(th['lvl']))
            debug.debug("Pos x: " + str(th['pos'].left) + " | y: " + str(th['pos'].top))

        ads = dorf.checkAd()
        #just debug
        for ad in ads:
            debug.data("AD lvl: " + str(ad['lvl']) + " | Amount: " + str(len(ad['chords'])))
            for pos in ad['chords']:
                debug.debug("Pos x: " + str(pos.left) + " | y: " + str(pos.top))

        # debug delay
        time.sleep(8)


    cancelFight()
    debug.info("Finished queue")


debug = debug.Debug()

main()