"""
    作者：LongXiShao
    功能：利用递归绘制分行树
    版本：1.0
    日期：2018-09-30
"""

import turtle


def set_pencolor(length,Limit_value):
    # 根据长度设置画笔颜色
    if length < Limit_value:
        turtle.pencolor("green")
    else:
        # 将树干的颜色设成棕色
        turtle.pencolor("#CD6600")
def draw_branch(length,pensize):
    """
        递归画树
    """
    # 每次减少的树枝的长度
    REDUCE_LENGHTH = 10

    # 每次转的角度
    ROTATION_DEGREE = 25

    if length > 5:
        set_pencolor(length,40)
        turtle.pensize(pensize)
        #绘制右侧树枝
        turtle.forward(length)
        turtle.right(ROTATION_DEGREE)
        draw_branch(length-REDUCE_LENGHTH,pensize-1)

        # 绘制左侧树枝
        turtle.left(ROTATION_DEGREE * 2)
        draw_branch(length - REDUCE_LENGHTH,pensize-1)

        set_pencolor(length, 40)
        # 返回上一个节点
        turtle.right(ROTATION_DEGREE)
        turtle.backward(length)

def main():
    """
        主函数
    """
    # 设置画笔
    turtle.bgcolor("black")
    turtle.speed(0)
    turtle.left(90)
    turtle.penup()
    turtle.backward(250)
    turtle.pendown()

    # 开始画树
    draw_branch(100,10)
    turtle.exitonclick()

if __name__ == '__main__':
    main()
