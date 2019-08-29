import numpy as np
from Pointer import Pointer
from mirror import Switch


def process(ar):
    arr = []
    for item in ar:
        arr.append(list(item))
    matrix = np.array(arr)
    length, width = matrix.shape
    path = []
    cursor = Pointer()

    while True:
        if cursor.xcoor >= width or cursor.xcoor < 0 or cursor.ycoor >= length or cursor.ycoor < 0:
            # result.append([cursor.ycoor, cursor.xcoor - 1])
            break
        path.append((cursor.xcoor, cursor.ycoor))
        if matrix[cursor.ycoor][cursor.xcoor] == '/' or matrix[cursor.ycoor][cursor.xcoor] == "\\":
            myswitch = Switch(matrix[cursor.ycoor][cursor.xcoor])
            if myswitch.type == '/':
                cursor.right_switch()
            elif myswitch.type == '\\':
                cursor.left_switch()

        x_move, y_move = cursor.getMove()
        cursor.xcoor += x_move
        cursor.ycoor += y_move

    return path


