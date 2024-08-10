"""
程序入口点。
"""

from pathlib import Path
import sys
import tkinter as tk
from tkinter import filedialog
import logging
import os
import datetime

# 弄获取 %localappdata% ({system_disk}:\Users\{username}\Appdata\local)的路径
LOCALAPPDATA = Path(os.path.expandvars("%LOCALAPPDATA%"))
# 配置日志记录
(WORKDIR := LOCALAPPDATA / "LiteLoaderQQNT Auto Patch").mkdir(exist_ok=True)
(LOGDIR := LOCALAPPDATA / "LiteLoaderQQNT Auto Patch/Logs").mkdir(exist_ok=True)


def mklogs():
    """
    日志初始化。
    """
    nowtime = datetime.datetime.now().strftime("%Y-%m-%d")
    logging.basicConfig(
        filename=LOGDIR / f"{nowtime}.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )


# 检测有没有源目录
def vape_qq():
    """
    获取 QQNT 目录。如果找不到，弹窗要求用户选择 QQNT 源目录。
    """
    if (ini := WORKDIR / "QQNT_file_path.ini").exists():
        with ini.open("r", encoding="utf-8") as f:
            return Path(f.read())
    # 创建一个隐藏的主窗口
    root = tk.Tk()
    root.iconbitmap(default="C:/Windows/System32/Shell32.dll")
    root.withdraw()  # 隐藏主窗口
    # 打开文件选择对话框
    qqnt_path = filedialog.askdirectory(title="选择 QQNT 的所在文件夹")
    # 将选择的路径写入配置文件
    if not qqnt_path:
        print("你没有选择 QQNT 的位置，请重试。")
        return None
    logging.info("QQNT 的文件路径: %s", qqnt_path)  # 打印文件路径
    qqnt_path = Path(qqnt_path)
    if not qqnt_path.exists():
        print("你选择的 QQNT 的位置不存在，请重试。")
        return None

    with ini.open("w", encoding="utf-8") as f:
        f.write(qqnt_path.as_posix())

    return qqnt_path


def vape_ll():
    """
    获取 LiteLoaderQQNT 目录。如果找不到，弹窗要求用户选择。
    """
    if (ini := WORKDIR / "LiteLoaderQQNT_file_path.ini").exists():
        with ini.open("r", encoding="utf-8") as f:
            return Path(f.read())
    # 创建一个隐藏的主窗口
    root = tk.Tk()
    root.iconbitmap(default="C:/Windows/System32/Shell32.dll")
    root.withdraw()  # 隐藏主窗口
    # 打开文件选择对话框
    qqnt_path = filedialog.askdirectory(title="选择 LiteLoaderQQNT 的所在文件夹")
    # 将选择的路径写入配置文件
    if not qqnt_path:
        print("你没有选择 LiteLoaderQQNT 的位置，请重试。")
        return None
    logging.info("LiteLoaderQQNT 的文件路径: %s", qqnt_path)  # 打印文件路径
    qqnt_path = Path(qqnt_path)
    if not qqnt_path.exists():
        print("你选择的 LiteLoaderQQNT 的位置不存在，请重试。")
        return None

    with ini.open("w", encoding="utf-8") as f:
        f.write(qqnt_path.as_posix())

    return qqnt_path


if __name__ == "__main__":
    mklogs()
    PATHQQ = vape_qq()
    if not PATHQQ:
        sys.exit(-1)
    PATHLL = vape_ll()
    if not PATHLL:
        sys.exit(-1)
    with (PATHQQ / "resources/app/app_launcher/index.js").open(
        "w", encoding="utf-8"
    ) as fxxkqq:
        fxxkqq.write(
            f"require(String.raw`{PATHLL}`);\nrequire('./launcher.node').load('external_index', module);"
        )
