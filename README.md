# Wu kong

悟空

## description

auto check your local uncommit changes and push it to remote repository.

自动提交本地尚未提交的代码，并自动推送到远端

## usage

使用说明：

### 安装 

```python
python3 setup.py install
```

### 使用

指定配置文件 -c
```sh
wukong -c /etc/wukong/config.ini
```

或使用默认路径 /etc/wukong/config.ini

### 配置文件说明

```sh
[Directory]
filepath = path.txt
```

filepath指定要同步的git项目文件夹文件

path.txt文件夹内容为git项目完整路径，每个一行

默认同步远端仓库origin，如需指定其他远端仓库在后边跟空格加仓库名

```sh
/home/kevin/codes/Hexo
/home/kevin/codes/addons/shop github
/home/kevin/codes/hft_repository/hft_repository github
/home/kevin/codes/scripts github
/home/kevin/codes/fengxin github
/home/kevin/codes/hft_petrocn_report
/home/kevin/codes/flask_members github
/home/kevin/codes/work_utils
```
