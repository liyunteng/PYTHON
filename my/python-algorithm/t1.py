#!/usr/bin/env python
# -*- coding: utf-8 -*-

# t1.py - t1

# Date   : 2019/12/25

def cover(board, lab=1, top=0, left=0, side=None):
    if side is None: side = len(board)

    s = side // 2

    offsets = (0, -1), (side-1, 0)

    for dy_outer, dy_inner in offsets:
        for dx_outer, dx_inner in offsets:
            if not board[top+dy_outer][left+dx_outer]:
                board[top+s+dy_inner][left+s+dx_inner] = lab

    lab += 1
    if s > 1:
        for dy in [0, s]:
            for dx in [0, s]:
                lab = cover(board, lab, top+dy, left+dx, s)
                print_board(board)
                print()

    return lab


def print_board(board):
    for row in board:
        print((' %2i' * 8) % tuple(row))


board = [[0] * 8 for i in range(8)]
board[0][7] = -1
print_board(board)
print()
cover(board)
print_board(board)
