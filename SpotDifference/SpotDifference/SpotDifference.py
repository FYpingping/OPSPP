from bangtal import *

setGameOption(GameOption.INVENTORY_BUTTON, False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON, False)

scene1 = Scene('틀린그림찾기', 'Images/problem.png')

problem = Object('Images/problem.png')
problem.locate(scene1, 0, 0)
problem.show()

check_margin = 34


class Rect:         #클래스는 멤버 변수와 멤버 함수를 갖게 됨
    def __init__(self,  cx, cy, r): # 생성자 함수는 항상 __@@@__ 형식
        self.centerx = cx
        self.centery = cy
        self.radius = r             # 이 세개는 속성이라고 본다. 사각형에 대한 속성

    def checkin(self, x, y):        # 클래스의 멤버는 항상 self 파라미터로 스스로를 알 수 있게 됨. 사각형의 속성들이 저장되었을 떄 체크인이라는 함수를 통해 기능을 수행
        return self.centerx - self.radius < x < self.centerx + self.radius and self.centery - self.radius < y < self.centery + self.radius      #이런 것들을 멤버 함수
    
    #그 객체의 속성과 그 개체 속성을 다루는 함수를 하나로 캡슐화 하는게 클래스 라는 개념이다.



class DifferencePoint:
    def __init__(self, lcx, rcx, cy, r):
        self.left_rect = Rect(lcx, cy, r)
        self.right_rect = Rect(rcx, cy, r)
        self.left_check = Object("Images/check.png")
        self.left_check.locate(scene1, lcx - check_margin, cy - check_margin)
        self.right_check = Object("Images/check.png")
        self.right_check.locate(scene1, rcx - check_margin, cy - check_margin)
        self.found = False

    def checkin(self, x, y):
        return self.left_rect.checkin(x, y) or self.right_rect.checkin(x, y)

    def show(self):
        self.left_check.show()
        self.right_check.show()
        self.found = True

# 첫번째 위치 (568, 594) - 54 , (1186, 594) - 54

points = [
DifferencePoint(568, 1186, 594, 54),
DifferencePoint(99, 717, 551, 17),
DifferencePoint(383, 1001, 482, 16),
DifferencePoint(401, 1019, 158, 27),
DifferencePoint(61, 679, 255, 36),
DifferencePoint(592, 1210, 421, 35),
DifferencePoint(320, 938, 117, 13)
]

count = 0
def clickobjectproblem(x, y, action):
    wrong = True
    global count
    for p in points:                #for은 반복문, (모든 points에 있는 p에 대해서)
        if p.checkin(x, y):
            if p.found == False:
                p.show()
                count += 1
                wrong = False
    if count == 7:
        showMessage("다 찾았습니다.")
    if wrong:
        endGame()

problem.onMouseAction = clickobjectproblem


showMessage('좌 우에 틀린 곳을 찾으세요')


startGame(scene1)