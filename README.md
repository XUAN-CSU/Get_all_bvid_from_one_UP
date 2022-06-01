# Get_all_bvid_from_one_UP
20220601：祝晅2022年六一儿童节快乐!

代码目的：获得B站一个up主的全部BV号 

使用方法，
## 安装python:https://www.python.org 建议下载python3稳定版本，记得安装时添加路径到系统,并且记得勾选装pip

WIN键 + R 调出一个框，输入cmd进入命令行 在命令行中键入python，查看python版本 ，

C:\Users\Ra>python

Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32

Type "help", "copyright", "credits" or "license" for more information.

exit() <!---是退出python回到命令行---> 

C:\Users\Ra>

此时可以选择更新pip命令如下：C:\Users\Ra>python -m pip install --upgrade pip

Requirement already satisfied: pip in f:\programs\python\python39\lib\site-packages (22.1.2)

## 安装you-get来根据BV号下载B站视频

C:\Users\Ra>pip3 install you-get

可以自行在命令行键入 you-get后回车 可以学习使用如何下载用法

## 在小公主要下载视频的文件夹，把这个20220531.py文件放入这个空白文件夹，右键选中它利用txt文档修改其中的第31行后保存

bilibili_user_id = [282170862] <!---[]中是up主的id 可以是多个人的id --->

空白区域按住Shift + 右键点击空白处，选择 在此处打开Powershell窗口(S)

输入cmd 进入命令行
python ./2022051.py，过一会儿会在这个文件夹中出现对应uid的文档：UserID_282170862_20220601081957571.txt

然后就可以调用you-get 下载 具体命令如下 you-get -I ./UserID_282170862_20220601081957571.txt

开始下载




