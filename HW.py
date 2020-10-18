from bangtal import *
#pip install bangtal

scene1 = Scene('룸1','Images\배경-1.png')
scene2 = Scene('룸2','Images\배경-2.png')

door1 = Object('Images\문-오른쪽-닫힘.png')
door1.locate(scene1,800,270)
door1.show()
door1.closed   =   True

def door1_onMouseAction(x,y,action):
    if door1.closed == True:
        if key.inHand() == True:
           door1.setImage('Images\문-오른쪽-열림.png')
           door1.closed = False
        else:
            showMessage('열쇠를 잡으세요!')
    else:
        scene2.enter()

#도어1 설정

key = Object('Images\열쇠.png')
key.locate(scene1,400,150)
key.setScale(0.2)
key.show()

def key_onMouseAction(x,y,action):
    key.pick()

#도어1 키 설정

door2 = Object('Images\문-오른쪽-닫힘.png')
door2.locate(scene2,800,270)
door2.show()
door2.closed   =   True

def door2_onMouseAction(x,y,action):
    if door2.closed == True:
        door2.setImage('Images\문-오른쪽-열림.png')
        door2.closed = False
    else:
        endGame()
        #3232
#도어 2 설정

door3 = Object('Images\문-왼쪽-열림.png')
door3.locate(scene2,300,270)
door3.show()

def door3_onMouseAction(x,y,action):
    scene1.enter()

#도어 3 설정
tree_size = 1;
tree = Object('Images\나무.png')
tree.locate(scene2,450,150)
tree.show()

def tree_onMouseAction(x,y,action):
    global tree_size
    tree_size = tree_size-0.1;
    tree.setScale(tree_size)


#나무 설정
showMessage('20145842 최필립.')

key.onMouseAction=key_onMouseAction
door1.onMouseAction=door1_onMouseAction
door2.onMouseAction=door2_onMouseAction
door3.onMouseAction=door3_onMouseAction
tree.onMouseAction=tree_onMouseAction
startGame(scene1)

