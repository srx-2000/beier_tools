import ctypes


# 由于python的逻辑运算与js的逻辑运算有一些区别，这里加入一个转换类
class JsOperate:
    @staticmethod
    def unsigned_right_shift(x, bit):
        """
        无符号右移
        @param x:需要移动的值
        @param bit:移动的位数
        @return:
        """
        x, y = ctypes.c_uint32(x).value, bit % 32
        return ctypes.c_uint32(x >> y).value

    @staticmethod
    def unsigned_left_shift(x, bit):
        """
        无符号左移
        @param x:需要移动的值
        @param bit:移动的位数
        @return:
        """
        x, y = ctypes.c_uint32(x).value, bit % 32
        return ctypes.c_uint32(x << y).value

    @staticmethod
    def js_signed_right_shift(x, bits):
        """
        有符号右移
        @param x:需要移动的值
        @param bits:移动的位数
        @return:
        """
        # 32 位整数的掩码
        mask = (1 << 32) - 1
        # 将 x 视为 32 位有符号整数
        x = x & mask
        # 执行有符号右移操作
        result = (x >> bits)
        # 如果 x 是负数，则将最高位以外的位设置为1，以保持负数符号
        if x & (1 << 31):
            result |= (mask ^ (1 << 31))
        return result

    @staticmethod
    def js_and(x, y):
        """
        与运算
        @param x:
        @param y:
        @return:
        """
        return ctypes.c_int(x & y).value

    @staticmethod
    def js_xor(x, y):
        """
        亦或运算
        @param x:
        @param y:
        @return:
        """
        return ctypes.c_int(x ^ y).value

    @staticmethod
    def js_signed_left_shift(x, bits):
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
