#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter  # 定义窗体类
import os
import requests
from tkinter import ttk
from tkinter.ttk import Treeview

LOGO_PATH = "./" + os.sep + "Connect.ico"  # LGO⽂件路径
state_list = [200, 401, 403, 404]
state_code = []
flag_1 = False
flag_2 = False
flag_3 = False
flag_4 = False


class MainForm:  # 定义窗体类
    def __init__(self):  # 构造⽅法⾥⾯进⾏窗体控制
        self.root = tkinter.Tk()  # 创建⼀个窗体
        self.root.title("CScan             Author: Cuer       QQ: 1633772030")  # 设置标题
        self.root.iconbitmap(LOGO_PATH)  # 设置LOGO的资源
        self.root.geometry("800x600")  # 设置最⼩化尺⼨
        # self.root['background'] = 'WhiteSmoke'  # 设置背景
        self.root.resizable(width=0, height=0)  # 固定尺寸
        # 第一行
        self.domainName_label = tkinter.Label(self.root, text="域名: ", width=6, height=1, font=("微软雅黑", 10))
        self.domain_text = tkinter.Text(self.root, width=65, height=1, font=("微软雅黑", 10), relief="ridge")
        self.button_run = tkinter.Button(self.root, text="开始扫描", width=10, font=("微软雅黑", 9), command=self.runScan)
        self.button_stop = tkinter.Button(self.root, text="停止扫描", width=10, font=("微软雅黑", 9))
        self.domainName_label.grid(row=0, column=0)
        self.domain_text.grid(row=0, column=1, columnspan=25)
        self.button_run.grid(row=0, column=26, padx=20)
        self.button_stop.grid(row=0, column=27, padx=10)

        # 第二行
        self.threads = tkinter.Label(self.root, text="线程: ", width=7, height=1, font=("微软雅黑", 10))
        self.threads_num = ttk.Combobox(self.root, width=7,
                                        values=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13',
                                                '14',
                                                '15', '16', '17', '18', '19', '20'])
        self.thread_info = tkinter.Label(self.root, text="(条，建议CPU核心*5)", width=15, height=1, font=("微软雅黑", 10))
        self.dict = tkinter.Label(self.root, text="选择字典: ", width=10, height=1, font=("微软雅黑", 10))
        self.dict_path = tkinter.Text(self.root, width=12, height=1, font=("微软雅黑", 10), relief="ridge")
        self.dict_info = tkinter.Label(self.root, text="(读取resource目录下)", width=0, height=1, font=("微软雅黑", 10))
        self.threads.grid(row=1, column=0)
        self.threads_num.grid(row=1, column=1, sticky="W")
        self.thread_info.grid(row=1, column=2, sticky="W")
        self.dict.grid(row=1, column=3, sticky="W")
        self.dict_path.grid(row=1, column=4, sticky="E")
        self.dict_info.grid(row=1, column=5)

        # 第三行
        self.drop = tkinter.Label(self.root, text="超时: ", width=7, height=1, font=("微软雅黑", 10))
        self.drop_time = ttk.Combobox(self.root, width=7, values=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
        self.drop_info = tkinter.Label(self.root, text="(秒，丢弃超时的页面)", width=15, height=1, font=("微软雅黑", 10))
        self.state = tkinter.Label(self.root, text="状态码: ", width=9, height=1, font=("微软雅黑", 10))
        self.state_200 = tkinter.Checkbutton(self.root, text='200', command=self.ch1)
        self.state_401 = tkinter.Checkbutton(self.root, text='401', command=self.ch2)
        self.state_403 = tkinter.Checkbutton(self.root, text='403', command=self.ch3)
        self.state_404 = tkinter.Checkbutton(self.root, text='404', command=self.ch4)
        self.drop.grid(row=2, column=0)
        self.drop_time.grid(row=2, column=1, sticky="W")
        self.drop_info.grid(row=2, column=2, sticky="W")
        self.state.grid(row=2, column=3, sticky="E")
        self.state_200.place(x=340, y=55)
        self.state_401.place(x=400, y=55)
        self.state_403.place(x=460, y=55)
        self.state_404.place(x=520, y=55)
        self.Show_Res()
        self.LOG = tkinter.Text(self.root, relief="solid", borderwidth=1, height=15, width=87, fg='gray', font=7)
        self.LOG.place(x=51, y=326)
        self.log_insert("@Version: 1.0.0\n@Author: Cuer\n@E-mail: cuerz@qq.com\n[+] Thank you for using CScan\n")

        self.root.mainloop()

    def ch1(self):
        global flag_1
        flag_1 = not flag_1
        if flag_1:
            state_code.append(state_list[0])
        else:
            state_code.remove(state_list[0])
        self.LOG.delete("5.0", "end")
        self.log_insert("\n[+] state_code: ")
        for state in state_code:
            self.log_insert(str(state) + " ")
        self.log_insert("\n")

    def ch2(self):
        global flag_2
        flag_2 = not flag_2
        if flag_2:
            state_code.append(state_list[1])
        else:
            state_code.remove(state_list[1])
        self.LOG.delete("5.0", "end")
        self.log_insert("\n[+] state_code: ")
        for state in state_code:
            self.log_insert(str(state) + " ")
        self.log_insert("\n")

    def ch3(self):
        global flag_3
        flag_3 = not flag_3
        if flag_3:
            state_code.append(state_list[2])
        else:
            state_code.remove(state_list[2])
        self.LOG.delete("5.0", "end")
        self.log_insert("\n[+] state_code: ")
        for state in state_code:
            self.log_insert(str(state) + " ")
        self.log_insert("\n")

    def ch4(self):
        global flag_4
        flag_4 = not flag_4
        if flag_4:
            state_code.append(state_list[3])
        else:
            state_code.remove(state_list[3])
        self.LOG.delete("5.0", "end")
        self.log_insert("\n[+] state_code: ")
        for state in state_code:
            self.log_insert(str(state) + " ")
        self.log_insert("\n")

    def Show_Res(self):
        self.root.treeview = Treeview(self.root, show='headings')
        self.root.treeview['columns'] = ("ID", "地址", "HTTP响应")
        self.root.treeview.heading(column="ID", text="ID")
        self.root.treeview.heading(column="地址", text="地址")
        self.root.treeview.heading(column="HTTP响应", text="HTTP响应")
        self.root.treeview.column('ID', width=100, anchor=tkinter.W)
        self.root.treeview.column('地址', width=400, anchor=tkinter.W)
        self.root.treeview.column('HTTP响应', width=200, anchor=tkinter.W)
        self.root.treeview.place(x=50, y=100)

    def delete_tree(self, tree):
        for item in tree.get_children():
            tree.delete(item)

    def log_insert(self, str):  # update log
        self.LOG.insert("end", chars=str)
        self.LOG.see("end")

    def runScan(self):
        self.LOG.delete("6.0", "end")
        self.log_insert("\n[+] Start Scanning......\n")
        self.delete_tree(self.root.treeview)
        domain = self.domain_text.get("0.0", "end").strip()
        dict = self.dict_path.get("0.0", "end").strip()
        dict = os.path.join("./resource", dict)
        drop_time=self.drop_time.get()
        if drop_time=='':
            drop_time=0
        else:
            drop_time=int(drop_time)
        self.spide(domain, dict,drop_time)
        self.log_insert("[+] End Scanning......\n")

    def spide(self, domain, dict,drop_time):
        try:
            with open(dict, 'r', encoding='UTF-8') as readfile:
                directory=readfile.readlines()
            readfile.close()
        except:
            self.log_insert("No such file or directory in resource\n")
            return
        try:
            for index, dirs in enumerate(directory):
                    # 生成对应url
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"
                    }
                    url = domain + dirs.strip('\n')
                    resp = requests.get(url=url, headers=headers,timeout=drop_time)
                    code = resp.status_code  # 获得状态码
                    if code in state_code:
                        self.root.treeview.insert(parent="", index="end", values=(index + 1, url, code))
        except:
            return


def main():
    MainForm()  # 实例化窗体类


if __name__ == "__main__":
    main()
