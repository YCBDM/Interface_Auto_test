# coding=utf-8
import pytest
import sys


# 功能函数
def multiply(a, b):
    print(sys._getframe().f_code.co_name)


if __name__ == '__main__':
    multiply(1, 2)
