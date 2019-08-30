# -*- coding:utf-8 -*-

import tkinter as tk

from computeCodeNumber import ComputeCodeNumber


class MainWindow():
    def __init__(self):
        self.mainWindow = tk.Tk()
        screenWidth = self.mainWindow.winfo_screenwidth()
        screenHeight = self.mainWindow.winfo_screenheight()
        self.mainWindow.geometry(
            '300x320+' + str(int((screenWidth - 300) / 2)) + '+' + str(int((screenHeight - 320) / 2)))
        self.mainWindow.resizable(width=False, height=False)
        self.mainWindow.title("文件行数计算")

        self.varSelectPython = tk.IntVar()
        self.varSelectJava = tk.IntVar()
        self.varSelectC = tk.IntVar()
        self.varSelectCPP = tk.IntVar()
        self.varSelectH = tk.IntVar()
        self.varSelectCS = tk.IntVar()
        self.varSelectJSP = tk.IntVar()
        self.varSelectPHP = tk.IntVar()
        self.varSelectASPX = tk.IntVar()
        self.varSelectTXT = tk.IntVar()
        self.varSelectASP = tk.IntVar()
        self.varSelectDAT = tk.IntVar()
        self.varSelectIgnoreTheBlankLine = tk.IntVar()
        self.varSelectIgnoreTheCommentLine = tk.IntVar()

        self.paintWindow()

        self.mainWindow.mainloop()

        pass

    def paintWindow(self):
        # 绘制多选框
        showMessage = tk.Label(self.mainWindow, width=30, text='选择需要计算行数的文件后缀（可多选）')
        showMessage.place(x=20, y=20, anchor='nw')
        checkButtonPython = tk.Checkbutton(self.mainWindow, text='.py', variable=self.varSelectPython, onvalue=1,
                                           offvalue=0)
        checkButtonPython.place(x=20, y=40, anchor='nw')
        checkButtonJava = tk.Checkbutton(self.mainWindow, text='.java', variable=self.varSelectJava, onvalue=1,
                                         offvalue=0)
        checkButtonJava.place(x=90, y=40, anchor='nw')
        checkButtonC = tk.Checkbutton(self.mainWindow, text='.c', variable=self.varSelectC, onvalue=1, offvalue=0)
        checkButtonC.place(x=160, y=40, anchor='nw')
        checkButtonCPP = tk.Checkbutton(self.mainWindow, text='.cpp', variable=self.varSelectCPP, onvalue=1, offvalue=0)
        checkButtonCPP.place(x=230, y=40, anchor='nw')
        checkButtonH = tk.Checkbutton(self.mainWindow, text='.h', variable=self.varSelectH, onvalue=1, offvalue=0)
        checkButtonH.place(x=20, y=70, anchor='nw')
        checkButtonCS = tk.Checkbutton(self.mainWindow, text='.cs', variable=self.varSelectCS, onvalue=1, offvalue=0)
        checkButtonCS.place(x=90, y=70, anchor='nw')
        checkButtonJSP = tk.Checkbutton(self.mainWindow, text='.jsp', variable=self.varSelectJSP, onvalue=1, offvalue=0)
        checkButtonJSP.place(x=160, y=70, anchor='nw')
        checkButtonPHP = tk.Checkbutton(self.mainWindow, text='.php', variable=self.varSelectPHP, onvalue=1, offvalue=0)
        checkButtonPHP.place(x=230, y=70, anchor='nw')
        checkButtonWEB = tk.Checkbutton(self.mainWindow, text='.aspx', variable=self.varSelectASPX, onvalue=1,
                                        offvalue=0)
        checkButtonWEB.place(x=20, y=100, anchor='nw')
        checkButtonTXT = tk.Checkbutton(self.mainWindow, text='.txt', variable=self.varSelectTXT, onvalue=1, offvalue=0)
        checkButtonTXT.place(x=90, y=100, anchor='nw')
        checkButtonWEB1 = tk.Checkbutton(self.mainWindow, text='.asp', variable=self.varSelectASP, onvalue=1,
                                         offvalue=0)
        checkButtonWEB1.place(x=160, y=100, anchor='nw')
        checkButtonHAHA = tk.Checkbutton(self.mainWindow, text='.xml', variable=self.varSelectDAT, onvalue=1,
                                         offvalue=0)
        checkButtonHAHA.place(x=230, y=100, anchor='nw')

        # 绘制是否忽略空白行选择
        checkButtonIfIgnoreTheBlankLine = tk.Checkbutton(self.mainWindow, text='忽略空白行',
                                                         variable=self.varSelectIgnoreTheBlankLine, onvalue=1,
                                                         offvalue=0)
        checkButtonIfIgnoreTheBlankLine.place(x=20, y=150, anchor='nw')
        checkButtonIfIgnoreTheCommentLine = tk.Checkbutton(self.mainWindow, text='忽略注释行',
                                                           variable=self.varSelectIgnoreTheCommentLine, onvalue=1,
                                                           offvalue=0)
        checkButtonIfIgnoreTheCommentLine.place(x=110, y=150, anchor='nw')
        # 绘制按钮
        computeButton = tk.Button(text='计算', command=self.computeButton, width=10)
        computeButton.place(x=200, y=150, anchor='nw')
        # 显示数据按钮
        self.showLineNumberLabel = tk.Label(self.mainWindow, width=20, text='总行数：')
        self.showLineNumberLabel.place(x=10, y=190, anchor='nw')
        self.showComputeTimeLabel = tk.Label(self.mainWindow, width=20, text='运行时间：')
        self.showComputeTimeLabel.place(x=10, y=220, anchor='nw')
        self.showDetailLabel = tk.Label(self.mainWindow, width=40, text='')
        self.showDetailLabel.place(x=10, y=250, anchor='nw')
        self.showLienceLabel1 = tk.Label(self.mainWindow, width=20, text='Create By Sniper', fg='gray')
        self.showLienceLabel1.place(x=80, y=280, anchor='nw')
        self.showLienceLabel2 = tk.Label(self.mainWindow, width=20, text='zhaoyu@sniper97.cn', fg='gray')
        self.showLienceLabel2.place(x=80, y=300, anchor='nw')
        pass

    def computeButton(self):
        fileFormatList = self.createFileFormatList()
        computeTool = ComputeCodeNumber(fileFormatList, self.varSelectIgnoreTheBlankLine.get(),
                                        self.varSelectIgnoreTheCommentLine.get())
        fileLine, runTume = computeTool.compute()
        print(fileLine)
        print(runTume)
        self.showLineNumberLabel.config(text='总行数：' + str(fileLine))
        self.showComputeTimeLabel.config(text='运行时间：' + str(runTume))
        self.showDetailLabel.config(text='详细信息查看本程序目录下的codeNumber.txt')
        pass

    def createFileFormatList(self):
        fileFormatList = []
        if self.varSelectPython.get() == 1:
            fileFormatList.append('py')
        if self.varSelectJava.get() == 1:
            fileFormatList.append('java')
        if self.varSelectC.get() == 1:
            fileFormatList.append('c')
        if self.varSelectCPP.get() == 1:
            fileFormatList.append('cpp')
        if self.varSelectH.get() == 1:
            fileFormatList.append('h')
        if self.varSelectCS.get() == 1:
            fileFormatList.append('cs')
        if self.varSelectJSP.get() == 1:
            fileFormatList.append('jsp')
        if self.varSelectPHP.get() == 1:
            fileFormatList.append('php')
        if self.varSelectASPX.get() == 1:
            fileFormatList.append('aspx')
        if self.varSelectTXT.get() == 1:
            fileFormatList.append('txt')
        if self.varSelectASP.get() == 1:
            fileFormatList.append('asp')
        if self.varSelectDAT.get() == 1:
            fileFormatList.append('xml')
        return fileFormatList


if __name__ == '__main__':
    a = MainWindow()
