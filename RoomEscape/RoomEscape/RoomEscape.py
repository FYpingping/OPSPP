from bangtal import *

scene1 = Scene('룸1', 'Image/배경-1.png')
scene2 = Scene('룸2', 'Image/배경-2.png')
scene3 = Scene('룸3', 'Image/배경-3.png')
scene4 = Scene('숨겨진 길','Image/복도2.png')

door1 = Object('Image/문-오른쪽-닫힘.png')
door1.locate(scene1, 800, 270)
door1.show()

door2 = Object('Image/문-왼쪽-열림.png')
door2.locate(scene2, 320, 270)
door2.show()

door3 = Object('Image/문-오른쪽-닫힘.png')
door3.locate(scene2, 920, 270)
door3.show()

key = Object('Image/열쇠.png')
key.setScale(0.2)
key.locate(scene1, 350, 150)
key.show()

flowerpot = Object('Image/화분.png')
flowerpot.locate(scene1, 300, 150)
flowerpot.show()

Box = Object('Image/Box(Closed)-sw.png')
Box.setScale(0.09)
Box.locate(scene2, 1100, 190)
Box.show()

keypad = Object('Image/키패드.png')
keypad.setScale(1.5)
keypad.locate(scene2, 890, 450)
keypad.show()

rollpaper = Object('Image/roll paper2.png')
rollpaper.setScale(0.03)
rollpaper.locate(scene2, 1130, 210)


cutton = Object('Image/커튼3-펴짐.png')
cutton.locate(scene2, 1050, 190)
cutton.show()

door4 = Object('Image/문-왼쪽-열림.png')
door4.locate(scene3, 500, 320)
door4.show()

hiddendoor = Object('Image/숨겨진 문.png')
hiddendoor.setScale(1.05)
hiddendoor.locate(scene3, 323, 20)

secretbox = Object('Image/비밀상자.png')
secretbox.setScale(1.2)
secretbox.locate(scene3, 0, 0)
secretbox.show()

gun = Object('Image/총.png')
gun.setScale(0.2)
gun.locate(scene3, 100, 70)

targetpaper = Object('Image/과녁-전.png')
targetpaper.setScale(0.15)
targetpaper.locate(scene3, 750, 400)
targetpaper.show()

picture = Object('Image/귀에 붕대를 감은 자화상-1.png')
picture.setScale(0.2)
picture.locate(scene3,1000, 400)
picture.show()

behindthepicture = Object('Image/액자 뒷면.png')
behindthepicture.locate(scene3, 400, 100)

key2 = Object('Image/A key.png')
key2.setScale(0.05)
key2.locate(scene3, 500, 140)




flowerpot.moved = False
def clickflowerpot(x, y, action):
    if flowerpot.moved == False:
        if action == MouseAction.DRAG_LEFT:
            flowerpot.locate(scene1, 200, 150)
            flowerpot.moved = True
        elif action == MouseAction.DRAG_RIGHT:
            flowerpot.locate(scene1, 400, 150)
            flowerpot.moved = True

def clickkey(x, y, action):
    key.pick()

door1.closed = True
def clickdoor1(x, y, action):
    if door1.closed:
        if key.inHand():
            door1.setImage('Image/문-오른쪽-열림.png')
            door1.closed = False
        else:
            showMessage('열쇠가 필요합니다.')
    else:
        scene2.enter()

def clickdoor2(x, y, action):
    scene1.enter()

cutton.moved = False
def clickcutton(x, y, action):
    if action == MouseAction.DRAG_RIGHT:
        cutton.setImage('Image/커튼3-접힘.png')
        cutton.locate(scene2, 1200, 190)
        cutton.moved = True

def clickbox(x, y, action):
    Box.setImage('Image/Box(Opened)-sw.png')
    rollpaper.show()

rollpaper.rolled = True
def clickrollpaper(x, y, action):
    if rollpaper.rolled:
        rollpaper.setImage('Image/paper.png')
        rollpaper.setScale(1)
        rollpaper.locate(scene2, 400, 300)
        rollpaper.rolled = False
    else:
        rollpaper.setImage('Image/roll paper2.png')
        rollpaper.setScale(0.03)
        rollpaper.locate(scene2, 1130, 210)
        rollpaper.rolled = True

door3.locked = True
door3.closed = True
def clickdoor3(x, y, action):
    if door3.locked:
        showMessage('문이 잠겨있습니다.')
    elif door3.closed:
        door3.setImage('Image/문-오른쪽-열림.png')
        door3.closed = False
    else:
        scene3.enter()

def clickkeypad(x, y, action):
    showKeypad('CAUSW', door3)

def door3unlock():
    showMessage('문의 잠금이 해제되었습니다.')
    door3.locked = False

def clickdoor4(x, y, action):
    scene2.enter()

def clickpicture(x, y, action):
    key2.show()
    behindthepicture.show()
    picture.hide()

def clickbackface(x, y, action):
    key2.hide()
    behindthepicture.hide()
    picture.show()

def clickkey2(x, y, action):
    key2.pick()

def clicksecretbox(x, y, action):
    if key2.inHand():
        showMessage('상자를 열었습니다.')
        secretbox.setImage('Image/비밀상자-1.png')
        gun.show()
    else:
        showMessage('상자를 열기 위해서는 열쇠가 필요합니다.')

def clickgun(x, y, action):
    gun.pick()

def clicktargetpaper(x, y, action):
    if gun.inHand():
        targetpaper.setImage('Image/과녁-후.png')
        showMessage('숨겨진 문이 나왔습니다.')
        hiddendoor.show()

hiddendoor.opened = False
def clickhiddendoor(x, y, action):
    if hiddendoor.opened == False:
        showMessage('숨겨진 문이 열렸습니다.')
        hiddendoor.setImage('Image/숨겨진 문-끝.png')
        hiddendoor.opened = True
    else:
        endGame()



key.onMouseAction = clickkey
flowerpot.onMouseAction = clickflowerpot
door1.onMouseAction = clickdoor1
door2.onMouseAction = clickdoor2
door3.onMouseAction = clickdoor3
door4.onMouseAction = clickdoor4
cutton.onMouseAction = clickcutton
Box.onMouseAction = clickbox
rollpaper.onMouseAction = clickrollpaper
keypad.onMouseAction = clickkeypad
door3.onKeypad = door3unlock    #door3에 붙은 키패드에서 이벤트가 발생하면 동작
picture.onMouseAction = clickpicture
behindthepicture.onMouseAction = clickbackface
key2.onMouseAction = clickkey2
secretbox.onMouseAction = clicksecretbox
gun.onMouseAction = clickgun
targetpaper.onMouseAction = clicktargetpaper
hiddendoor.onMouseAction = clickhiddendoor

startGame(scene1)