from bangtal import *

setGameOption(GameOption.INVENTORY_BUTTON, False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON, False)

scene1 = Scene('산타레이스','Images/background.png')

santa = Object('Images/santa.png')
santa.x = 0
santa.y = 500
santa.locate(scene1, santa.x, santa.y)


startbutton = Object('Images/start.png')
startbutton.locate(scene1, 610, 300)
startbutton.show()

playbutton = Object('Images/play.png')
playbutton.locate(scene1, 610, 30)

endbutton = Object('Images/end.png')
endbutton.locate(scene1, 610, 120)

restartbutton = Object('Images/restart.png')
restartbutton.locate(scene1, 610, 210)


timer = Timer(10. )
showTimer(timer)

def clickplaybutton(x, y, action):
    santa.x += 30
    santa.locate(scene1, santa.x, santa.y)
    if santa.x > 1280:
        showMessage('선물 배달 성공')
        playbutton.hide()
        restartbutton.show()
        endbutton.show()
        timer.stop()



def clickstartbutton(x, y, action):
    startbutton.hide()
    santa.show()
    playbutton.show()
    timer.start()


def clickendbutton(x, y, action):
    endGame()

def clickrestartbutton(x, y, action):
    santa.x = 0
    santa.locate(scene1, santa.x, santa.y)
    santa.show()
    restartbutton.hide()
    endbutton.hide()
    playbutton.show()
    timer.set(10.)
    timer.start()

def timeout():
    showMessage('선물 배달 실패')
    santa.hide()
    playbutton.hide()
    restartbutton.show()
    endbutton.show()

    

playbutton.onMouseAction = clickplaybutton
startbutton.onMouseAction = clickstartbutton
endbutton.onMouseAction = clickendbutton
restartbutton.onMouseAction = clickrestartbutton
timer.onTimeout = timeout


startGame(scene1)
