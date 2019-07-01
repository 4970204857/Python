

class Stack(object):
    def __init__(self):
        self.array = [[], []]


    def l_push(self, data):
        print("数组2添加数据",data)
        self.array[0].append(data)

    def l_pop(self):
        if len(self.array[0]) == 0:
            print('Stack a is empty')
        else:
            print('数组2删除最后的元素')
            self.array[0].pop()

    def r_push(self, data):
        print("数组1添加数据", data)
        self.array[1].append(data)

    def r_pop(self):
        if len(self.array[1]) == 0:
            print('Stack b is empty')
        else:
            print('数组1删除最后的元素')
            self.array[1].pop()

    def show(self):

        if len(self.array[0]) == 0:
            print('数组2 为Null')
        else:
            print('数组2:', self.array[0])
        if len(self.array[1]) == 0:
            print('数组1 为Null')
        else:
            print('数组1:', self.array[1],'\n\n')


import unittest #导入unittest模块 
import time
class WidgetTestCase(unittest.TestCase):

    def setUp(self):
        self.Stack = Stack()

    def test_1_r_push_one(self):
        self.Stack.r_push(1)
        self.Stack.show()
        time.sleep(2)
        self.Stack.r_push(2)
        self.Stack.show()
        time.sleep(2)
        self.Stack.r_push(3)
        self.Stack.show()
        time.sleep(2)
        self.Stack.r_push(4)
        self.Stack.show()
        time.sleep(2)
        self.Stack.l_push(5)
        self.Stack.show()
        time.sleep(2)
        self.Stack.l_push(6)
        self.Stack.show()
        time.sleep(2)
        self.Stack.l_push(7)
        self.Stack.show()
        time.sleep(2)
        self.Stack.l_push(8)
        self.Stack.show()
        time.sleep(2)
        self.Stack.l_push(9)
        self.Stack.show()
        time.sleep(2)
        self.Stack.r_pop()
        self.Stack.show()
        time.sleep(2)
        self.Stack.show()
        self.Stack.r_pop()
        time.sleep(2)
        self.Stack.show()
        self.Stack.r_pop()
        time.sleep(2)
        self.Stack.show()
        self.Stack.l_pop()
        time.sleep(2)
        self.Stack.show()
        self.Stack.l_pop()
        time.sleep(2)
        self.Stack.show()
        self.Stack.l_pop()
        time.sleep(2)
        self.Stack.show()
        self.Stack.l_pop()
        time.sleep(2)
        self.Stack.show()
        self.Stack.l_pop()
        time.sleep(2)
        self.Stack.show()






if __name__ == '__main__':

    '''栈：是一种运算受限的线性表，其特点在于仅允许在一端进行元素的插入和删除操作，最后入栈的最先出栈，而最先入栈的元素最后出栈'''

    unittest.main()
