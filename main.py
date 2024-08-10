"""
程序入口点。
"""

import tkinter as tk
from tkinter import filedialog
import logging
import os
import datetime
import time

# 弄获取 %localappdata% ({system_disk}:\Users\{username}\Appdata\local)的路径
localappdata = os.path.expandvars("%LOCALAPPDATA%")
# 配置日志记录
if not os.path.exists(f"{localappdata}/LiteLoaderQQNT Auto Patch"):
    os.mkdir(f"{localappdata}/LiteLoaderQQNT Auto Patch/")
    os.mkdir(f"{localappdata}/LiteLoaderQQNT Auto Patch/Logs")
if not os.path.exists(f"{localappdata}/LiteLoaderQQNT Auto Patch/Logs"):
    os.mkdir(f"{localappdata}/LiteLoaderQQNT Auto Patch/Logs")


def mklogs():
    """
    日志初始化。
    """
    nowtime = datetime.datetime.now()
    day_string = nowtime.strftime("%Y-%m-%d")
    logging.basicConfig(
        filename=f"{localappdata}/LiteLoaderQQNT Auto Patch/Logs/{day_string}.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )


mklogs()


# 检测有没有源目录
def vape_qq():
    """
    获取 QQNT 目录。如果找不到，弹窗要求用户选择 QQNT 源目录。
    """
    if not os.path.exists(
        f"{localappdata}/LiteLoaderQQNT Auto Patch/QQNT_file_path.ini"
    ):
        with open(
            f"{localappdata}/LiteLoaderQQNT Auto Patch/QQNT_file_path.ini",
            "w",
            encoding="utf-8",
        ) as f:
            f.write("")
        # 创建一个隐藏的主窗口
        root = tk.Tk()
        root.iconbitmap(default="C:/Windows/System32/Shell32.dll")
        root.withdraw()  # 隐藏主窗口
        # 打开文件选择对话框
        qqnt_path = filedialog.askdirectory(title="选择 QQNT 的所在文件夹")
        # 将选择的路径写入配置文件
        if qqnt_path:
            logging.info("QQNT 的文件路径: %s", qqnt_path)  # 打印文件路径
            with open(
                f"{localappdata}/LiteLoaderQQNT Auto Patch/QQNT_file_path.ini",
                "w",
                encoding="utf8",
            ) as f:
                f.write(qqnt_path)
        else:
            print("你没有选择 QQNT 的位置，请重试。")

            time.sleep(3)


def vape_ll():
    """
    获取 LiteLoaderQQNT 目录。如果找不到，弹窗要求用户选择。
    """
    if not os.path.exists(
        f"{localappdata}/LiteLoaderQQNT Auto Patch/LiteLoaderQQNT_file_path.ini"
    ):
        with open(
            f"{localappdata}/LiteLoaderQQNT Auto Patch/LiteLoaderQQNT_file_path.ini",
            "w",
            encoding="utf-8",
        ) as llqqnt:
            llqqnt.write("")
        # 创建一个隐藏的主窗口
        root = tk.Tk()
        root.iconbitmap(default="C:/Windows/System32/Shell32.dll")
        root.withdraw()  # 隐藏主窗口
        # 打开文件选择对话框
        llqqnt_path = filedialog.askdirectory(title="选择 LiteLoaderQQNT 的所在文件夹")
        # 将选择的路径写入配置文件
        if llqqnt_path:
            logging.info("LiteLoaderQQNT 的文件路径: %s", llqqnt_path)  # 打印文件路径
            with open(
                f"{localappdata}/LiteLoaderQQNT Auto Patch/LiteLoaderQQNT_file_path.ini",
                "w",
                encoding="utf8",
            ) as llqqnt:
                llqqnt.write(llqqnt_path)
        else:
            print("你没有选择 LiteLoaderQQNT 的位置，请重试。")

            time.sleep(3)


vape_qq()
vape_ll()
if os.path.exists(f"{localappdata}/LiteLoaderQQNT Auto Patch/QQNT_file_path.ini"):
    if os.path.exists(
        f"{localappdata}/LiteLoaderQQNT Auto Patch/LiteLoaderQQNT_file_path.ini"
    ):
        with open(
            f"{localappdata}/LiteLoaderQQNT Auto Patch/LiteLoaderQQNT_file_path.ini",
            "r",
            encoding="utf-8",
        ) as latest_loc:
            qqnt_latest_location = latest_loc.read()
        with open(
            f"{localappdata}/LiteLoaderQQNT Auto Patch/QQNT_file_path.ini",
            "r",
            encoding="utf-8",
        ) as qqnt:
            vape = qqnt.read()
            with open(
                f"{vape}/resources/app/app_launcher/index.js", "w", encoding="utf-8"
            ) as fxxkqq:
                fxxkqq.write(
                    f"require(String.raw`{qqnt_latest_location}`);\nrequire('./launcher.node').load('external_index', module);"
                )
    else:
        print("error")
else:
    print("error")
