"""
last step
"""

from autils import Logger
from autils import OST
from functools import partial
import os
import subprocess

logger = Logger(filename="work_backup.log", when="d").logger
cmd = partial(OST.sudo_cmd, "kevinkong")


def cmd_executor(cmd):
    cmdlist = cmd.split(" ")
    return subprocess.check_output(cmdlist).decode('utf-8').strip()


class Item(object):

    def __init__(self, directory=None, origin="origin"):
        self.directory = directory
        self.origin = origin


class Work(object):
    """
    检查工作目录
    """

    def __init__(self, items=None):
        if items is None:
            logger.warn("工作目录为空")
            self.items = []
        else:
            self.items = items

    def backup(self):
        """
        检查未提交的工作
        """
        for item in self.items:
            # 切换工作目录
            os.chdir(item.directory)
            print("正在检查{}".format(item.directory))
            # 检查是否有未push的代码
            status_str = subprocess.check_output(
                ["git", "status"]).decode("utf-8")
            # 获取当前分支
            branch = cmd_executor(
                "git rev-parse --abbrev-ref HEAD")
            print(status_str)
            if "Changes not staged for commit" in status_str:
                print("当前{}分支有尚未提交的代码，正在提交...".format(branch))
                # 有尚未提交的代码
                os.system("git add .")
                os.system("git commit -m 'robot commited.'")
            if "Your branch is ahead of" in status_str:
                print("当前{}分支有未推送的代码，正在远端{}推送..".format(
                    branch, item.origin))
                # 把代码提交到远程桌面库
                os.system("git push {} {}".format(item.origin, branch))

            print("目录{}，检查完成".format(item.directory))
