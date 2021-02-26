#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'YinJia'

import os


def new_report(testreport):
    """
    生成最新的测试报告文件
    :param testreport:
    :return:返回文件
    """
    # 获取report目录下的文件列表
    lists = os.listdir(testreport)
    # 对目录下的文件按创建时间进行排序
    lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
    # 获取新文件的绝对路径，report的路径拼上最新的HTML文件名
    file_new = os.path.join(testreport, lists[-1])
    return file_new
