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

            # 获取当前分支
            branch = cmd_executor(
                "git rev-parse --abbrev-ref HEAD")
            # 检查是否有未提交的代码
            status_str = subprocess.check_output(
                ["git", "status"]).decode("utf-8")
            # 检查当前工作目录是否有遗漏工作
            if "Changes not staged for commit" in status_str:
                print("当前{}分支有尚未提交的代码，正在提交...".format(branch))
                # 有尚未提交的代码
                os.system("git add .")
                os.system("git commit -m 'robot commited.'")

            # 获取当前所有的分支
            branches = [b.strip() for b in cmd_executor(
                "git branch").replace("*", "").split("\n")]

            # 切换分支
            for branch in branches:
                print('切换到{}分支'.format(branch))
                os.system("git checkout {}".format(branch))
                try:
                    # 检查当前分支是否有未push的commit
                    unpushed = cmd_executor(
                        "git log {}/{}..{}".format(item.origin, branch, branch))
                    if unpushed:
                        print("当前{}分支有未推送的代码，正在远端{}推送..".format(
                            branch, item.origin))
                        # 把代码提交到远程桌面库
                        os.system("git push {} {}".format(item.origin, branch))
                except Exception as ex:
                    # 远端并未创建分支，直接推送
                    print("远端没有{}分支，正在远端{}推送..".format(
                        branch, item.origin))
                    # 把代码提交到远程桌面库
                    os.system("git push {} {}".format(item.origin, branch))

            print("目录{}，检查完成".format(item.directory))
            print('=========>(*^_^*)<==========')
