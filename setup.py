try:
    from setuptools import setup, find_packages
except:
    from distutils.core import setup
from setuptools.command.install import install
import pkg_resources
import sys
import site
import os
from configparser import ConfigParser
from subprocess import call, Popen, PIPE
import work

# class InstallCommand(install):
    
    # def initialize_options(self):
    #     install.initialize_options(self)

    # def finalize_options(self):
    #     print('正在安装服务...')
    #     # pth = self.binaries_directory()
    #     pth = os.path.abspath(os.path.dirname(__file__))
    #     if not pth:
    #         raise ("目标文件夹查找失败,安装失败")
    #     cf = open('/lib/systemd/system/moyao.service', 'w')
    #     fcontent = [
    #         "[Unit]\n",
    #         "Description = MoYao Service\n\n",
    #         "[Service]\n",
    #         "Environment='DISPLAY=:0'\n",
    #         "Restart=on-failure\n",
    #         "ExecStart={0}\n".format(
    #             "/usr/bin/moyao-bin -c /etc/moyao/config.ini"),
    #         "RemainAfterExit=yes\n\n",
    #         "[Install]\n",
    #         "WantedBy=multi-user.target"
    #     ]
    #     cf.writelines(fcontent)
    #     install.finalize_options(self)


    #     print('安装完成')

    # def run(self):
    #     install.run(self)
    #     install.do_egg_install(self)
    #     # 给可执行文件执行权限
    #     os.chmod("/usr/bin/moyao-bin", int('755', 8))
    #     # 给日志和配置文件写入权限
    #     # os.chmod("/var/log/moyao/moyao.log", int('777', 8))
    #     # os.chmod("/etc/moyao/config.ini", int('777', 8))
    #     print('启动服务中...')
    #     call(["systemctl", "enable", "moyao.service"])
    #     call(["systemctl", "daemon-reload"])
    #     r = call(["systemctl", "restart", "moyao.service"])
    #     p = Popen("systemctl status moyao", shell=True, stdout=PIPE)
    #     rs = p.communicate()[0].decode("utf-8").split('\n')
    #     ls = (line for line in rs if 'running' in line)
    #     if ls:
    #         print('服务启动成功')
    #     else:
    #         print("服务启动失败,请使用命令systemctl status moyao查看具体原因")
        


data_files = [
    ('/etc/work_util/', ['config.ini']),
    ('/usr/bin', ['wbackup']),
    ('.', ['requirements.txt'])
]

setup(name='Work_backup',
      version=work.__version__,
      description='A Tools for working backup.',
      author='Kevin Kong',
      author_email='kfxw2007@163.com',
      license='http://www.apache.org/licenses/LICENSE-2.0.html',
      url='',
      data_files=data_files,
      packages=find_packages(),
      package_dir={'%s' % 'work_util': 'work_util'},
      include_package_data=True,
      python_requires='>=3.5',
      install_requires=[
          "autils"
      ],
    )
