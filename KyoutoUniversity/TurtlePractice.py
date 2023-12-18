from turtle import *
import random

def twoCircle():
    t1 = Turtle()
    t2 = Turtle()
    t1.color("red")
    t2.color("blue")
    for i in range(180):
        t1.forward(5)
        t2.forward(3)
        t1.left(2)
        t2.left(2)
        (x,y) = t1.pos()
        print(x,y)
    done()

def come(x,y):
    (xx,yy) = pos()
    newxy = ((x), (y))
    goto(newxy)
# onscreenclick(come)
    done()

def blackball():
    stop_flag = False
    # マウスがクリックされたときの関数, 引数 x, y をとるように
    # しないといけないが, 使わない
    # 実行停止フラグを True にする
    def clicked(x,y):
        global stop_flag
        stop_flag = True
    #
    # マウスがクリックされたときの動作を指定, clicked 関数を
    # 呼び出す
    #
    onscreenclick(clicked)
    speed(0)
    while(not stop_flag):
        # -90 度から 90 度の範囲でランダムに向きを変える
        left(random.randint(-90,90))
        forward(10)
        # タートルの位置が原点から一定の距離を超えれば, 戻る
        if position()[0]**2+position()[1]**2 > 200**2:
            forward(-10)

def detour(L):
    if L < 10:
        forward(L)
    else:
        LL = L/3
        detour(LL)
        left(60)
        detour(LL)
        right(120)
        detour(LL)
        left(60)
        detour(LL)
for i in range(6):
    detour(100)