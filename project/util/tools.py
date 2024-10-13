""" 工具类函数和子类 """

import datetime,os

def timeSeq()->str:
    '''返回当前时间的字符串 精确到毫秒'''
    return datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S.%f')

def path_combine_relavabs(folder:str,relav:str)->str:
    '''在路径内新建文件时需要合并文件名与路径'''
    return os.path.normpath(os.path.join(os.path.abspath(folder),relav))