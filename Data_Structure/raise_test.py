'''
使用raise主动抛出异常
'''

def test_raise(n):
    if not isinstance(n, int):
        raise Exception("not a int type")
    else:
        print("good")

test_raise(8.9)
