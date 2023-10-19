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
from Crypto.Cipher import AES
import base64
import hashlib


def base64_en(code: str):
    return base64.b64encode(code.encode("utf8")).decode("utf8")


def base_64_de(code: str) -> bytes:
    return base64.b64decode(code.encode("utf-8"))


def sha_512(code: str):
    return hashlib.sha512(code.encode("utf8")).hexdigest()


def sha_256(code: str):
    return hashlib.sha256(code.encode("utf8")).hexdigest()


def aes_de_bs64(code: bytes, key: str):
    """
    这里传入的code是经过base64解密后的byte数组
    @param code: 待解密文本
    @param key: 秘钥
    @return:
    """
    cipher = AES.new(key.encode('utf8'), AES.MODE_ECB)
    plaintext = cipher.decrypt(code)
    unpad = lambda s: s[0:-s[-1]]
    return unpad(plaintext).decode('utf8')


def aes_de(code: str, key: str):
    """
    这里传入的code是待解密的字符串
    @param code: 待解密文本
    @param key: 秘钥
    @return:
    """
    cipher = AES.new(key.encode('utf8'), AES.MODE_ECB)
    code = base64.b64decode(code)
    plaintext = cipher.decrypt(code)
    unpad = lambda s: s[0:-ord(s[-1])]
    return unpad(plaintext.decode('utf-8'))


def aes_en(code: str, key: str, vi=None):
    """
    aes加密
    @param code: 待解密文本
    @param key: 秘钥
    @param vi: 随机初始化
    @return:
    """
    if vi:
        cipher = AES.new(key.encode(), AES.MODE_ECB, vi.encode())
    else:
        cipher = AES.new(key.encode(), AES.MODE_ECB)
    count = len(code.encode('utf-8'))
    add = AES.block_size - (count % AES.block_size)
    pad_text = code + (chr(add) * add)
    ciphertext = cipher.encrypt(pad_text.encode("utf8"))
    return base64.b64encode(ciphertext)
