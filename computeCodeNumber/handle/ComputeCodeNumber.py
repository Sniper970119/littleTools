# -*- coding:utf-8 -*-
import os
import time
import datetime


class ComputeCodeNumber():
    def __init__(self, fileFormatList, ignoreBlank, ignoreComment):
        self.fileFormatList = fileFormatList
        self.ignoreBlank = ignoreBlank
        self.ignoreComment = ignoreComment
        self.filelists = []
        self.file = open('./codeNumber.txt', 'w')
        self.file.write('运行时间：' + str(datetime.datetime.strptime(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()),
                                                                 '%Y-%m-%d-%H-%M-%S')) + '\n过滤条件：' + str(
            fileFormatList) + '\n')
        if ignoreBlank == 1:
            self.file.write('是否忽略空白行：True\n')
        else:
            self.file.write('是否忽略空白行：False\n')
        if ignoreComment == 1:
            self.file.write('是否忽略注释行：True\n')
        else:
            self.file.write('是否忽略注释行：False\n')
        self.file.write('\n\n各文件详细行数\n')

    def compute(self):
        startTime = time.clock()
        self.getFile()
        totalline = 0
        for filelist in self.filelists:
            totalline = totalline + self.countLine(filelist)
        return totalline, '%0.2f s' % (time.clock() - startTime)

    # 遍历文件, 递归遍历文件夹中的所有
    def getFile(self):
        global filelists
        for parent, dirnames, filenames in os.walk('./'):
            for filename in filenames:
                ext = filename.split('.')[-1]
                # 只统计指定的文件类型，略过一些log和cache文件
                if ext in self.fileFormatList:
                    self.filelists.append(os.path.join(parent, filename))

    # 统计一个文件的行数
    def countLine(self, fname):
        count = 0
        for file_line in open(fname).xreadlines():
            count += 1
            if self.ignoreBlank == 1:
                if file_line == '' or file_line == '\n':  # 过滤掉空行
                    count -= 1
            if self.ignoreComment == 1:
                fileLine = file_line.strip()
                if fileLine.startswith('/'):
                    count -= 1
                if fileLine.startswith('#'):
                    count -= 1
                if fileLine.startswith('*'):
                    count -= 1
        print(fname + '----', count)
        self.fileSave(str(fname) + '\t\t' + str(count) + '\n')
        return count

    def fileSave(self, data):
        self.file.write(data)
        # 关闭文件流
