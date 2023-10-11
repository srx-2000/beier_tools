import ctypes


# 由于python的逻辑运算与js的逻辑运算有一些区别，这里加入一个转换类
def urs(x, bit):
    """
    无符号右移
    @param x:需要移动的值
    @param bit:移动的位数
    @return:
    """
    x, y = ctypes.c_uint32(x).value, bit % 32
    return ctypes.c_uint32(x >> y).value


def uls(x, bit):
    """
    无符号左移
    @param x:需要移动的值
    @param bit:移动的位数
    @return:
    """
    x, y = ctypes.c_uint32(x).value, bit % 32
    return ctypes.c_uint32(x << y).value


def srs(x, bits):
    """
    有符号右移
    @param x:需要移动的值
    @param bits:移动的位数
    @return:
    """
    # 使用 ctypes 模块将数值强制转换为有符号 32 位整数
    value = ctypes.c_int32(x).value
    result = value >> bits
    return result


def sls(x, bits):
    """
    有符号左移
    @param x: 需要移动的
    @param bits: 移动的位数
    @return:
    """
    # 32 位整数的掩码
    mask = (1 << 32) - 1
    # 将 x 视为 32 位有符号整数
    x = x & mask
    # 执行有符号左移操作
    result = (x << bits) & mask
    # 如果结果大于等于 2^31，则减去 2^32 得到负数
    if result >= (1 << 31):
        result -= (1 << 32)
    return result


def band(x, y):
    """
    与运算
    @param x:
    @param y:
    @return:
    """
    return ctypes.c_int(x & y).value


def bxor(x, y):
    """
    亦或运算
    @param x:
    @param y:
    @return:
    """
    return ctypes.c_int(x ^ y).value
