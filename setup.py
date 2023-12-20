# setup.py文件内容
from setuptools import setup

setup(
    name='beierTools',  # 应用名（pip安装和卸载时的名字）
    version='0.0.14',  # 当前版本，每次打包都需要更改，否则上传时会重复报错
    author='Beier',  # 作者
    author_email='1601684622@qq.com',  # 作者邮箱
    licence='MIT License',  # 许可协议
    url='https://github.com/srx-2000/beier_tools',  # 应用主页链接
    description='Beier developments tools', # 描述
    packages=["encrypt", "operation"], # 如果要打包的目标中有多个模块，需要加上这行，列表中的元素就是模块名
    install_requires=["pycryptodome>=3.18.0"],  # 依赖包
)