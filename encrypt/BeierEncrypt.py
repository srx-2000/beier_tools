#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :beier_tools 
@File    :BeierEncrypt.py
@IDE     :PyCharm 
@Author  :Beier
@Date    :2023/10/18 16:53 
@github  :https://github.com/srx-2000
'''
from Crypto.Cipher import AES, DES3
import base64
import hashlib

ENCODING = "utf8"

__unpad = lambda s: s[0:-ord(s[-1])]


def base64_en(code: str):
    return base64.b64encode(code.encode(ENCODING)).decode(ENCODING)


def base_64_de(code: str) -> bytes:
    return base64.b64decode(code.encode(ENCODING))


def sha_512(code: str):
    return hashlib.sha512(code.encode(ENCODING)).hexdigest()


def sha_256(code: str):
    return hashlib.sha256(code.encode(ENCODING)).hexdigest()


def md5(code: str):
    return hashlib.md5(code.encode(ENCODING)).hexdigest()


def aes_de_bs64(code: bytes, key: str):
    """
    这里传入的code是经过base64解密后的byte数组
    @param code: 待解密文本
    @param key: 秘钥
    @return:
    """
    cipher = AES.new(key.encode(ENCODING), AES.MODE_ECB)
    plaintext = cipher.decrypt(code)
    return __unpad(plaintext).decode(ENCODING)


def aes_de(code: str, key: str):
    """
    这里传入的code是待解密的字符串
    @param code: 待解密文本
    @param key: 秘钥
    @return:
    """
    cipher = AES.new(key.encode(ENCODING), AES.MODE_ECB)
    code = base64.b64decode(code)
    plaintext = cipher.decrypt(code)
    return __unpad(plaintext.decode(ENCODING))


def aes_en(code: str, key: str, vi=None):
    """
    aes加密
    @param code: 待加密文本
    @param key: 秘钥
    @param vi: 随机初始化
    @return:
    """
    if vi:
        cipher = AES.new(key.encode(ENCODING), AES.MODE_ECB, vi.encode(ENCODING))
    else:
        print(len(key.encode(ENCODING)))
        cipher = AES.new(key.encode(ENCODING), AES.MODE_ECB)
    count = len(code.encode(ENCODING))
    add = AES.block_size - (count % AES.block_size)
    pad_text = code + (chr(add) * add)
    ciphertext = cipher.encrypt(pad_text.encode(ENCODING))
    return base64.b64encode(ciphertext)


def des3_de(code: str, key: str):
    """
    des3解密
    @param code: 待加密文本
    @param key: 秘钥
    @return:
    """
    aes = DES3.new(key.encode(ENCODING), DES3.MODE_ECB)
    code = base_64_de(code).decode(ENCODING)
    res = bytes.fromhex(code)
    msg = aes.decrypt(res).decode(ENCODING)
    return __unpad(msg)


def des3_en(code: str, key: str, vi=None):
    """
    des3加密
    @param code: 待加密文本
    @param key: 秘钥
    @param vi: 随机初始化
    @return:
    """
    if vi:
        cipher = DES3.new(key[:24].encode(ENCODING), DES3.MODE_ECB, vi.encode(ENCODING))
    else:
        cipher = DES3.new(key[:24].encode(ENCODING), DES3.MODE_ECB)
    count = len(code.encode(ENCODING))
    add = DES3.block_size - (count % DES3.block_size)
    pad_text = code + (chr(add) * add)
    ciphertext = cipher.encrypt(pad_text.encode(ENCODING))
    return ciphertext.hex()


def des3_de_bs64(code: str, key: str):
    """
    des3解密
    @param code:这里传入的code是经过base64解密后的字符串
    @param key:秘钥
    @return:
    """
    aes = DES3.new(key.encode(ENCODING), DES3.MODE_ECB)
    res = bytes.fromhex(code)
    msg = aes.decrypt(res).decode(ENCODING)
    return __unpad(msg)
